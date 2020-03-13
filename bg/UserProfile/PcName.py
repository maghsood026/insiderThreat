import pandas as pd
from statistics import mode


class UserPcName:
    def __init__(self, filename, outputfile):
        self.filename = filename
        self.outputfile = outputfile

    def get_all_users(self):
        df = pd.read_csv(self.outputfile)
        return set(df["user_id"].values)

    def get_dataframe(self, filename):
        df = pd.read_csv(filename)
        return df

    def add_pc_name_col(self):
        """
        create pc column with None value :)
        :return:
        """
        csv_input = pd.read_csv('UserProfile.csv')
        csv_input['pc'] = ""
        csv_input.to_csv('UserProfile.csv', index=False)

    def remove_ex_col(self):
        df = pd.read_csv('logon.csv')
        new_df = df.drop(columns=['id', 'date', 'activity'])
        return new_df

    def detect_user_pc_name(self):

        df = self.remove_ex_col()
        df1 = self.get_dataframe(self.outputfile)
        for user in self.get_all_users():
            try:
                df1.loc[df1["user_id"] == user, "pc"] = mode(df[df["user"] == user]["pc"].values)
            except:
                pass
        df1 = df1.drop(columns=['Unnamed: 0'])
        df1.to_csv(self.outputfile)


up = UserPcName("logon.csv", 'UserProfile.csv')
up.detect_user_pc_name()