import json
from senarioC.UnNormalLogon import AbnormalLogon
import pandas as pd
import numpy as np


class TakeAnotherPc(AbnormalLogon):
    """
    calculate users who logon to computers that not belong for that user
    and connect usb to that computers
    """

    def __init__(self, logon_df, device_df, profile_df, all_users):
        """
        :param logon_df:
        :param device_df:
        :param profile_df:
        :param all_users:
        """
        super().__init__(logon_df)
        self.logon_df = logon_df
        self.device_df = device_df
        self.profile_df = profile_df
        self.all_user = all_users

    def list_of_time_usb_connected(self, user):
        """
        calculate list of time that usb connected
        :return:list_of_times
        """
        is_user = self.device_df["user"] == user
        connected = self.device_df["activity"] == "Connect"
        pc_id = self.device_df[is_user]["pc"] != self.profile_df[self.profile_df["user_id"] == user]["pc"].values[0]
        list_of_times = list(self.device_df[is_user & pc_id & connected]['date'].values)
        return list_of_times

    def get_info_users_used_another_pc(self):
        """
        generate dict of user that used another computer and
        :return:
        """
        dict_of_state = {'users': {}}
        for user in self.all_user:
            is_user = self.logon_df["user"] == user
            is_logon = self.logon_df["activity"] == "Logon"
            pc_id = self.logon_df[is_user]["pc"] != self.profile_df[self.profile_df["user_id"] == user]["pc"].values[0]

            list_of_time_logon = list(self.logon_df[is_user & pc_id & is_logon]['date'].values)
            list_of_time_usb_connected = self.list_of_time_usb_connected(user)
            total_times = list_of_time_logon + list_of_time_usb_connected
            dict_of_state['users'].update(
                {user: {'logon_to_another_pc': {'count_of_logon': len(list_of_time_logon),
                                                'time_of_logon': list_of_time_logon},
                        'connect_usb_to_another_pc': {'count_of_connect': len(list_of_time_usb_connected),
                                                      'time_of_connect': list_of_time_usb_connected},
                        'count_of_abnormal_time': self.is_in_abnormal_time(user, total_times)}})

        return dict_of_state

    def is_in_abnormal_time(self, user, list_of_time):
        return len(set(list(pd.to_datetime(list_of_time)))) - len(
            np.setdiff1d([d.hour for d in list(pd.to_datetime(list_of_time))], self.anomalyLogon(user)))
