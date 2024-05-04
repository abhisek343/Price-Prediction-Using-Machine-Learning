```mermaid
graph LR
    A[Raw Data - AmesHousing.csv in archive.zip] --> B(DataIngestor);
    B --> C{Extracted DataFrame - Raw};
    C --> D(HandleMissingValuesStep);
    D --> E{DataFrame - Missing Values Handled};
    E --> F(FeatureEngineeringStep - LogTransform);
    F --> G{DataFrame - Log Transformed Features e.g., Gr Liv Area, SalePrice};
    G --> H(OutlierDetectionStep);
    H --> I{DataFrame - Outliers Handled};
    I --> J(DataSplitterStep);
    J --> K[X_train, y_train - Log Transformed SalePrice];
    J --> L[X_test, y_test - Log Transformed SalePrice];
    K --> M(ModelTraining);
    L --> N(ModelEvaluation);

    subgraph "ZenML Pipeline: Data Processing Stages"
        direction TB
        B; C; D; E; F; G; H; I; J;
    end
    
    style A fill:#fff2cc,stroke:#333,stroke-width:2px
    style K fill:#d9ead3,stroke:#333,stroke-width:2px
    style L fill:#fce5cd,stroke:#333,stroke-width:2px
    style M fill:#cfe2f3,stroke:#333,stroke-width:2px
    style N fill:#f4cccc,stroke:#333,stroke-width:2px
