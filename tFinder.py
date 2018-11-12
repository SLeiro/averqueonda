from twython import Twython
from pprint import pprint
import pandas as pd
from dao import YmlDao
# import ntlk



yml = YmlDao('credential.yml', 'api')
credentials = {1: yml.public, 2: yml.private}
python_tweets = Twython(credentials[1], credentials[2])

def search_tweets(q=''):
    query = {'q': q,
            'count': 10,
            }

    dict_ = {'user': [], 'tweet': []}
    for status in python_tweets.search(**query)['statuses']:
        dict_['user'].append(status['user']['screen_name'])
        dict_['tweet'].append(status['text'])
    # Structure data in a pandas DataFrame for easier manipulation
    print(pprint(dict_, indent=2))
    df = pd.DataFrame(dict_)
    print(df)
    df.to_csv('pepe.csv')

if __name__ == '__main__':
    search_tweets('q')
