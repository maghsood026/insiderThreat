import pandas as pd
from senarioC.UnNormalLogon import AbnormalLogon
import numpy as np


def get_len_of_attached_file(list_of_file):
    count = 0
    try:
        for c in list_of_file:
            if c <= 10:
                count += c
    except Exception as e:
        pass
    return count


def get_len_of_attached_file(list_of_file):
    count = 0
    for c in list_of_file:
        try:
            c = int(c)
            if c <= 20:
                count += c
        except Exception as e:
            pass

    return count


class AttachedEmailSen(AbnormalLogon):
    """
    implement senario that user that sent frequently attached email ...
    """

    def __init__(self, logonDF, emailDF, allUsers):
        super().__init__(logonDF)
        self.logonDF = logonDF
        self.emailDF = emailDF
        self.allUsers = allUsers

    def rm_extra_col(self):
        return self.emailDF.drop(columns=['Unnamed: 0'])

    def get_info_from_attached_emails(self):
        """
         calculate use ful information for attached emails
        :return: dictionary information
        """
        attached_file_dict = {'users': {}}
        df = self.emailDF
        for user in self.allUsers:
            isuser = df["user"] == user
            sent_attached_file = df["attachments"] != 0
            times = list(df[isuser & sent_attached_file]['date'].values)
            df = self.rm_extra_col()
            attached_file_dict['users'].update({user: {
                'count_of_attached_file': int(get_len_of_attached_file(list(df[isuser]["attachments"].values))),
                'time_of_send':
                    times, 'count_of_abnormal_time': int(self.is_in_abnormal_time(user, times))}})

        return attached_file_dict

    def is_in_abnormal_time(self, user, list_of_time):

        return len(np.setdiff1d(self.anomalyLogon(user), [d.hour for d in list(pd.to_datetime(list_of_time))]))


