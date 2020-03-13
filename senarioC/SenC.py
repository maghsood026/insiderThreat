import pandas as pd
from senarioC.AttachedEmail import AttachedEmailSen
import os
import json


def get_data_frame(filename):
    df = pd.read_csv(filename)
    return df


def get_path(filename):
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/"
    return directory + filename


class GenerateJsonFileSenC:
    def __init__(self, logon, email, profile, output_file):
        self.logon = logon
        self.email = email
        self.profile = profile
        self.output_file = output_file

    def get_all_users(self):
        """
        get set of all users
        :return:
        """
        profile = get_path(self.profile)
        df = pd.read_csv(profile, low_memory=False)
        return set(df["user_id"].values)

    def get_info_of_attached_email(self):
        states = AttachedEmailSen(get_data_frame(get_path(self.logon)), get_data_frame(get_path(self.email)),
                                  self.get_all_users())
        return states.get_info_from_attached_emails()

    def generate_json_file(self):
        try:
            with open(self.output_file, 'w') as fb:
                json.dump(self.get_info_of_attached_email(), fb)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    cs = GenerateJsonFileSenC('logon.csv', 'email.csv', 'UserProfile.csv', 'SenarioC.json')
    cs.generate_json_file()