import pandas as pd
from statistics import mode


class AbnormalLogon:
    """
    generate list of unusual logon time
    """
    def __init__(self, logon_df):
        self.logon_df = logon_df

    def anomalyLogon(self, user):
        """

        :param user:
        :return: list of unusual logon
        """
        new_array = []
        logons, logoff = self.get_user_activity(user)
        for i in logons:
            try:
                if i > mode(logoff) or (i < mode(logons) and abs(i - mode(logons)) > 1):
                    new_array.append(i)
            except Exception as e:
                pass

        return new_array

    def get_user_activity(self, user):
        """
        detect all logon and logoff user
        :param user:
        :return: logons (list) and logoffs(list)
        """
        df = self.logon_df
        isuser = df["user"] == user
        logon = df["activity"] == "Logon"
        logoff = df["activity"] == "Logoff"
        logons = [d.hour for d in list(pd.to_datetime(df[isuser & logon]["date"]))]
        logoffs = [d.hour for d in list(pd.to_datetime(df[isuser & logoff]["date"]))]
        return logons, logoffs
