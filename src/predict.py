import argparse, joblib
import pandas as pd
import extra_funcs

# set up argument parsing (make sure these match those in config.yml)
parser = argparse.ArgumentParser()
parser.add_argument("--infile", type=str, required=True)
args = parser.parse_args()

# READ DATA
data = pd.read_csv(args.infile)

# ENCODE DATA
aligned = extra_funcs.align_abs(data.Hchain, data.Lchain)
encoded = extra_funcs.one_hot_encode(aligned.Hchain_align, aligned.Lchain_align)

# PREDICT
modelfile = 'finalized_model.sav'
loaded_model = joblib.load(modelfile)
y_pred = loaded_model.predict_proba(encoded)

# SAVE PREDICTIONS WITH THE COLUMN NAME prediction IN THE FILE predictions.csv
pd.DataFrame(y_pred[:, 1], columns=['prediction']).to_csv("predictions.csv", index=False)
