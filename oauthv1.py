from requests_oauthlib import OAuth1Session
from datetime import datetime
import yaml

with open('data.yml', 'r') as f:
    data = yaml.load(f)

oauth = OAuth1Session(data['client_key'],
        client_secret=data['client_secret'])

start_date = int(datetime.strptime(data['start_date'] , '%d/%m/%Y').timestamp())
end_date = int(datetime.strptime(data['end_date'] , '%d/%m/%Y').timestamp())
publisher_id = data['publisher_id']

base_url = f'https://console.inner-active.com/iamp/services/performance/publisher/{publisher_id}/{start_date}/{end_date}'

headers = {
  "Content-type": "application/json",
  "Accept": "application/json"
}

r = oauth.get(base_url, headers=headers)

print(r.content)

