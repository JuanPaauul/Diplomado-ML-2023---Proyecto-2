# Diplomado-ML-2023---Proyecto-2
# Water Potability Prediction

## Overview

This project aims to create a machine learning model to predict whether a water sample is potable or not. The project utilizes Azure ML Pipelines to streamline the development and deployment process.

## Key Components

- **Jupyter Notebooks**: Contains the main experimentation and development work. Notable notebooks include:
  - `clean-data.ipynb`: Data cleaning and preprocessing.
  - `train-model.ipynb`: Model training and evaluation.
  - `eval-model.ipynb`: Making predictions using the trained model.

- **Azure ML Pipelines**: Streamlines the end-to-end workflow with key components, including:
  - Data Preparation/Cleaning
  - Data Splitting
  - Model Training
  - Model Scoring (Score)
  - Model Evaluation (Evaluate)

- **YAML Configuration Files**: Define the pipeline components and their dependencies.

## Execution Steps

1. **Data Preparation/cleaning**:
   - Run `clean-data.ipynb` to clean and preprocess the dataset.

2. **Model Training**:
   - Execute `train-model.ipynb` to train and evaluate the machine learning model.

3. **Azure ML Pipeline**:
   - Create and run an Azure ML Pipeline to automate the workflow using the defined YAML configuration files. The pipeline includes components for data preparation, splitting, training, scoring, and evaluation.

4. **Score Component**:
   - The "Score" component is responsible for scoring new data using the trained model. Ensure it is properly configured in your pipeline.

5. **Evaluate Component**:
   - The "Evaluate" component calculates relevant metrics for model performance. Verify the "Evaluate" component in your pipeline and its YAML configuration.

6. **Deployment** (if applicable):
   - Deploy the model in a production environment using Azure ML services or other suitable platforms.

## Dataset

The dataset used for this project is available on Kaggle: [Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability).

For more detailed information and code examples, refer to the Jupyter notebooks and Azure ML Pipeline configurations.

