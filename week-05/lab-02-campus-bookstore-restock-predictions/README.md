# AIDA 1141 Week 5 — Graded Lab 2: Campus Bookstore Restock Predictions

- **Assessment:** Graded Lab 2
- **Total value:** 5% of the course grade
- **Submission:** One completed lab folder, one private-repository push, and one D2L submission
- **Tools:** VS Code, Python 3.10 or later, pandas, and scikit-learn

## Read this first

This is the **one graded lab for Week 5**. It has two parts in the same folder:

- **Guided supervised-learning challenge — 3%**
- **Independent production extension — 2%**

Complete both parts in this folder. They are marking components of **one Lab 2**, not two assignments. Push this completed folder to your own private AIDA 1141 repository and submit **one link** to that repository in D2L. Do not push work to the instructor's `AIDA_1141_Graded_Labs` repository.

The supplied data are fictional and contain no personal information. The models are introductory examples, not tools for making real inventory decisions.

## What you will do

You work as a junior analyst helping a fictional campus bookstore plan inventory. You will:

1. use labelled past product records to make a **classification** model that predicts whether a product should be reordered;
2. make a **regression** model that predicts a numeric suggested order quantity;
3. create two prediction files; and
4. write a short note explaining what the predictions mean and one limitation.

## Files supplied

- `data/bookstore_history.csv` — past weekly product records with known answers;
- `data/new_products.csv` — two products for which the answers are not provided;
- `starter_analysis.py` — starter code with clearly marked TODO steps;
- `requirements.txt` — Python packages required for the lab;
- `decision_note.md` — template to complete;
- `RUBRIC.md` — exactly what will be assessed and the mark allocation.

## Part 1 — Guided classification challenge (3%)

### Business question

> Based on the supplied product information, should the bookstore consider reordering each new product now?

The answer is a category (`Yes` or `No`), so this is **classification**.

### Step 1 — Get the starter into your own repository

1. Sign in to GitHub with the account you use for AIDA 1141. Make sure you accepted the invitation to the private course repositories.
2. On your computer, create a folder named `AIDA-work`.
3. Open VS Code. Choose **File → Open Folder** and select `AIDA-work`.
4. Choose **Terminal → New Terminal** in VS Code.
5. In GitHub, open `AIDA_1141_Graded_Labs`. Click the green **Code** button and copy the **HTTPS** link.
6. In the VS Code terminal, type `git clone ` (include a space), paste the link, and press **Enter**. The command will look like this; use the link you copied:

   ```bash
   git clone https://github.com/stem-ai-studio-classroom/AIDA_1141_Graded_Labs.git
   ```

7. In GitHub, open your own private AIDA 1141 student repository. Click **Code**, choose **HTTPS**, and copy its link.
8. In the terminal, type `git clone `, paste your own repository link, and press **Enter**. Do not type angle-bracket placeholders; paste the actual link.
9. In the VS Code Explorer, open the cloned `AIDA_1141_Graded_Labs` folder, then `week-05`. Copy the complete folder named `lab-02-campus-bookstore-restock-predictions`.
10. In the Explorer, open your cloned private student repository. Create a folder named `week-05` inside it if one is not already there. Paste the lab folder into that `week-05` folder.
11. In VS Code choose **File → Open Folder** and select the copied `lab-02-campus-bookstore-restock-predictions` folder inside your student repository. Check the path in VS Code: it must be under your student repository, not under `AIDA_1141_Graded_Labs`.
12. Choose **Terminal → New Terminal**. The prompt should end with `lab-02-campus-bookstore-restock-predictions`.

### Step 2 — Set up Python

In the VS Code terminal, check Python:

**Windows:**

```powershell
py --version
```

**macOS:**

```bash
python3 --version
```

You need Python 3.10 or later. Create a project environment:

**Windows:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

**macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

The terminal prompt normally shows `(.venv)` after activation. If Windows blocks activation, run this in the same PowerShell terminal, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Step 3 — Inspect the data before writing code

In VS Code's Explorer, open `data/bookstore_history.csv` and `data/new_products.csv`. The columns mean:

| Column | Meaning |
|---|---|
| `product_id` | Fictional product code; used to identify a row, not as a prediction feature. |
| `units_sold_last_week` | Number sold during the previous week. |
| `stock_on_hand` | Number currently in stock. |
| `days_until_delivery` | Estimated days until the next regular delivery. |
| `reorder_now` | Known past outcome (`Yes` or `No`); the classification label. |
| `recommended_order_units` | Known past suggested quantity; the regression label. |

For classification, use these three numeric **features** (inputs): `units_sold_last_week`, `stock_on_hand`, and `days_until_delivery`. Its **label** (answer to predict) is `reorder_now`.

For the first, simpler regression model, use only `units_sold_last_week` as its numeric feature. Its **label** is `recommended_order_units`.
- Do not include either label among the features. The new-products file intentionally has no label columns because those are the unknown answers to predict.

### Step 4 — Complete the classification TODOs

1. In VS Code's Explorer, click `starter_analysis.py` to open it.
2. Find the section marked `GUIDED PART A — CLASSIFICATION (3%)`.
3. Complete **TODO 1** by selecting the three feature columns from `history` and storing them in `X_class`.
4. Complete **TODO 2** by selecting `reorder_now` from `history` and storing it in `y_class`.
5. Read the provided model setup. It creates a small `DecisionTreeClassifier`; a decision tree learns a sequence of simple questions from the examples.
6. Complete **TODO 3** by training the classifier with `X_class` and `y_class` using `.fit(...)`.
7. Complete **TODO 4** by using `.predict(...)` on the same feature columns from `new_products`.
8. Save the file with **Ctrl+S** (Windows) or **Command+S** (macOS).
9. In the terminal, run the script:

   **Windows:** `py starter_analysis.py`

   **macOS:** `python3 starter_analysis.py`

10. Check the terminal message and open `outputs/classification_predictions.csv`. It should contain one row for each new product and a predicted `Yes` or `No` category. The script stops after this file if you have not yet completed the regression TODOs; that is expected at this stage.

### Step 5 — Explain the classification result

In `decision_note.md`, complete the **Part A** prompts. State:

- which columns were features and which column was the label;
- what category the model predicted for each new product; and
- why the prediction should be treated as a suggestion for staff to review, not an automatic order.

Do not claim that a predicted `Yes` proves an item will run out. The model only learned from the supplied examples.

## Part 2 — Independent regression extension (2%)

### Business question

> What number of units might the bookstore consider ordering for each new product?

The answer is a number, so this is **regression**. You must complete this part independently using the same supplied files and the TODO prompts. You may refer to the Week 5 lecture notes and worked Practice Lab 2, but do not copy a completed graded solution from another person.

### Step 6 — Complete the regression TODOs

1. In `starter_analysis.py`, find `INDEPENDENT PART B — REGRESSION (2%)`.
2. Complete **TODO 5** by selecting `units_sold_last_week` from `history` and storing it in `X_regression`. Use this one feature to keep the first regression model straightforward.
3. Complete **TODO 6** by selecting `recommended_order_units` from `history` and storing it in `y_regression`.
4. Complete **TODO 7** by training the provided `LinearRegression` model with `.fit(...)`.
5. Complete **TODO 8** by using `.predict(...)` on the `units_sold_last_week` column from `new_products`.
6. Save the script with **Ctrl+S** or **Command+S**.
7. Run it again in the terminal using `py starter_analysis.py` (Windows) or `python3 starter_analysis.py` (macOS).
8. Open `outputs/regression_predictions.csv`. It should contain one numeric estimate for each new product. The program rounds predictions to one decimal place for readability.

### Step 7 — Finish your decision note

Complete the **Part B** prompts in `decision_note.md`. Your note must:

- report the numeric regression estimates from your output file;
- explain one useful thing the estimates suggest;
- name one limitation of these small fictional examples; and
- recommend one reasonable next step for bookstore staff before placing an order.

The model's numeric output is an estimate. Do not claim it is the correct order quantity.

## Step 8 — Check that your work is complete

Before submitting, confirm that your one Lab 2 folder contains:

- your completed `starter_analysis.py`;
- the supplied `data` files (do not alter the original data);
- `outputs/classification_predictions.csv`;
- `outputs/regression_predictions.csv`;
- your completed `decision_note.md`;
- `requirements.txt` and this `README.md`.

Run the script one last time. Read the terminal output and open both output CSV files. Make sure the predictions have not been left blank and your note agrees with your output.

## Step 9 — Commit and push from your private student repository

The copied lab folder must still be inside your **own** private student repository. In the VS Code terminal, run:

```bash
git status
git add week-05/lab-02-campus-bookstore-restock-predictions
git commit -m "Complete AIDA 1141 Lab 2"
git push
```

If your terminal is already inside the lab folder, use `git add .` instead of the longer `git add` path. If Git says there is nothing to commit, confirm that you saved your files and are in your own student repository. Never push to the instructor Graded Labs repository.

## Step 10 — Submit once in D2L

1. Open your private student repository on GitHub and confirm the completed `week-05/lab-02-campus-bookstore-restock-predictions` folder is visible.
2. Copy the link to your **private student repository**.
3. Submit that repository link in the Week 5 Lab 2 D2L submission area **once**.

Do not make separate submissions for the guided classification and independent regression parts. They are both included in this single Lab 2 folder and one submission.

See `RUBRIC.md` for the marking breakdown. Check D2L for the official due date.
