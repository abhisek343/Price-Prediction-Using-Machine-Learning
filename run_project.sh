#!/bin/bash

# Master script to set up, train, and run the Prices Predictor System UI on macOS/Linux

# Function to print messages with color
print_message() {
    COLOR_GREEN="\033[0;32m"
    COLOR_YELLOW="\033[0;33m"
    COLOR_RED="\033[0;31m"
    COLOR_CYAN="\033[0;36m"
    COLOR_NC="\033[0m" # No Color

    MESSAGE=$1
    COLOR_CODE=$2

    case $COLOR_CODE in
        "green") echo -e "${COLOR_GREEN}${MESSAGE}${COLOR_NC}" ;;
        "yellow") echo -e "${COLOR_YELLOW}${MESSAGE}${COLOR_NC}" ;;
        "red") echo -e "${COLOR_RED}${MESSAGE}${COLOR_NC}" ;;
        "cyan") echo -e "${COLOR_CYAN}${MESSAGE}${COLOR_NC}" ;;
        *) echo -e "${MESSAGE}" ;;
    esac
}

print_message "🚀 Starting Prices Predictor System Setup & Run..." "green"

# 1. Virtual Environment Setup
if [ ! -d "./venv" ]; then
    print_message "🐍 Creating Python virtual environment..." "green"
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        print_message "❌ Failed to create virtual environment. Please check your Python 3 installation." "red"
        exit 1
    fi
fi

print_message "激活虚拟环境 (Activating virtual environment)..." "green"
source ./venv/bin/activate
if [ $? -ne 0 ]; then
    print_message "❌ Failed to activate virtual environment." "red"
    exit 1
fi

# 2. Install Dependencies
print_message "📦 Installing dependencies from requirements.txt..." "green"
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    print_message "❌ Failed to install dependencies. Please check requirements.txt and your internet connection." "red"
    exit 1
fi

# 3. ZenML Configuration
print_message "🔧 Configuring ZenML Stack (errors for existing components/stack are okay)..." "green"
zenml init # Idempotent
zenml integration install mlflow -y

# Try to register components, suppress stderr for "already exists" errors
zenml experiment-tracker register mlflow_tracker --flavor=mlflow &>/dev/null
zenml model-deployer register mlflow_deployer --flavor=mlflow &>/dev/null

# Try to register and set stack, suppress stderr
zenml stack register local_mlflow_stack -o default -a default -e mlflow_tracker -d mlflow_deployer &>/dev/null
zenml stack set local_mlflow_stack &>/dev/null
print_message "✅ ZenML Stack configured." "green"

# 4. Run ML Training Pipeline
print_message "🧠 Training the ML model (running run_pipeline.py)..." "green"
python run_pipeline.py
if [ $? -ne 0 ]; then
    print_message "❌ Failed to run the training pipeline. Check the errors above." "red"
    exit 1
fi
print_message "✅ ML Model training complete!" "green"

# 5. Start the Flask Web UI
print_message "🌐 Launching the Flask Web UI for predictions..." "green"
print_message "👉 Access the UI at http://127.0.0.1:5001" "cyan"
print_message "ℹ️  Press CTRL+C in this terminal to stop the UI." "yellow"

# Start Flask app. It will take over this terminal.
python ui/app.py

print_message "👋 Flask UI process ended." "green"
