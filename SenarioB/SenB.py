from SenarioB.ConnectTOAnotherPc import TakeAnotherPc
from SenarioB.BasicClass import Basic
import pandas as pd
import os
import json


def get_file_path(filename):
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/"
    return directory + filename


def get_data_frame(filename):
    """
    create data frame for each filename
    :param filename:
    :return: data frame
    """
    df = pd.read_csv(filename, low_memory=False)
    return df


class GenerateJsonFileSenB(Basic):

    def __init__(self, logon_file, device_file, profile, output_file):
        super().__init__()
        self.logon_file = logon_file
        self.device_file = device_file
        self.profile = profile
        self.output_file = output_file

    def get_all_users(self):
        """
        get set of all users
        :return:
        """
        df = pd.read_csv(get_file_path(self.profile))
        return set(df["user_id"].values)

    def get_info_used_another_pc(self):
        """
        dict of information of user used another computer and connect usb and calculate this action in un normal
        times for each users :return:
        """
        s1 = TakeAnotherPc(get_data_frame(get_file_path(self.logon_file)),
                           get_data_frame(get_file_path(self.device_file)),
                           get_data_frame(get_file_path(self.profile)), self.get_all_users())
        return s1.get_info_users_used_another_pc()

    def generate_json_file(self):
        try:
            with open(self.output_file, 'w') as fb:
                json.dump(self.get_info_used_another_pc(), fb)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    json_file = GenerateJsonFileSenB('logon.csv', 'device.csv', 'UserProfile.csv', 'SenarioB.json')
    json_file.generate_json_file()