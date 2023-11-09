import argparse
import joblib  
import pandas as pd  
from pathlib import Path
import os

parser = argparse.ArgumentParser("score")
parser.add_argument("--model_input", type=str, help="Path of input model")
parser.add_argument("--test_data", type=str, help="Path to test data")
parser.add_argument("--score_output", type=str, help="Path of scoring output")
args = parser.parse_args()

model = joblib.load(Path(args.model_input) / 'decission_tree_modelo.pkl')

test_data = pd.read_csv(Path(args.test_data)/'test-data.csv')

X_test = test_data.drop(columns=['Potability'])  

y_pred = model.predict(X_test)

test_data['predictions'] = y_pred


test_data.to_csv(os.path.join(args.score_output, 'score_output.csv'), index=False)