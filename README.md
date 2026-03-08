# log_analyzer_dashboard
Python-based system log analyzer that detects errors, warnings, and failed events from application logs and visualizes them using a Streamlit dashboard.
# System Log Analyzer Dashboard

A Python-based tool that analyzes system and application log files to detect errors, warnings, and failed events.
The project generates automated reports, visualizes error patterns, and provides an interactive dashboard for quick troubleshooting.

---

## Features

* Detects **ERROR, WARNING, and FAILED** events from log files
* Extracts and analyzes recurring error patterns
* Generates **automated summary reports**
* Creates **visual graphs of error frequency**
* Interactive **Streamlit dashboard for log monitoring**

---

## Tech Stack

* Python
* Pandas
* Matplotlib
* Streamlit

---

## Project Structure

```id="yy6v99"
log-analyzer-dashboard
│
├── logs
│   └── sample_log.txt
│
├── output
│
├── log_analyzer.py
├── dashboard.py
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1. Install dependencies

```id="4bovod"
pip install -r requirements.txt
```

### 2. Run the log analyzer

```id="y3c61v"
python log_analyzer.py --file logs/sample_log.txt
```

### 3. Run the dashboard

```id="mjkvht"
streamlit run dashboard.py
```

Open the dashboard in your browser:

```id="s5f3y0"
http://localhost:8501
```

Upload a log file to analyze system errors and warnings.

---

## Example Log Format

```id="nrm7me"
2026-03-07 10:13:15 ERROR Database connection failed
2026-03-07 10:14:22 WARNING Disk space running low
2026-03-07 10:16:10 FAILED Login attempt
```

---

## Use Case

System logs are essential for diagnosing application failures.
This project simulates how **technical support engineers and system administrators analyze logs to detect system issues and identify recurring failures quickly.**

---
## Dashboard Preview

![Dashboard](images/dashboard.png)

## Future Improvements

* Real-time log monitoring
* Email alerts for critical errors
* Advanced log pattern detection using regex
* Integration with cloud monitoring tools

