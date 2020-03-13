import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from statistics import mode

class UserBehavior:
    def __init__(self, filename):
        self.filename = filename

    def get_dataFram(self):
        df = pd.read_csv(self.filename)
        new_df = df.drop(columns=['id'])
        return new_df

    def get_of_all_user(self):
        df = self.get_dataFram()

        return set(df['user'].unique())

    def anomalyLogon(self, user):
        new_array = []
        logons, logoff = self.get_user_activity(user)
        for i in logons:
            if i > mode(logoff) or (i < mode(logons) and abs(i - mode(logons))>1):
                new_array.append(i)
        return new_array
    def get_user_activity(self, user):
        df = self.get_dataFram()
        isuser = df["user"] == user
        logon = df["activity"] == "Logon"
        logoff = df["activity"] == "Logoff"
        logons = [d.hour for d in list(pd.to_datetime(df[isuser & logon]["date"]))]
        logoffs = [d.hour for d in list(pd.to_datetime(df[isuser & logoff]["date"]))]
        return logons, logoffs

    def show_activity(self):
        pass

if __name__ == "__main__":
    ub = UserBehavior('logon.csv')
    user = "IIW0249"
    # print(ub.get_user_activity(user))

