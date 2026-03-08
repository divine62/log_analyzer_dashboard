import streamlit as st
import pandas as pd
from collections import Counter

st.set_page_config(page_title="Log Analyzer Dashboard", layout="wide")

st.title("🖥️ System Log Analyzer Dashboard")

file = st.file_uploader("Upload Log File")

if file is not None:

    lines = file.read().decode().split("\n")

    errors = []
    warnings = []
    failed = []

    for line in lines:

        if "ERROR" in line:
            message = line.split("ERROR")[1].strip()
            errors.append(message)

        elif "WARNING" in line:
            message = line.split("WARNING")[1].strip()
            warnings.append(message)

        elif "FAILED" in line:
            message = line.split("FAILED")[1].strip()
            failed.append(message)

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Errors", len(errors))
    col2.metric("Total Warnings", len(warnings))
    col3.metric("Total Failed Events", len(failed))

    # Error frequency
    error_counts = Counter(errors)

    if error_counts:

        df = pd.DataFrame({
            "Error Message": list(error_counts.keys()),
            "Count": list(error_counts.values())
        })

        st.subheader("Most Common Errors")

        st.dataframe(df)

        st.subheader("Error Distribution")

        chart_data = pd.DataFrame({
            "Type": ["Errors", "Warnings", "Failed"],
            "Count": [len(errors), len(warnings), len(failed)]
        })

        st.bar_chart(chart_data.set_index("Type"))