import pandas as pd
import numpy as np
import argparse
from sklearn.metrics import accuracy_score, roc_auc_score


def benchmark(predictions_csv, targets_csv):
    
    predictions = pd.read_csv(predictions_file)['prediction']
    targets = pd.read_csv(targets_csv)['target']
    
    
    acc = accuracy_score(targets, np.where(predictions>.5, 1, 0))
    auc = roc_auc_score(targets, predictions)

    return {
        'accuracy': acc,
        'AUC': auc
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions', default='predictions.csv')
    parser.add_argument('--targets', default='targets.csv')
    args = parser.parse_args()
    print('Benchmarks: ', benchmark(args.predictions, args.targets))