import pandas as pd
from SenarioC.UnNormalLogon import AbnormalLogon
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


def have_attached_file(email_df):
    count = 0
    try:
        if int(email_df["attachments"]) <= 20:
            count = email_df["attachments"]
    except:
        pass

    if count != 0:
        return True
    else:
        return False


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
         user: {
                'count_of_attached_file': integer,
                'time_of_send': [list of times],
                'count_of_abnormal_time': integer
                 }
        """
        attached_file_dict = {'users': {}}
        df = self.emailDF
        for user in self.allUsers:
            isuser = df["user"] == user
            sent_attached_file = have_attached_file(df)
            times = list(df[isuser & sent_attached_file]['date'].values)
            df = self.rm_extra_col()
            attached_file_dict['users'].update({user: {
                'count_of_attached_file': int(get_len_of_attached_file(list(df[isuser]["attachments"].values))),
                'time_of_send': times,
                'count_of_abnormal_time': int(self.is_in_abnormal_time(user, times))}})

        return attached_file_dict

    def is_in_abnormal_time(self, user, list_of_time):
        return len(set(list(pd.to_datetime(list_of_time)))) - len(
            np.setdiff1d([d.hour for d in list(pd.to_datetime(list_of_time))], self.anomalyLogon(user)))
