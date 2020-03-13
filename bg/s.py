import pandas as pd
if __name__ == "__main__":
    df = pd.read_csv('ee.csv', low_memory=False).head(1009000).drop('Unnamed: 0')
    df.to_csv('ee.csv')