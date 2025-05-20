```mermaid
graph TD
    A["Raw Data (archive.zip)"] --> B("Data Ingestion Step");
    B --> C("Preprocessing & FE Steps");
    C --> D("Model Training & Eval Step");
    D -- "Model & Metrics" --> E["MLflow Tracking Server"];
    E -- "Loads Model" --> F("Flask Web UI");
    E -- "Loads Model" --> G("Local Prediction Script");
    
    U["User via Browser"] --> F;
    F -- "Prediction Request" --> F;
    F -- "Displays Prediction" --> U;
    
    H["User via CLI"] --> G;
    G -- "Displays Prediction" --> H;

    I["ZenML CLI / Scripts"];
    %% Defined, but not linked yet to avoid error

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#lightgrey,stroke:#333,stroke-width:2px
    style F fill:#lightblue,stroke:#333,stroke-width:2px
    style G fill:#lightgreen,stroke:#333,stroke-width:2px
    style I fill:#orange,stroke:#333,stroke-width:2px
```
