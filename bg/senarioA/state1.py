import pandas as pd
from re import search
import os

class State1:
    """
    implement senario that user that visited url frequently ...
    """
    def __init__(self, filename, output, senariofile):
        self.filename = filename
        self.output = output
        self.senariofile = senariofile

    def get_dataframe(self, filename):
        df = pd.read_csv(filename)
        return df

    def get_all_users(self):
        """
        get set of all users
        :return:
        """
        df = pd.read_csv(self.output)
        return set(df["user_id"].values)

    def generate_senario_file(self):
        """
        generate SenarioB.csv file with user_id, state1, state2, state3, state4, state5 fields
        :return:
        """
        users = self.get_all_users()
        dict = {
            'user_id': list(users)
        }
        csv_input = pd.DataFrame.from_dict(dict)
        csv_input['state1'] = 0
        csv_input['state2'] = 0
        csv_input.to_csv(self.senariofile)

    def have_and_count_spc_url(self, list):
        count = 0
        for url in list:
            if search("http://dropbox.com", url):
                count += 1
        if count != 0:
            return count, True
        else:
            return 0, False


    def visited_spc_url(self):
        df = self.get_dataframe(self.filename)
        df1 = self.get_dataframe(self.senariofile)
        print(df1)
        print()
        for user in self.get_all_users():
            isuser = df["user"] == user
            count, visited_spc_url = self.have_and_count_spc_url(list(df[isuser]["url"].values))
            if visited_spc_url:
                try:
                    df1.loc[df1["user_id"] == user, "state1"] = 1
                    df1.loc[df1["user_id"] == user, "state2"] = count
                except Exception as e:
                    pass
        df1.to_csv(self.senariofile, index=False)





DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/"

s1 = State1(DIR + "http.csv", DIR + "UserProfile.csv", DIR + "SenarioA.csv")
s1.visited_spc_url()
