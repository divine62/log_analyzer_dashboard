import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser(description="Log File Analyzer")
parser.add_argument("--file", required=True, help="Path to log file")

args = parser.parse_args()

log_file = args.file

errors = []
warnings = []
failed = []

with open(log_file, "r") as file:
    for line in file:

        if "ERROR" in line:
            message = line.split("ERROR")[1].strip()
            errors.append(message)

        elif "WARNING" in line:
            message = line.split("WARNING")[1].strip()
            warnings.append(message)

        elif "FAILED" in line:
            message = line.split("FAILED")[1].strip()
            failed.append(message)

error_counts = Counter(errors)
warning_counts = Counter(warnings)

print("\n===== LOG ANALYSIS REPORT =====\n")

print("Total Errors:", len(errors))
print("Total Warnings:", len(warnings))
print("Total Failed Events:", len(failed))

print("\nMost Common Errors:\n")

for err, count in error_counts.items():
    print(err, ":", count)

os.makedirs("output", exist_ok=True)

report_text = f"""
===== LOG ANALYSIS REPORT =====

Total Errors: {len(errors)}
Total Warnings: {len(warnings)}
Total Failed Events: {len(failed)}
"""

with open("output/report.txt", "w") as f:
    f.write(report_text)

df = pd.DataFrame({
    "Error": list(error_counts.keys()),
    "Count": list(error_counts.values())
})

df.to_excel("output/log_report.xlsx", index=False)

plt.bar(error_counts.keys(), error_counts.values())
plt.xticks(rotation=45)
plt.title("Error Frequency")
plt.tight_layout()
plt.savefig("output/error_graph.png")

print("\nReports generated in /output folder")