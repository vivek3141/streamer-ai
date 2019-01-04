# Streamer-AI
Python based AI that uses Recurrent Neural Networks, Neuroevolution and Streamlabs APIs to live stream games while commentating over them at the same time.

## Requirements
Install the requirements with
```bash
sudo make
```

#### Alternative
Install the python requirements with
```bash
pip install -r requirements.txt
```
and install `mpg123`

## Getting the API Key
* Go to `streamlabs.com` then sign in using your account. Then go to API settings, 
create a new app and copy the client ID and client Secret. Click the `Sample Authentication URL` below and then copy
the code in the URL.
* Call a `POST` request to `/token`. Make sure to use the same Redirect URI as set up in the app. Example:
```bash
curl --request POST \
     --url 'https://streamlabs.com/api/v1.0/token' \
     -d 'grant_type=grant_type&client_id=client_id&client_secret=client_secret&redirect_uri=redirect_uri'
 ```
 Example return:
 ```bash
 {
  access_token: 'loXk8FTOFwKfrLP3bGCnJldBxuGX03a03iQdxR8A',
  token_type: 'Bearer',
  refresh_token: 'IXCGDha46Q4eHBKrijmAqUwScbsMSuBy9IopXp80'
}
 ```
 * Authorize this `access_token` for the scope `socket.token` using `/authorize`. Example:
 ```bash
 curl --request GET \
  --url 'https://streamlabs.com/api/v1.0/authorize?response_type=response_type&client_id=client_id&redirect_uri=redirect_uri&scope=socket.token'
  ```
 * Use the `access_token` to get a `socket_token`. Call a `GET` request to `/socket/token`. Example:
```bash
 curl --request GET \
  --url 'https://streamlabs.com/api/v1.0/socket/token?access_token=access_token'
```
You can also use python's `reqests` library instead of `curl`
* Install with `pip install requests`
* Example to get `socket_token`:
```python
import requests

url = "https://streamlabs.com/api/v1.0/socket/token"

querystring = {"access_token":"access_token"}

response = requests.request("GET", url, params=querystring)

print(response.text)
```

