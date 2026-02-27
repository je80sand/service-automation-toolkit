# Service Automation Toolkit (Python)

A command-line Python tool that simulates a real-world service desk workflow.  
It validates customer service tickets, builds structured job records, and outputs clean, human-readable service summaries.

This project demonstrates practical automation, modular Python design, and readable output suitable for operational or support environments.

## 🎯 Why This Project Exists

This project was built to demonstrate how Python can be used to automate everyday service and field-support workflows.

It mirrors real technician and service-desk tasks such as:
- Accepting structured user input
- Validating required information
- Creating standardized job records
- Producing clean, readable summaries for reporting or documentation

The goal is to showcase practical Python automation skills that translate directly to real operational environments.
---

## 🧠 What This Tool Does

- Accepts a service ticket entered by a user
- Validates required fields (name, address, issue)
- Builds a structured job record
- Outputs a clean, human-readable service summary
- Mimics real technician or service-desk automation workflows

---

## ▶️ How to Run

From the project root directory:

```bash
cd src
python3 main.py

## 📌 Example Output

Below is an example of the program running successfully and generating a completed service summary:


Enter service ticket (name, address, issue): John, 567 D St, Low Light

JOB SUMMARY
-------------------------
Time Completed : 2026-01-15T11:34:30
Customer : John
Address : 567 D St
Issue : Low Light
Status : Completed

## ✅ Skills Demonstrated

- Modular Python architecture and functional design
- Defensive input validation and structured error handling
- Structured CLI workflow design
- Operational console reporting and formatted output
- Git version control and professional GitHub workflow
