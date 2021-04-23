import pandas as pd
from glob import glob
from tqdm import tqdm

data = pd.concat([pd.read_csv(file, header=1) for file in tqdm(glob("csv/*/*"))])
data.to_csv("mydata.csv", index=False)
