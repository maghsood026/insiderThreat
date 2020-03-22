import os
import json
import pandas as pd


def get_senario_path(senarioname):
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/anomalyDetection/' + "/{}/".format(
        senarioname)
    return directory + senarioname + '.json'


def get_profile_dataframe():
    return pd.read_csv('UserProfile.csv')


class GenerateProfile:
    def __init__(self, senarioA, senarioB, senarioC, Output):
        self.senarioA = senarioA
        self.senarioB = senarioB
        self.senarioC = senarioC
        self.Output = Output

    def get_dict(self, senarioname):
        data = {}
        with open(get_senario_path(senarioname), 'r') as file:
            data = json.load(file)
        return data

    def get_dict_for_pie_chart(self):
        profile = {'users': {}}
        data_senarioA = self.get_dict(self.senarioA)
        profile_df = get_profile_dataframe()
        for user in data_senarioA['users']:
            is_user = profile_df['user_id'] == user
            role = profile_df[is_user]['role'].values[0]
            malicious_rate = int(((data_senarioA['users'][user]['count_of_visited_url']) / 1000) + (
                    (data_senarioA['users'][user]['count_of_abnormal_time']) / 200))
            profile['users'].update({user: {
                'role': role,
                'malicious_rate': malicious_rate
            }})
        return profile

    def generate_json_file(self):
        try:
            with open('visualization/'+self.Output, 'w') as file:
                json.dump(self.get_dict_for_pie_chart(), file)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    GP = GenerateProfile('SenarioA', 'SenarioA', 'SenarioA', 'Output.json')
    GP.generate_json_file()
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

