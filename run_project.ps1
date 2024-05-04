# Master script to set up, train, and run the Prices Predictor System UI on Windows (PowerShell)

# Function to print messages
function Print-Message {
    param (
        [string]$Message,
        [string]$Color = "Green"
    )
    Write-Host $Message -ForegroundColor $Color
}

Print-Message "Starting Prices Predictor System Setup & Run..."

# 1. Virtual Environment Setup
if (-not (Test-Path ".\venv")) {
    Print-Message "Creating Python virtual environment..."
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Print-Message "Failed to create virtual environment. Please check your Python installation." -Color Red
        exit 1
    }
}

Print-Message "Activating virtual environment..."
try {
    .\venv\Scripts\Activate.ps1
} catch {
    Print-Message "Activation might require setting execution policy. If script fails, try:" -Color Yellow
    Print-Message "   Set-ExecutionPolicy Unrestricted -Scope Process" -Color Yellow
    Print-Message "Then re-run this script." -Color Yellow
    # Attempting to proceed, pip install might still work if venv python is called directly
}

# 2. Install Dependencies
Print-Message "Installing dependencies from requirements.txt..."
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Print-Message "Failed to install dependencies. Please check requirements.txt and your internet connection." -Color Red
    exit 1
}

# 3. ZenML Configuration
Print-Message "Configuring ZenML Stack (errors for existing components/stack are okay)..."
zenml init # Idempotent
zenml integration install mlflow -y

# Try to register components, ignore errors if they already exist
zenml experiment-tracker register mlflow_tracker --flavor=mlflow 2>&1 | Out-Null
zenml model-deployer register mlflow_deployer --flavor=mlflow 2>&1 | Out-Null

# Try to register and set stack, ignore errors if already exists/set
zenml stack register local_mlflow_stack -o default -a default -e mlflow_tracker -d mlflow_deployer 2>&1 | Out-Null
zenml stack set local_mlflow_stack 2>&1 | Out-Null
Print-Message "ZenML Stack configured."

# 4. Run ML Training Pipeline
Print-Message "Training the ML model (running run_pipeline.py)..."
python run_pipeline.py
if ($LASTEXITCODE -ne 0) {
    Print-Message "Failed to run the training pipeline. Check the errors above." -Color Red
    exit 1
}
Print-Message "ML Model training complete!"

# 5. Start the Flask Web UI
Print-Message "Launching the Flask Web UI for predictions..."
Print-Message "Access the UI at http://127.0.0.1:5001" -Color Cyan
Print-Message "Press CTRL+C in this terminal to stop the UI." -Color Yellow

# Start Flask app. It will take over this terminal.
python ui/app.py
