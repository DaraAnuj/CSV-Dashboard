# CSV Insight Agent

An agentic AI tool that lets you chat with any CSV file in plain English. Powered by the Anthropic Claude API — just point it at a CSV, ask a question, and it profiles the data, runs analysis, and generates charts automatically.

---

## Demo

```
Question: What is the survival rate by passenger class? Plot a bar chart.
──────────────────────────────────────────────────
  → calling tool: profile_csv
  → calling tool: run_analysis
  → calling tool: plot_chart

Insight:
1st class had the highest survival rate at 63%, followed by
2nd class at 47%, and 3rd class at 24%. Chart saved to chart.png.
```

---

## How it works

The agent runs a loop:
1. You give it a CSV file and a question
2. Claude decides which tool to call (profile, analyse, or plot)
3. Your code runs the tool and sends the result back to Claude
4. Claude reasons over the result and either calls another tool or gives a final answer

---

## Project structure

```
csv-agent/
├── agent.py       # The agent loop — the brain of the operation
├── tools.py       # The actual pandas/matplotlib functions Claude can call
├── schemas.py     # JSON descriptions of tools that Claude reads
└── README.md
```

---

## Setup

```powershell
# 1. Clone the repo and enter the folder
git clone https://github.com/your-username/csv-agent.git
cd csv-agent

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\Activate.ps1        # Windows PowerShell
# source venv/bin/activate       # Mac / Linux

# 3. Install dependencies
pip install anthropic pandas matplotlib

# 4. Set your API key
$env:ANTHROPIC_API_KEY="sk-ant-your-key-here"   # Windows (current session)
# export ANTHROPIC_API_KEY="sk-ant-your-key-here" # Mac / Linux
```

To persist the API key across sessions on Windows:
```powershell
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-your-key-here", "User")
```

---

## Usage

```powershell
python agent.py <path-to-csv> "<your question>"
```

**Examples:**

```powershell
# CSV in the same folder
python agent.py titanic.csv "What is the survival rate by passenger class?"

# CSV anywhere on your machine
python agent.py "C:\Users\You\Downloads\sales.csv" "What are the top 5 products by revenue?"

# Ask for a chart
python agent.py data.csv "Show me a histogram of age distribution"
```

The agent saves any generated charts as `chart.png` in the project folder.

---

## Available tools

| Tool | What it does |
|------|-------------|
| `profile_csv` | Returns shape, column names, data types, null counts, and sample values |
| `run_analysis` | Runs a pandas snippet against the dataframe and returns the result |
| `plot_chart` | Generates a bar, line, or histogram chart and saves it as `chart.png` |

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `anthropic` | Claude API client |
| `pandas` | Data loading and analysis |
| `matplotlib` | Chart generation |

---

## License

MIT
