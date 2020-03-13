import pandas as pd
import os

class State2:

    def __init__(self, filename, outputfile, senariofile):
        self.filename = filename
        self.outputfile = outputfile
        self.senariofile = senariofile

    def get_dataframe(self, filename):
        df = pd.read_csv(filename)
        return df

    def get_all_users(self):
        """
        get set of all users
        :return:
        """
        df = pd.read_csv(self.outputfile)
        return set(df["user_id"].values)

    def sent_email_in_another_pc(self):
        """
        update state2 in SenarioB.csv file
        :return:
        """
        df1 = self.get_dataframe(self.senariofile)
        df = self.get_dataframe(self.filename)
        profileDf = self.get_dataframe(self.outputfile)
        for user in self.get_all_users():
            inuser = df["user"] == user
            isconnect = df["activity"] == "Connect"

            pc_id = df[inuser]["pc"] == profileDf[profileDf["user_id"] == user]["pc"].values[0]
            try:
                pass
                df1.loc[df1["user_id"] == user, "state2"] = len(df[inuser & pc_id & isconnect])
            except Exception as e:
                pass
        df1.to_csv(self.senariofile, index=False)

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/"

s2 = State2(DIR + 'device.csv', DIR + 'UserProfile.csv', DIR + "SenarioB.csv")
print(s2.sent_email_in_another_pc())