import requests
import json

key = 'your_key_from_devloper.blackboard.com_registration'
secret = 'secretfrom_devloper.blackboard.com_registration'
target_domain = 'yourbbinstance.domain.edu'
set_token_path = '/learn/api/public/v1/oauth2/token'
user_path = '/learn/api/public/v1/users'
payload =  {"grant_type": "client_credentials","token": None}

def set_token():
    oauth_url = 'https://' + target_domain + set_token_path
    print('[POST] OAuth2 Set Token URL: ' + oauth_url)
    oauth_res = requests.post(oauth_url, data=payload, auth=(key, secret))
    print('=== Token Response ===\n%s\n' % oauth_res.text)
    payload['token'] = oauth_res.json()['access_token']

    
def get_user(user_id):
    user_url = 'https://' + target_domain + user_path + '/userName:' + user_id
    auth = "Bearer %s" % payload['token']
    headers = {'Authorization': auth, 'Content-Type': 'application/json'}
    print('[GET] Users URL: ' + user_url)
    res = requests.get(user_url, headers=headers)
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

def main():
    set_token()
    
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
    print(get_user('python_demo'))


if __name__ == '__main__':
    main()