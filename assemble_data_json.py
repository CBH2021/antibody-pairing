import pandas as pd
from glob import glob
from tqdm import tqdm

data = pd.concat([pd.read_json(file, lines=True) for file in tqdm(glob('*.json.gz'))])
data.to_csv('human-unpaired-heavy.csv', index=False)