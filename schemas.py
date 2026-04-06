TOOL_SCHEMAS = [
    {
        "name": "profile_csv",
        "description": "Returns shape, column names, dtypes, null counts, and sample values from the loaded CSV.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "run_analysis",
        "description": (
            "Runs a pandas code snippet against the dataframe `df`. "
            "You must assign the final result to a variable named `result`. "
            "Example: result = df['sales'].sum()"
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "A single Python expression or block using pandas. Must set `result`.",
                },
            },
            "required": ["code"],
        },
    },
    {
        "name": "plot_chart",
        "description": "Generates and saves a chart as chart.png.",
        "input_schema": {
            "type": "object",
            "properties": {
                "chart_type": {"type": "string", "enum": ["histogram", "bar", "line"]},
                "x_col":      {"type": "string", "description": "Column name for x axis"},
                "y_col":      {"type": "string", "description": "Column for y axis (not needed for histogram)"},
                "title":      {"type": "string"},
            },
            "required": ["chart_type", "x_col"],
        },
    },
]