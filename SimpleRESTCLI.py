"""Simple Bb REST API CLI v0.0.1
Usage:
  SimpleRESTCLI.py users [USER_ID] [options]
  SimpleRESTCLI.py [options]
  SimpleRESTCLI.py (-h | --help)
  SimpleRESTCLI.py --version

Command:
  USER_ID: The user to provide and REST Action to.
    default: _x_1 
    externalId: externalId:<USER_ID>
    userName: userName:<USER_ID> where USER_ID = userName (jdoe)
    uuid: uuid:<USER_ID> where USER_ID = uuid (xxxx)

Options:
  -h, --help      Show this screen.
  -v, --verbose   Verbose mode.
  -p, --post      Do a post Test.
  -d, --delete    Do a delete Test.
"""

import requests
import json
from docopt import docopt

key = 'your_key_from_devloper.blackboard.com_registration'
secret = 'secretfrom_devloper.blackboard.com_registration'
target_domain = 'yourbbinstance.domain.edu'
set_token_path = '/learn/api/public/v1/oauth2/token'
user_path = '/learn/api/public/v1/users'
payload =  { "grant_type": "client_credentials","token": None}

def set_token():
    oauth_url = 'https://' + target_domain + set_token_path
    
    if debug:
      print('[POST] OAuth2 Set Token URL: ' + oauth_url)

    oauth_res = requests.post(oauth_url, data=payload, auth=(key, secret))
    
    if debug:
      print('=== Token Response ===\n%s\n' % oauth_res.text)
    
    payload['token'] = oauth_res.json()['access_token']


def get_user(user_id=None):
    user_url = 'https://' + target_domain + user_path + '/' + (user_id or '')
    auth = "Bearer %s" % payload['token']
    headers = {'Authorization': auth, 'Content-Type': 'application/json'}
    
    if debug:
      print('[GET] Users URL: ' + user_url)
    
    res = requests.get(user_url, headers=headers)
    
    if debug:
      print('=== Users Response ===\n%s\n' % res.json())
    return res.json()

def post_user(data):
    user_url = 'https://' + target_domain + user_path
    auth = "Bearer %s" % payload['token']
    headers = {'Authorization': auth, 'Content-Type': 'application/json'}
    print('[POST] Users URL: ' + user_url)
    res = requests.post(user_url, headers=headers, data=data)
    print('=== Users POST Response ===\n%s\n' % res.text)
    return res.json()

def delete_user(user_id):
    user_url = 'https://' + target_domain + user_path + '/' + user_id
    auth = "Bearer %s" % payload['token']
    headers = {'Authorization': auth, 'Content-Type': 'application/json'}
    print('[DELETE] User URL: ' + user_url)
    res = requests.delete(user_url, headers=headers)
    print('=== User DELETE Response ===\n%s\n' % res.text)
    return res.json()

def main():
  if debug:
    print(args)
  set_token()

  if args['--post']:
    user_data = '''{
                "externalId": "test.python.user",
                "dataSourceId": "_2_1",
                "userName": "python_demo",
                "password": "python36",
                "availability": {
                  "available": "Yes"
                },
                "name": {
                  "given": "Python",
                  "family": "Demo"
                },
                "contact": {
                  "email": "no.one@ereh.won"
                }
              }'''

    posted_user = post_user(json.dumps(json.loads(user_data)))

    if debug:
      print(posted_user)
  
  elif args['--delete']:
    # Tradionally you want to check for the USER
    deleted_user = delete_user('userName:python_demo')
    
    if debug:
      print(deleted_user)

  else:
    user = get_user(args['USER_ID'])
    
    print(user)

    if args['USER_ID']:
      print('user ID: {} email: {}'.format(user['userName'], 
            user['contact']['email']))

if __name__ == '__main__':
  args = docopt(__doc__, version='Simple Bb REST API CLI v0.0.1')
  debug = args['--verbose']
  main()
