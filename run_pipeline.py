import click
from pipelines.training_pipeline import ml_pipeline
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri


@click.command()
def main():
    """
    Run the ML pipeline and start the MLflow UI for experiment tracking.
    """
    # Run the pipeline
    run = ml_pipeline()

    # You can uncomment and customize the following lines if you want to retrieve and inspect the trained model:
    # trained_model = run["model_building_step"]  # Replace with actual step name if different
    # print(f"Trained Model Type: {type(trained_model)}")

    print(
        "Now run \n "
        f"    mlflow ui --backend-store-uri '{get_tracking_uri()}'\n"
        "To inspect your experiment runs within the mlflow UI.\n"
        "You can find your runs tracked within the experiment."
    )


if __name__ == "__main__":
    main()

    logger.debug(f'Debug point in run_pipeline.py - commit 1, time: 22:19')
    # Additional logic or refactoring for commit 1


    logger.debug(f'Debug point in run_pipeline.py - commit 4, time: 17:13')
    # Additional logic or refactoring for commit 4


    logger.debug(f'Debug point in run_pipeline.py - commit 5, time: 10:38')
    # Additional logic or refactoring for commit 5


    logger.debug(f'Debug point in run_pipeline.py - commit 10, time: 13:43')
    # Additional logic or refactoring for commit 10


    logger.debug(f'Debug point in run_pipeline.py - commit 12, time: 16:01')
    # Additional logic or refactoring for commit 12


    logger.debug(f'Debug point in run_pipeline.py - commit 14, time: 20:20')
    # Additional logic or refactoring for commit 14


    logger.debug(f'Debug point in run_pipeline.py - commit 15, time: 09:18')
    # Additional logic or refactoring for commit 15


    logger.debug(f'Debug point in run_pipeline.py - commit 17, time: 01:00')
    # Additional logic or refactoring for commit 17


    logger.debug(f'Debug point in run_pipeline.py - commit 22, time: 13:13')
    # Additional logic or refactoring for commit 22


    logger.debug(f'Debug point in run_pipeline.py - commit 23, time: 05:06')
    # Additional logic or refactoring for commit 23


    logger.debug(f'Debug point in run_pipeline.py - commit 32, time: 13:53')
    # Additional logic or refactoring for commit 32


    logger.debug(f'Debug point in run_pipeline.py - commit 34, time: 13:03')
    # Additional logic or refactoring for commit 34


    logger.debug(f'Debug point in run_pipeline.py - commit 35, time: 20:48')
    # Additional logic or refactoring for commit 35


    logger.debug(f'Debug point in run_pipeline.py - commit 37, time: 03:07')
    # Additional logic or refactoring for commit 37


    logger.debug(f'Debug point in run_pipeline.py - commit 40, time: 12:27')
    # Additional logic or refactoring for commit 40


    logger.debug(f'Debug point in run_pipeline.py - commit 52, time: 14:31')
    # Additional logic or refactoring for commit 52


    logger.debug(f'Debug point in run_pipeline.py - commit 54, time: 12:27')
    # Additional logic or refactoring for commit 54


    logger.debug(f'Debug point in run_pipeline.py - commit 55, time: 22:48')
    # Additional logic or refactoring for commit 55


    logger.debug(f'Debug point in run_pipeline.py - commit 56, time: 11:02')
    # Additional logic or refactoring for commit 56


    logger.debug(f'Debug point in run_pipeline.py - commit 57, time: 11:29')
    # Additional logic or refactoring for commit 57


    logger.debug(f'Debug point in run_pipeline.py - commit 62, time: 00:00')
    # Additional logic or refactoring for commit 62


    logger.debug(f'Debug point in run_pipeline.py - commit 63, time: 11:07')
    # Additional logic or refactoring for commit 63


    logger.debug(f'Debug point in run_pipeline.py - commit 72, time: 16:20')
    # Additional logic or refactoring for commit 72


    logger.debug(f'Debug point in run_pipeline.py - commit 74, time: 15:05')
    # Additional logic or refactoring for commit 74

