import requests
import random
import time

session = requests.Session()

class NitroTypePY:
    def create(username, password, email, wpm, accuracy):
        create_res = session.post(
            'https://www.nitrotype.com/api/v2/auth/register/username',
            headers = {
                'authority': 'www.nitrotype.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://www.nitrotype.com',
                'pragma': 'no-cache',
                'referer': 'https://www.nitrotype.com/race',
                'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
            },
            json = {
                'username': username,
                'password': password,
                'email': email,
                'acceptPolicy': 'on',
                'receiveContact': '',
                'tz': 'America/New_York',
                'qualifying': 1,
                'avgSpeed': wpm,
                'avgAcc': accuracy,
                'carID': 9,
                'raceSounds': 'only_fx',
            }
        )
        return create_res
    
    def friend_requests(cookie):
        friend_res = session.get(
            'https://www.nitrotype.com/api/v2/friend-requests',
            headers = {
                'authority': 'www.nitrotype.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'authorization': 'Bearer %s' % cookie,
                'origin': 'https://www.nitrotype.com',
                'pragma': 'no-cache',
                'referer': 'https://www.nitrotype.com/',
                'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
            },
            params = {
                'r': '0.%s' % time.time(),
            }
        )
        return friend_res
    
    def accept_friend(friend_id, cookie):
        accept_res = session.post(
            'https://www.nitrotype.com/api/v2/friend-requests/%s/accept' % friend_id,
            headers = {
                'authority': 'www.nitrotype.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'authorization': 'Bearer %s' % cookie,
                'origin': 'https://www.nitrotype.com',
                'pragma': 'no-cache',
                'referer': 'https://www.nitrotype.com/',
                'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
            },
            json = {}
        )
        return accept_res
    
    def friend(friend_id, cookie):
        fr_res = session.post(
            'https://www.nitrotype.com/api/v2/friend-requests/%s/request' % friend_id,
            headers = {
                'authority': 'www.nitrotype.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'authorization': 'Bearer %s' % cookie,
                'origin': 'https://www.nitrotype.com',
                'pragma': 'no-cache',
                'referer': 'https://www.nitrotype.com/',
                'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
            },
            json = {}
        )
        return fr_res


        