<h1 align="center">NitroTypePY</h1>
<h2 align="left">Information</h2>

* API wrapper for [nitrotype.com](https://nitrotype.com).
* Still under development and testing

<h2 align="left">Features</h2>

* Accepting friend requests, scanning for incoming friend requests, creating new accounts, and friend users are all features of the wrapper as for now!
* More soon.

<h2 align="left">Usage</h2>

1. Make a user account
```py
from NitroTypePY import *

def register():
    reg = NitroTypePY.create(
        username = 'NTPythonTest',
        password = '', 
        email    = '', 
        wpm      = '115', 
        accuracy = '95'
    )
    print(reg.text)
```
2. Scan for new friend requests.
```py
def req():
    req = NitroTypePY.friend_requests(
       cookie = ''
    )
    print(req.text)
```
3. Accept incoming friend request(s)
```py
def accept():
    accpt = NitroTypePY.accept_friend(
        friend_id = '50',
        cookie    = ''
    )
    print(accpt.text)
```
4. Friend users by entering their unique ID.
```py
def friend():
    fr = NitroTypePY.friend(
        friend_id = '50',
        cookie    = ''
    )
    print(fr.text)
```


<h2 align="left">Support</h2>

* If assistance is required, please create an [issue](https://github.com/nightclubs/NitroTypePY/issues), explaining the problem and what assistance is required.
* If you want to make a suggestion, do the same thing as a support issue, but instead of requesting assistance, simply tell me what to add.
