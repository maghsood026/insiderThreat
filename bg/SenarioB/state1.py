import pandas as pd
import os
class State1:
    """
    user logon to another PC in company
    """
    def __init__(self, filename, outputfile, senraiofile):
        """
        :param filename:
        :param outputfile:
        :param senraiofile:
        """
        self.filename = filename
        self.outputfile = outputfile
        self.senariofile = senraiofile

    def get_dataframe(self, filename):
        """
        create dataframe for each filename
        :param filename:
        :return:
        """
        df = pd.read_csv(filename, low_memory=False)
        return df

    def get_all_users(self):
        """
        get set of all users
        :return:
        """
        df = pd.read_csv(self.outputfile)
        return set(df["user_id"].values)

    def remove_ex_columns(self, filename):
        """
        remove extra columns for increase speed of process
        :param filename:
        :return:
        """
        df = pd.read_csv(filename)
        return df.drop(columns=['id', 'date', 'activity'])

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
        csv_input['state3'] = 0
        csv_input['state4'] = 0
        csv_input['state5'] = 0
        csv_input.to_csv(self.senariofile)

    def add_malicious_rate_col(self):
        """
        append malicious_rate col name in the end of UserProfile.csv
        :return:
        """
        csv_input = pd.read_csv('UserProfile.csv')
        csv_input['malicious_rate'] = 0
        csv_input.to_csv('UserProfile.csv', index=False)

    def user_logon_to_another_pc(self):
        """
        update state1 in SenarioB.csv file
        :return:
        """
        df1 = df = self.get_dataframe(self.senariofile)
        df = self.get_dataframe(self.filename)
        profileDf = self.get_dataframe(self.outputfile)
        for user in self.get_all_users():
            inuser = df["user"] == user
            islogon = df["activity"] == "Logon"
            pc_id = df[inuser]["pc"] != profileDf[profileDf["user_id"] == user]["pc"].values[0]
            try:
                df1.loc[df1["user_id"] == user, "state1"] = len(df[inuser & pc_id & islogon])
            except Exception as e:
                pass
        df1.to_csv(self.senariofile, index=False)


DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/"

s1 = State1(DIR + 'logon.csv', DIR + 'UserProfile.csv', DIR + "SenarioB.csv")
s1.user_logon_to_another_pc()




