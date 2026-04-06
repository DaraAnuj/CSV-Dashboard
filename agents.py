import anthropic, json
from tools import load_csv, profile_csv, run_analysis, plot_chart
from schemas import TOOL_SCHEMAS

client = anthropic.Anthropic()

TOOL_MAP = {
    "profile_csv": lambda _: profile_csv(),
    "run_analysis": lambda inp: run_analysis(inp["code"]),
    "plot_chart":   lambda inp: plot_chart(
                        inp["chart_type"], inp["x_col"],
                        inp.get("y_col"), inp.get("title", "")
                    ),
}

def run_agent(csv_path: str, user_question: str):
    load_csv(csv_path)
    print(f"\nQuestion: {user_question}\n{'─'*50}")

    messages = [{"role": "user", "content": user_question}]
    system = (
        "You are a data analyst. A CSV file is already loaded as `df`. "
        "Always call profile_csv first to understand the data before answering. "
        "Use run_analysis for calculations. Use plot_chart when a visual helps. "
        "When you have a full answer, respond in plain text — no more tool calls."
    )

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system=system,
            tools=TOOL_SCHEMAS,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    print("\nInsight:\n" + block.text)
            break

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"  → calling tool: {block.name}")
                    output = TOOL_MAP[block.name](block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": output,
                    })
            messages.append({"role": "user", "content": tool_results})

if __name__ == "__main__":
    import sys
    csv_path = sys.argv[1]
    question = sys.argv[2]
    run_agent(csv_path, question)