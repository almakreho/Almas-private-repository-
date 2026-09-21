# Graded Lab 1 — Utility-Consumption Anomaly Review

## Week 4 graded lab

**Course:** AIDA 1141 — Introduction to Machine Learning and Data Science  
**Business context:** Apex Facilities Platform  
**Assessment:** LAB03, Part A/B  
**Value:** Use the approved course weighting in D2L.

## Business case

You are a junior data analyst supporting an Apex Facilities operations manager. The manager is responsible for occupied campus buildings and has noticed that some weekly utility readings appear higher than expected.

The manager needs an initial, decision-ready review of fictional utility data:

- Which buildings show the largest energy variance from baseline?
- Are any weeks unusual enough to investigate?
- Is the pattern consistent across buildings or isolated to one building?
- What should facilities staff check next?

The manager is not asking for a production application or a database system. They need a reproducible exploratory analysis that clearly connects the data, the method, the evidence, and the recommended next action.

## Data

Use:

~~~text
data/apex_utility_weekly.csv
~~~

All records are fictional. The file contains weekly readings for occupied buildings.

Important fields:

- `building` — building identifier;
- `week_start` — start date of the reporting week;
- `occupied_hours` — recorded occupied hours;
- `energy_kwh` — measured weekly energy consumption;
- `baseline_kwh` — expected weekly energy consumption for comparison;
- `comfort_incidents` — number of recorded comfort-related incidents;
- `maintenance_ticket` — whether a maintenance ticket was opened.

## Required method

You must:

1. load the CSV with pandas;
2. convert `week_start` to a date type;
3. check missing values and duplicate building/week records;
4. calculate:
   - `variance_kwh = energy_kwh - baseline_kwh`;
   - `variance_pct = variance_kwh / baseline_kwh * 100`;
5. summarize results by building;
6. compare weekly results;
7. define and state a transparent anomaly rule;
8. create at least two labelled visualizations;
9. explain what a facilities decision-maker should do next.

A suitable starting rule is:

~~~text
Flag a record when variance_pct is at least 20%,
or when variance_pct is at least 10% and comfort_incidents is 2 or more.
~~~

You may refine the rule, but you must explain the threshold and trade-off.

## Deliverables

### Deliverable 1 — Reproducible analysis

Submit a Python script or notebook that:

- loads the supplied dataset;
- performs the quality checks;
- creates the calculated fields;
- produces the required summaries;
- flags anomalies;
- saves the tables and charts.

### Deliverable 2 — Evidence tables

Provide:

1. a building summary with total energy, total baseline, average variance percentage, and anomaly count;
2. a weekly summary with energy, baseline, variance percentage, and anomaly count;
3. an anomaly review table containing the flagged records and the rule result.

### Deliverable 3 — Visual evidence

Provide at least two charts:

1. measured energy compared with baseline by week;
2. average variance percentage by building.

Every chart must have:

- a meaningful title;
- labelled axes;
- a readable legend where required;
- a short interpretation.

### Deliverable 4 — Decision note

Write a short note for the facilities operations manager containing:

- the most important finding;
- the building or week requiring first review;
- one recommended next action;
- one limitation;
- one next validation step.

Do not claim that an anomaly proves equipment failure. An anomaly identifies a record or pattern for human review.

### Deliverable 5 — Reproducibility and Git

Your private AIDA 1141 repository must contain:

~~~text
lab03-utility-anomaly/
├── data/
├── outputs/
├── analysis.py or notebook
├── requirements.txt
├── decision_note.md
└── README.md
~~~

Commit and push your work to your private AIDA 1141 repository:

~~~powershell
git add .
git commit -m "Complete LAB03 utility anomaly review"
git push
~~~

Submit the private repository URL and any required export through D2L.

## Student starter

Use `starter_analysis.py` as a starting point, or create your own notebook. You are responsible for completing the analysis and documenting your reasoning.

## Submission quality standard

Another analyst should be able to clone your private repository, install the requirements, run the analysis, inspect the outputs, and understand your recommendation.

Your work must identify:

- the decision owner;
- the decision or action being supported;
- the unit of analysis;
- the anomaly rule;
- the limitation;
- the next validation step.

This lab is within the approved Apex Facilities course context. The simplified CSV workflow is intentional: it lets you demonstrate Week 4 exploratory analysis and visualization without building the larger platform.
