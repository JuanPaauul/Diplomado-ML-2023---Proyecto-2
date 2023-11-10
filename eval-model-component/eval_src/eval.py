
import argparse
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from pathlib import Path
import os

parser = argparse.ArgumentParser("evaluate")
parser.add_argument("--scoring_result", type=str, help="Path of scoring result")
parser.add_argument("--eval_output", type=str, help="Path of output evaluation result")
parser.add_argument("--target_column", type=str, help="name of target column)")
args = parser.parse_args()

scoring_result = pd.read_csv(args.scoring_result)

y_true = scoring_result[args.target_column]
y_pred = scoring_result[args.target_column]

accuracy = accuracy_score(y_true, y_pred)
confusion = confusion_matrix(y_true, y_pred)
report = classification_report(y_true, y_pred)


eval_msg = f"Accuracy: {accuracy:.2f}\n"
eval_msg += f"Confusion Matrix:\n{confusion}\n"
eval_msg += f"Classification Report:\n{report}"

with open(args.eval_output, 'w') as f:
    f.write(eval_msg)