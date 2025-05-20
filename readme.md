# 🏡✨ Prices Predictor System: Your Journey to AI-Powered House Valuations! ✨🏡

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

---

🚀 **Welcome Aboard, Future Price Prediction Pro!** 🚀

Ever wondered how house prices are determined? Dive into the world of machine learning with the **Prices Predictor System**! This isn't just another project; it's an end-to-end adventure that takes you from raw data to a working prediction model, complete with a snazzy web UI to play with. We're using the famous Ames Housing dataset to predict those tricky house prices, all while showcasing a production-ready MLOps workflow with ZenML and MLflow. Let's get those AI gears turning!

---

## 📜 Table of Awesome Contents

1.  [What's This All About? 🤔 (Project Overview)](#whats-this-all-about---project-overview)
2.  [Supercharged Features! ⚡](#supercharged-features-)
3.  [The Magic Ingredients 🧙‍♂️ (Technology Stack)](#the-magic-ingredients---technology-stack)
4.  [Let's Get This Party Started! 🎉 (Getting Started)](#lets-get-this-party-started---getting-started)
    *   [Your Pre-Flight Checklist 📋](#your-pre-flight-checklist-)
    *   [Installation & Blast-Off Sequence 🚀](#installation--blast-off-sequence-)
    *   [ZenML: Your MLOps Command Center 🌌](#zenml-your-mlops-command-center-)
5.  [Show Me The Action! 🎬 (Running the Project)](#show-me-the-action---running-the-project)
    *   [🌟 **Option 1: The "One-Click" Wonder Scripts!** 🌟](#-option-1-the-one-click-wonder-scripts--)
    *   [Step-by-Step Manual Adventure (If you prefer the scenic route!)](#step-by-step-manual-adventure-if-you-prefer-the-scenic-route)
        *   [Train Your AI Brain 🧠 (ML Pipeline)](#train-your-ai-brain--ml-pipeline)
        *   [Predict Like a Pro! 🔮](#predict-like-a-pro-)
        *   [Deploy Your Creation ☁️ (Optional Service Deployment)](#deploy-your-creation--optional-service-deployment)
    *   [Peek Behind the Curtain 📊 (Dashboards)](#peek-behind-the-curtain--dashboards)
6.  [The Blueprint 🗺️ (Project Structure)](#the-blueprint--project-structure)
7.  [Our Treasure Chest 💰 (Dataset)](#our-treasure-chest--dataset)
8.  [Secret Spells & Blueprints 🧩 (Design Patterns)](#secret-spells--blueprints--design-patterns)
9.  [Join the Quest! 🙏 (Contributing)](#join-the-quest---contributing)
10. [The Fine Print 📜 (License)](#the-fine-print--license)
11. [System Design Deep Dive 🧠📐](#system-design-deep-dive--)
    *   [Technology Stack Overview 🛠️💻🐍](./system_design/05_technology_stack.md)
12. [Got Questions? 📧 (Contact)](#got-questions---contact)

---

## What's This All About? 🤔 (Project Overview)

This system isn't just code; it's a demonstration of a complete machine learning journey:

*   💧 **Data Wrangling**: We'll grab the Ames Housing dataset and whip it into shape.
*   🤖 **AI Training Camp**: Using ZenML, we'll build a pipeline that preprocesses data, trains a smart regression model, and checks its homework (evaluation).
*   📈 **Track Everything**: With MLflow, every experiment, parameter, and metric is logged. No more "Wait, which model was that again?" moments!
*   🔮 **Prediction Power**: Get house price predictions through a handy command-line script OR a cool, interactive web UI you can show off!
*   ☁️ **To the Cloud (Conceptually)**: We've got the steps for deploying your model as a service, though local mileage may vary by OS.

*(For visual diagrams of the architecture, data flow, and more, please see the [System Design Deep Dive](#system-design-deep-dive--) section and the linked documents within.)*

---

## Supercharged Features! ⚡

*   **Smart Data Ingestion**: Smoothly loads data from a ZIP file.
*   **Deep Dive EDA**: A Jupyter notebook (`analysis/EDA.ipynb`) to explore the dataset's secrets.
*   **Pro Preprocessing**:
    *   Vanishes missing values like a magician!
    *   Spots and handles outliers.
    *   Transforms features with logs, scales them (MinMax, Standard), and turns categories into numbers (One-Hot Encoding).
*   **ZenML Magic Pipelines**:
    *   Automated training for perfect reruns every time.
    *   MLflow integration for A+ experiment tracking.
*   **Model Mastery**: Trains a Linear Regression model (but you can swap in your own champion!).
*   **Crystal Ball Predictions**:
    *   Quick checks with a command-line script.
    *   Fun, interactive predictions with a Flask web UI.
*   **Deployment Ready (Almost!)**: Shows how to deploy with MLflow.
*   **Neat & Tidy Code**: Organized with design patterns for easy understanding and expansion.
*   **Quality Checks**: Basic unit tests to keep things running smoothly.

---

## The Magic Ingredients 🧙‍♂️ (Technology Stack)

*   🐍 **Python 3.x**: The serpent that powers our magic.
*   ✨ **ZenML**: Our MLOps spellbook for orchestrating pipelines.
*   📊 **MLflow**: The crystal ball for tracking experiments and serving models.
*   🤖 **Scikit-learn**: The arsenal of machine learning spells and tools.
*   🐼 **Pandas**: For taming and shaping our data.
*   🔢 **NumPy**: For all the number-crunching.
*   🌐 **Flask**: To build our interactive web UI.
*   🎨 **Matplotlib & Seaborn**: For painting beautiful data pictures in EDA.
*   🖱️ **Click**: For crafting user-friendly command-line tools.

---

## Let's Get This Party Started! 🎉 (Getting Started)

Time to roll up your sleeves and bring this project to life!

### Your Pre-Flight Checklist 📋

*   ✅ Python 3.x installed? (Check with `python --version` or `python3 --version`)
*   ✅ Pip ready to fetch packages? (Usually included with Python)
*   ✅ Git installed for code-cloning action?

### Installation & Blast-Off Sequence 🚀

1.  **Clone Your Spaceship (The Repository):**
    ```bash
    git clone https://github.com/YOUR_USERNAME/Price-Prediction.git # ✏️ Replace YOUR_USERNAME!
    cd Price-Prediction
    ```

2.  **Build Your Personal Cockpit (Virtual Environment):**
    This keeps your project's tools separate and tidy.
    ```bash
    python -m venv venv  # Or python3
    ```
    Now, step inside (activate it!):
    *   **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1 
        # ⚠️ If you see a red error about execution policy, try this first:
        # Set-ExecutionPolicy Unrestricted -Scope Process
        # Then re-run: .\venv\Scripts\Activate.ps1
        ```
    *   **Windows (Command Prompt):**
        ```cmd
        venv\Scripts\activate.bat
        ```
    *   **macOS/Linux (bash/zsh):**
        ```bash
        source venv/bin/activate
        ```
    Your terminal prompt should now have a `(venv)` prefix – you're in!

3.  **Load Up the Essentials (Install Dependencies):**
    With `(venv)` active, let your computer grab all the necessary tools:
    ```bash
    pip install -r requirements.txt
    ```

### ZenML: Your MLOps Command Center 🌌

ZenML is our trusty mission control for MLOps. Let's get it set up!

1.  **Initialize ZenML in Your Project Base:**
    (Make sure you're in the `Price-Prediction` directory with `(venv)` active)
    ```bash
    zenml init
    ```
    This creates a hidden `.zen` folder where ZenML keeps its notes.

2.  **Assemble Your ZenML Super-Stack:**
    A "stack" tells ZenML what tools to use. We'll build one with MLflow.
    ```powershell
    # Install the MLflow integration for ZenML
    zenml integration install mlflow -y

    # Tell ZenML about our MLflow experiment tracker
    # (Don't worry if it says 'mlflow_tracker' already exists!)
    zenml experiment-tracker register mlflow_tracker --flavor=mlflow 

    # And our MLflow model deployer
    # (Again, "already exists" is fine!)
    zenml model-deployer register mlflow_deployer --flavor=mlflow

    # Now, create a new stack named 'local_mlflow_stack' using these components
    zenml stack register local_mlflow_stack -o default -a default -e mlflow_tracker -d mlflow_deployer

    # And make it our active stack!
    zenml stack set local_mlflow_stack
    ```
    🎉 **Woohoo!** Your ZenML command center is online and ready!

---

## Show Me The Action! 🎬 (Running the Project)

With setup complete, it's time for the main event! We've even created convenient master scripts to get you going quickly.

### 🌟 **Recommended: The "One-Click" Wonder Scripts!** 🌟

For the easiest and most streamlined experience, use these master scripts. They automate the main workflow: virtual environment checks, dependency installation, ZenML setup, model training, and launching the interactive Web UI.

*   **Windows Users (PowerShell):**
    Simply run the PowerShell script from the project root:
    ```powershell
    .\run_project.ps1
    ```
*   **macOS/Linux Users (bash/zsh):**
    First, make the script executable (you only need to do this once):
    ```bash
    chmod +x run_project.sh
    ```
    Then, run it:
    ```bash
    ./run_project.sh
    ```

**What these magic scripts do for you:**
1.  Checks for/helps with virtual environment activation (and creation if it's your first time).
2.  Installs all necessary Python packages.
3.  Configures the ZenML stack (it's safe to re-run; it won't break existing setups).
4.  Kicks off the `run_pipeline.py` script to train your AI model.
5.  Once training is complete, it launches the Flask Web UI, making it available at `http://127.0.0.1:5001` for you to make predictions!

> **Note:** The Flask Web UI will run in your terminal. To stop it, press `CTRL+C` in that terminal window.

### Alternative: Manual Step-by-Step Execution 🗺️

If you prefer a hands-on approach to understand each component or wish to run parts of the project individually (perhaps for debugging or deeper learning), this manual guide is for you! The master scripts above automate these steps, but doing them manually can be very insightful.

**(Remember to always have your virtual environment activated: `.\venv\Scripts\activate` on Windows or `source venv/bin/activate` on macOS/Linux for these commands.)**

#### 1. Train Your AI Brain 🧠 (ML Pipeline)

This is where the magic happens! We train our model using the ZenML pipeline.
```bash
python run_pipeline.py
```
*   **What's Cooking?** This script runs all the steps: data loading, cleaning, feature magic, model training, and evaluation. Everything gets logged to MLflow.
*   **Heads Up!** The script uses `data/archive.zip` (included). The MLflow logs will likely go to a ZenML-managed folder in your user's AppData (check the script output for the exact path to use with `mlflow ui`).

#### 2. Predict Like a Pro! 🔮

Once your AI brain is trained (either via the master script or manually), let's see its predictions!

*   **Option A: Quick Test with the Command-Line Script** 💻
    The `sample_predict.py` script loads your latest model and predicts on a built-in example. This is great for a quick check.
    ```bash
    python sample_predict.py
    ```
    This script is configured to:
    *   Connect to the correct MLflow tracking URI used by ZenML.
    *   Load the latest model version from the `ml_pipeline` experiment.
    *   Apply necessary data transformations (like `np.log1p` for `Gr Liv Area`) before prediction and inverse transformations (`np.expm1`) after, to give you the final price.

*   **Option B: Fun & Interactive with the Web UI** 🎈 (If not already started by the master script)
    If you didn't use the master script or stopped the UI, you can start it manually:
    1.  Ensure Flask is installed (it's in `requirements.txt`).
    2.  Launch the app (from the project root):
        ```bash
        python ui/app.py
        ```
    3.  Open your web browser and go to: **http://127.0.0.1:5001**
        Now you can input different house features and see live predictions!

#### 3. Deploy Your Creation ☁️ (Optional Service Deployment)

The `run_deployment.py` script attempts to deploy the trained model as an MLflow serving endpoint. This is more for demonstration of deployment capabilities.
```bash
python run_deployment.py
```
*   **Windows Users Note**: MLflow's local model serving as a persistent background service can be tricky on Windows when launched this way. The script might run, but the service may not stay active for long. For reliable local predictions, the Web UI (Option B) or `sample_predict.py` (Option A) are better choices.
*   **Stopping the Service**: If you did start one and want to stop it:
    ```bash
    python run_deployment.py --stop-service
    ```

### 4. Peek Behind the Curtain 📊 (Dashboards)

*   **MLflow UI - The Experiment Lab** 🔬:
    See all your training runs, compare metrics, and marvel at your model artifacts!
    Use the command from the `run_pipeline.py` output (it'll be something like this, **replace with YOUR actual path**):
    ```powershell
    # Example for Windows, check your run_pipeline.py output!
    mlflow ui --backend-store-uri "file:C:\Users\YOUR_USER_NAME\AppData\Roaming\zenml\local_stores\YOUR_ZENML_ARTIFACT_STORE_ID\mlruns"
    ```
    Then navigate your browser to **http://127.0.0.1:5000**.

*   **ZenML Dashboard - Mission Control Overview** 🛰️:
    Get a bird's-eye view of your ZenML pipelines, stacks, and runs.
    ```bash
    zenml up
    ```
    Then fly your browser to **http://127.0.0.1:8237**.

---

## The Blueprint 🗺️ (Project Structure)

Here's how our project is organized:
```
.
├── .zen/                   # ZenML's secret hideout 🤫
├── analysis/               # Where we explore data 🕵️‍♀️
│   ├── EDA.ipynb           # Our main investigation notebook
│   └── analyze_src/        # Helper scripts for analysis
├── data/                   # Raw ingredients 📦
│   └── archive.zip         # The Ames Housing dataset (zipped)
├── explanations/           # How the magic tricks work ✨ (Design Patterns)
├── extracted_data/         # Unpacked data, ready for cooking 🍳
├── mlruns/                 # MLflow's diary (can be elsewhere with ZenML) 📔
├── pipelines/              # ZenML's grand plans 📜
│   ├── deployment_pipeline.py
│   └── training_pipeline.py
├── src/                    # Core spell components (Python modules) 🧪
├── steps/                  # Individual steps in our ZenML pipelines 🚶‍♂️
├── system_design/          # 🧠📐 System Design Documents
│   ├── diagrams/           # 🖼️ Mermaid diagram source files
│   │   ├── 01_architecture_overview_diagram.md
│   │   ├── 02_data_flow_diagram.md
│   │   ├── 03_ml_pipeline_details_diagram.md
│   │   ├── 04a_local_prediction_script_diagram.md
│   │   └── 04b_flask_ui_workflow_diagram.md
│   ├── 01_architecture_overview.md
│   ├── 02_data_flow.md
│   ├── 03_ml_pipeline_details.md
│   ├── 04_prediction_services.md
│   └── 05_technology_stack.md
├── tests/                  # Keeping our spells bug-free 🐞
├── ui/                     # Our cool Flask Web UI 🖼️
│   ├── app.py              # The Flask brain
│   └── templates/
│       └── index.html      # The UI's pretty face
├── .DS_Store               # macOS ghost file 👻 (ignore)
├── config.yaml             # Project settings (currently shy)
├── readme.md               # You are here! 📍
├── requirements.txt        # List of magical tools needed 📜
├── run_deployment.py       # Script for the (optional) deployment show 🚀
├── run_pipeline.py         # Script to kick off model training 🚂
├── run_project.ps1         # One script to rule them all (Windows) 👑
├── run_project.sh          # One script to rule them all (macOS/Linux) 👑
└── sample_predict.py       # Quick prediction tester ⚡
```

---

## System Design Deep Dive 🧠📐

Want to understand the nuts and bolts of how this system works? We've prepared detailed design documents for you. Each document may contain embedded Mermaid diagrams or link to their source files in the `system_design/diagrams/` folder.

*   [**01: Architecture Overview**](./system_design/01_architecture_overview.md) 🏗️ - Get the big picture of all components and how they connect.
*   [**02: Data Flow Pipeline**](./system_design/02_data_flow.md) 💧 - Follow the data's journey from raw to ready-for-training.
*   [**03: ML Pipeline Details**](./system_design/03_ml_pipeline_details.md) ⚙️🔬 - A closer look at the ZenML training pipeline and MLflow integration.
*   [**04: Prediction Services & UI**](./system_design/04_prediction_services.md) 🔮💻 - How predictions are served via scripts and the web UI.
*   [**05: Technology Stack**](./system_design/05_technology_stack.md) 🛠️💻🐍 - The key technologies, libraries, and frameworks used.

**Viewing the Diagrams:** The individual system design documents linked above contain visual diagrams. The raw Mermaid code for these diagrams can also be found in the `system_design/diagrams/` folder. To view them as visual charts:
*   **In VS Code (Recommended):**
    1.  Open this `readme.md` file or any `.md` file in the `system_design/diagrams/` folder.
    2.  Open the Markdown Preview: Press `Ctrl+Shift+V` (or `Cmd+Shift+V` on macOS), or click the preview icon in the top-right of the editor.
    3.  **For the best experience and features (like icon support):** Install the **"Markdown Preview Mermaid Support"** extension from the VS Code Marketplace.
*   **Online:** Copy a Mermaid code block and paste it into the [Mermaid Live Editor](https://mermaid.live).

---
## Our Treasure Chest 💰 (Dataset)

We're using the famous **Ames Housing dataset**. It's packed in `data/archive.zip` and contains `AmesHousing.csv`. Our data ingestion step unpacks it for you into `extracted_data/`.
Want to see the data's soul? Check out `analysis/EDA.ipynb`.

---

## Secret Spells & Blueprints 🧩 (Design Patterns)

We've used some clever software design patterns to keep our code organized and powerful:

*   🧙 **Factory Pattern**: Like a magic hat that pulls out the right tool (e.g., data ingestor) when you need it, without you knowing all the nitty-gritty.
*   📜 **Strategy Pattern**: Lets you switch game plans (e.g., how to handle missing data or scale features) on the fly without rewriting everything.
*   🏛️ **Template Method Pattern**: Provides a basic recipe (template) for a task, but lets you customize specific ingredients (steps) later.

Dive into the `explanations/` folder for more on these cool concepts!

---

## Join the Quest! 🙏 (Contributing)

Got ideas? Found a bug? Want to add your own magic? Contributions are what make open-source awesome!

1.  **Fork the Project** (Create your own copy)
2.  **Create your Feature Branch** (`git checkout -b feature/MyAwesomeSpell`)
3.  **Commit your Changes** (`git commit -m 'Added MyAwesomeSpell'`)
4.  **Push to the Branch** (`git push origin feature/MyAwesomeSpell`)
5.  **Open a Pull Request** (Share your magic with us!)

Don't forget to give the project a star ⭐ if you like it!

---

## The Fine Print 📜 (License)

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for more details (if it exists, otherwise trust the badge!).

---

## Got Questions? 📧 (Contact)

(Your Name/Organization - Your Contact Information - Make this project truly yours!)

---

🎉 **Happy Predicting!** 🎉
