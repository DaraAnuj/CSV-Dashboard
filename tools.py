import pandas as pd
import matplotlib.pyplot as plt
import json

df = None

def load_csv(path: str):
    global df
    df = pd.read_csv(path)
    return df

def profile_csv() -> str:
    info = {
        "shape": {"rows": df.shape[0], "cols": df.shape[1]},
        "columns": {},
    }
    for col in df.columns:
        info["columns"][col] = {
            "dtype": str(df[col].dtype),
            "nulls": int(df[col].isna().sum()),
            "sample": df[col].dropna().head(3).tolist(),
        }
    return json.dumps(info, default=str)

def run_analysis(code: str) -> str:
    local = {"df": df, "pd": pd}
    try:
        exec(code, local)
        result = local.get("result", "Code ran but no `result` variable was set.")
        return str(result)
    except Exception as e:
        return f"ERROR: {e}"

def plot_chart(chart_type: str, x_col: str, y_col: str = None, title: str = "") -> str:
    fig, ax = plt.subplots(figsize=(7, 4))
    if chart_type == "histogram":
        df[x_col].dropna().plot(kind="hist", ax=ax, title=title or x_col)
    elif chart_type == "bar":
        if y_col and y_col in df.columns:
            df.groupby(x_col)[y_col].mean().plot(kind="bar", ax=ax, title=title)
        else:
            df[x_col].value_counts().plot(kind="bar", ax=ax, title=title or x_col)
    elif chart_type == "line":
        df.plot(x=x_col, y=y_col, kind="line", ax=ax, title=title)
    plt.tight_layout()
    plt.savefig("chart.png", dpi=120)
    plt.close()
    return "chart.png saved."