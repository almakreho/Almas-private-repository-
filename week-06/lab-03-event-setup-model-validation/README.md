# AIDA 1141 Week 6 — Graded Lab 3: Train and Validate an Event Setup Model

- **Assessment:** Graded Lab 3
- **Total value:** 5% of the course grade
- **Submission:** One lab folder, one push to your private course repository, one D2L submission
- **Tools:** VS Code, Python 3.10+, pandas, and scikit-learn

## Read this first

This is **one graded lab worth 5%**. It has two marked parts in this same folder:

- **Part A — Guided in-class validation checkpoint: 3%**
- **Part B — Independent model extension: 2%**

These are components of one Lab 3, not two assignments. Keep both parts in this folder. Push the completed folder to your own private AIDA 1141 repository and submit **one repository link** in D2L. Do not push to the instructor's `AIDA_1141_Graded_Labs` repository.

The fictional data contain no personal information. This classroom model is not for scheduling real staff or making actual event commitments.

## Your task

A fictional campus events team wants to estimate how many **minutes** room setup may take. You will use past setup records to train and validate a simple regression model.

You will:

1. inspect the data and identify the features and numeric target;
2. keep some historical records aside for validation;
3. compare a simple average-value baseline with a linear regression model;
4. calculate and interpret mean absolute error (MAE) on the same validation records; and
5. independently test whether adding the number of equipment items improves validation MAE.

Do your own analysis. The supplied starter contains TODOs, not a completed solution. You may use class notes and Practice Lab 3 to understand the method, but use this lab's separate event-setup data and write your own results and explanations.

## Files supplied

- `data/event_setups.csv` — fictional historical room setups and known setup times;
- `starter_analysis.py` — starter program with clearly labeled TODOs;
- `requirements.txt` — packages to install;
- `decision_note.md` — prompts for your short interpretation;
- `RUBRIC.md` — marking criteria and exact allocation.

## Part A — Guided in-class checkpoint (3%)

### Business question

> Using the room area, can we estimate setup time for a similar event, and how large is the typical error on records held aside from training?

### Step 1 — Copy the starter into your own private repository

1. Sign in to GitHub with your AIDA 1141 account. Accept the course repository invitations if needed.
2. On your computer, create a folder named `AIDA-work`.
3. Open VS Code. Select **File → Open Folder** and choose `AIDA-work`.
4. Select **Terminal → New Terminal**. The command area appears at the bottom of VS Code.
5. In GitHub, open `AIDA_1141_Graded_Labs`. Select the green **Code** button, choose **HTTPS**, and copy the link.
6. In the VS Code terminal, type `git clone ` (include the space), paste the link, and press **Enter**. It will look like this:

   ```bash
   git clone https://github.com/stem-ai-studio-classroom/AIDA_1141_Graded_Labs.git
   ```

7. In GitHub, open your own private AIDA 1141 repository. Select **Code → HTTPS**, copy its link, then type `git clone ` in the terminal, paste the link, and press **Enter**. If you already cloned your student repository for another lab, do not clone it a second time.
8. In VS Code's Explorer (the file list on the left), open the downloaded `AIDA_1141_Graded_Labs` folder, then `week-06`.
9. Copy the entire folder named `lab-03-event-setup-model-validation`.
10. In the Explorer, open your own private student repository. Create a folder named `week-06` inside it if needed. Paste the copied lab folder inside `week-06`.
11. Select **File → Open Folder** and open the copied `lab-03-event-setup-model-validation` folder that is inside your private student repository. Check that the path is under your student repository, not under `AIDA_1141_Graded_Labs`.
12. Select **Terminal → New Terminal**. The terminal is now ready for commands in this lab folder.

### Step 2 — Set up Python

Check that Python 3.10 or later is installed.

**Windows:**

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

**macOS:**

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

After activation, the terminal prompt usually begins with `(.venv)`. If Windows blocks activation, run this in the same PowerShell terminal, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

This affects only the current terminal window. `requirements.txt` is a list of packages; the `pip install` command reads it and installs them.

### Step 3 — Read the data before coding

In VS Code's Explorer, click `data/event_setups.csv`. Each row is one fictional past event. The columns are:

| Column | Meaning | Use in the model |
|---|---|---|
| `event_id` | Made-up event identifier | Keep to identify a row; do not use as a feature |
| `room_area_sqm` | Room area in square metres | Part A feature; Part B feature |
| `equipment_items` | Number of equipment items to set up | Add this feature in Part B |
| `setup_minutes` | Recorded setup duration in minutes | Numeric target to estimate |

The **target** is `setup_minutes`: the number the model is asked to estimate. In Part A, use `room_area_sqm` as the feature. In Part B, use both `room_area_sqm` and `equipment_items`. Do not use `event_id` as a feature; it is only a label for the row.

### Step 4 — Complete the Part A TODOs

1. In the Explorer, open `starter_analysis.py`.
2. Find `PART A — GUIDED CHECKPOINT (3%)`.
3. Complete **TODO A1**: create `X_a` from the `room_area_sqm` column. Keep it as a table by using double square brackets, for example `history[["column_name"]]`.
4. Complete **TODO A2**: create `y` from the `setup_minutes` column.
5. Complete **TODO A3**: split `X_a` and `y` into training and validation groups. Use the starter's settings: 25% validation (`test_size=0.25`) and `random_state=42`. Keep all four results in the named variables shown in the starter code.
6. Complete **TODO A4**: train the `DummyRegressor` baseline on the training data only, then predict the validation rows.
7. Complete **TODO A5**: train the `LinearRegression` model on the same training rows, then predict the same validation rows.
8. Complete **TODO A6**: calculate MAE for each model by comparing its validation predictions with `y_valid`.
9. Complete **TODO A7**: fill in the results table and save it using the output path already provided in the starter.
10. Save the file (**Ctrl+S** on Windows or **Command+S** on macOS).

### Step 5 — Run Part A and save your in-class checkpoint

In the terminal, run:

**Windows:**

```powershell
py starter_analysis.py
```

**macOS:**

```bash
python3 starter_analysis.py
```

If the program says a Part A TODO is not complete, return to `starter_analysis.py` and check the numbered TODO. If you see `ModuleNotFoundError`, activate `.venv` and repeat the package-install command from Step 2. If you see `FileNotFoundError`, check that VS Code opened this lab folder and that `event_setups.csv` is inside `data`.

Your Part A run should create two files: `outputs/part_a_validation.csv` records the held-aside event IDs, known setup times, and both models' estimates; `outputs/part_a_model_comparison.csv` records both validation MAE scores. Open them in VS Code and confirm they contain rows and numbers. Keep both files when you complete Part B; they are your initial checkpoint evidence.

### Step 6 — Write the Part A checkpoint explanation

Open `decision_note.md` and complete the **Part A — in-class checkpoint** prompts. Use your own actual output. State which model had lower validation MAE, report both MAE values in minutes, and explain one reason the result should not be treated as a guarantee. Do not claim the model has been proven reliable for real events.

### Step 7 — Save the Part A checkpoint in Git

Before the in-class checkpoint ends, save the work in your private student repository. In the VS Code terminal, run:

```bash
git status
git add week-06/lab-03-event-setup-model-validation
git commit -m "AIDA 1141 Lab 3 Part A checkpoint"
git push
```

If your terminal is already inside the lab folder, use `git add .` instead. Your commit must be in your own private AIDA 1141 repository. Do not push to the instructor Graded Labs repository.

## Part B — Independent model extension (2%)

Complete Part B independently after the guided checkpoint. Continue in the **same Lab 3 folder** and the same student repository.

### Step 8 — Add a second feature and compare

1. Return to `starter_analysis.py` and find `PART B — INDEPENDENT EXTENSION (2%)`.
2. Complete **TODO B1**: make `X_b` contain both `room_area_sqm` and `equipment_items`.
3. Use the **same** training and validation row split from Part A. Do not create a new random split; this makes the comparison fair because both models are tested on the same held-aside events.
4. Complete **TODO B2**: train a second `LinearRegression` model using the Part B features and training rows.
5. Complete **TODO B3**: predict the held-aside rows and calculate its validation MAE in minutes.
6. Complete **TODO B4**: save `outputs/part_b_model_comparison.csv` with the Part A single-feature model MAE and the Part B two-feature model MAE.
7. Save `starter_analysis.py`, then run it again with `py starter_analysis.py` (Windows) or `python3 starter_analysis.py` (macOS).
8. Open the CSV files in `outputs`. Confirm that the prediction file has validation rows and that both comparison files contain model names and numeric MAE values.

### Step 9 — Finish the Part B decision note

Complete the **Part B — independent extension** prompts in `decision_note.md`. Based on your own comparison:

- say whether adding `equipment_items` lowered the validation MAE;
- report the change in MAE (Part A MAE minus Part B MAE; a negative change means Part B was worse);
- explain what the result suggests, without claiming it proves future accuracy; and
- give one sensible next check before anyone used this approach for real event planning.

If Part B did not improve the score, report that honestly. A result that does not improve is still a valid experiment when the steps and interpretation are correct.

## Final check — one folder, one push, one D2L submission

Before submitting, confirm this same Lab 3 folder contains:

- completed `starter_analysis.py`;
- the original, unchanged `data/event_setups.csv`;
- `outputs/part_a_validation.csv`;
- `outputs/part_a_model_comparison.csv`;
- `outputs/part_b_model_comparison.csv`;
- your completed `decision_note.md`;
- `README.md`, `RUBRIC.md`, and `requirements.txt`.

Run the program once more and check that all three output files are current and that your decision note agrees with the results. Then, from your private student repository, save and push your final work:

```bash
git status
git add week-06/lab-03-event-setup-model-validation
git commit -m "Complete AIDA 1141 Lab 3"
git push
```

If you already committed all final changes, Git may say there is nothing new to commit; in that case, run `git push` and continue.

To submit in D2L:

1. Open your private AIDA 1141 repository on GitHub and check that the completed Week 6 folder is visible.
2. Copy the link to your private student repository.
3. Submit that repository link in the **Week 6 Lab 3** D2L submission area once.

Submit **one link only** for the entire Lab 3. Part A and Part B are marked components within this single 5% lab, not separate submissions. Check D2L for the official due date.
