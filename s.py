import pandas as pd

df = pd.read_csv('UserProfile.csv', index_col=False)


def get_users(df):
    return list(set(list(df['user_id'].values)))


user_id = [x for x in get_users(df)]

# List2
email = [list(set(df[df['user_id'] == x]['email']))[0] for x in get_users(df)]
role = [list(set(df[df['user_id'] == x]['role']))[0] for x in get_users(df)]
team = [list(set(df[df['user_id'] == x]['team']))[0] for x in get_users(df)]
pc = [list(set(df[df['user_id'] == x]['pc']))[0] for x in get_users(df)]
malicious_rate = [list(set(df[df['user_id'] == x]['malicious_rate']))[0] for x in get_users(df)]

list_of_tuples = list(zip(user_id, email, role, team, pc, malicious_rate))
df = pd.DataFrame(list_of_tuples, columns=['user_id', 'email', 'role', 'team', 'pc', 'malicious_rate'])
df.to_csv('UserProfile.csv')
