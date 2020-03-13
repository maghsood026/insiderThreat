import pandas as pd
import os

class State1:
    """
    implement senario that user that sent frequently attached email ...
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
        generate senarioC.csv file with user_id, state1, state2
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


    def count_of_attached_file(self, list):
        count = 0
        for c in list:
            count += c
        return count

    def sent_attached_file(self):
        df = self.get_dataframe(self.filename)
        df1 = self.get_dataframe(self.senariofile)
        for user in self.get_all_users():
            isuser = df["user"] == user
            sent_attached_file = df["attachments"] != 0
            my_df = df[sent_attached_file & isuser]
            print(list(df[sent_attached_file & isuser]["attachments"].values))
            if not False:
                try:
                    pass
                    # print(self.count_of_attached_file(list(df[sent_attached_file & isuser]["attachments"].values)))
                    # df1.loc[df1["user_id"] == user, "state1"] = 1
                    # df1.loc[df1["user_id"] == user, "state2"] = self.count_of_attached_file(list(df[sent_attached_file & isuser]["attachments"].values))
                except Exception as e:
                    pass
        df1.to_csv(self.senariofile, index=False)






DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/"

s1 = State1(DIR + "email.csv", DIR + "UserProfile.csv", DIR + "SenarioC.csv")
s1.sent_attached_file()
