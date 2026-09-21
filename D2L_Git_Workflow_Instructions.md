# AIDA 1141 — GitHub and D2L Workflow

## Purpose

Use this workflow to obtain an AIDA 1141 lab, complete it in your own private repository, push your work to GitHub, and submit the required evidence through D2L.

You will use two repositories:

1. The instructor source repository provides lab briefs, datasets, starter files, rubrics, and examples.
2. Your private AIDA 1141 repository is where you complete and save your own work.

Do not push your work to an instructor source repository.

## Repository links

### Practical lab examples

[AIDA 1141 Practical Lab Examples](https://github.com/stem-ai-studio-classroom/AIDA_1141_Practical_Lab_Examples)

Practice Lab 1 is located at:

~~~text
week-04/campus-bookstore-worked-lab/
~~~

### Graded labs

[AIDA 1141 Graded Labs](https://github.com/stem-ai-studio-classroom/AIDA_1141_Graded_Labs)

### Your private repository

Use the private repository assigned to you in the `stem-ai-studio-classroom` organization. It will look similar to:

~~~text
AIDA_1141_YourName
~~~

## Step 1 — Open your private repository

If you have not cloned it yet:

1. Open your private repository on GitHub.
2. Select **Code** and copy the HTTPS URL.
3. In VS Code, open the Command Palette with `Ctrl+Shift+P`.
4. Select **Git: Clone**.
5. Paste the URL and choose a local folder.
6. Open the cloned folder in VS Code.

If you already cloned it, open that existing folder. Do not create a new repository for each lab.

## Step 2 — Get the lab files

Open the instructor source repository and select **Code → Download ZIP**, or clone/pull the source repository.

Copy the complete lab folder into your private AIDA 1141 repository. For Practice Lab 1, copy:

~~~text
week-04/campus-bookstore-worked-lab/
~~~

The course source repository is where the instructor distributes files. Your private repository is where you complete and submit your work.

## Step 3 — Create the Python environment

Open a VS Code terminal inside the lab folder and run:

~~~powershell
py -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
py -m pip install -r requirements.txt
~~~

If PowerShell does not allow activation, run the environment directly:

~~~powershell
.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt
.\\.venv\\Scripts\\python.exe analysis.py
~~~

## Step 4 — Run the analysis

~~~powershell
py analysis.py
~~~

The script loads the CSV from `data` and creates outputs in `outputs`. Confirm that the charts and summary tables appear. Read the results and complete the business explanation required by the lab.

## Step 5 — Check and commit your work

From the root of your private repository, run:

~~~powershell
git status
git add .
git commit -m "Complete Practice Lab 1 bookstore demand analysis"
~~~

Use the commit message specified by the lab if one is provided.

## Step 6 — Push to your private repository

~~~powershell
git push
~~~

Open your private GitHub repository and refresh the page. Confirm that your lab folder, code, data, outputs, and documentation are visible.

## Step 7 — Submit through D2L

GitHub is the working and version-history location. D2L is the official course submission location.

Unless the lab says otherwise, submit:

1. the URL of your private AIDA 1141 repository;
2. any required ZIP, PDF, image, or decision note;
3. a short confirmation that your code runs successfully.

For a non-graded practice lab, the instructor may only require the GitHub push. Follow that week's D2L instructions.

## Important rules

- Do not push to instructor source repositories.
- Do not create a new private repository for every lab.
- Do not use another student's repository.
- Do not commit passwords, API keys, database credentials, or personal information.
- Keep all course work in your assigned private AIDA 1141 repository.
- Practice labs and graded labs are standalone, outcome-aligned weekly work.

If something goes wrong, send the instructor your private repository URL, the command you ran, the full error message, and a screenshot of the relevant VS Code or GitHub page. Never send passwords or access tokens.
