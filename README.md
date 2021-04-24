# Prediction of heavy and light chain antibody pairing

Fork this challenge repository as a starting template at the beginning of the hackathon.

## Challenge Aim

The aim of this challenge is to predict heavy and light chain antibody pairing. You are given a CSV file using the `--infile` argument, with the columns Hchain for heavy chain sequences and Lchain for light chain sequences. For each set of heavy and light chain, your output prediction needs to be a value between 0 and 1. 

### Example Output
You code should output a file called `predictions.csv` in the following format:

```
prediction
0.42
0.475
0.7
```

## Benchmarking System
The continuous integration script in `.github/workflows/ci.yml` will automatically build the `Dockerfile` on every commit to the `main` branch. This docker image will be published as your hackathon submission to `https://biolib.com/<YourTeam>/<TeamName>`. For this to work, make sure you set the `BIOLIB_TOKEN` and `BIOLIB_PROJECT_URI` accordingly as repository secrets. 
