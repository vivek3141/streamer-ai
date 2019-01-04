<script src="//yihui.name/js/math-code.js"></script>
<!-- Just one possible MathJax CDN below. You may use others. -->
<script async
  src="//mathjax.rstudio.com/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
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
and install `mpg123`, `fceux` and add them to `PATH`.

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
You can also use python's `requests` library instead of `curl`
* Install with `pip install requests`
* Example to get `socket_token`:
```python
import requests

url = "https://streamlabs.com/api/v1.0/socket/token"

querystring = {"access_token":"access_token"}

response = requests.request("GET", url, params=querystring)

print(response.text)
```
Put the `socket_token` in a file called `config`, with the following format, shown in
`config.example`:
```
socket_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
```
## How it works
For an explanation for how the game runs, watch [this video](https://www.youtube.com/watch?v=hNDkjy2rXG4&).
### Short Explanation
#### How the game is played
This program uses a mathematical model, called a neural network, which simulates the brain of a human being. 
A neural network works by taking inputs and outputting probabilities for each of the outputs. This can be accomplished
by using a sigmoid function. <br><br>
![Sigmoid](https://qph.fs.quoracdn.net/main-qimg-07066668c05a556f1ff25040414a32b7)
<br><br>
`Neuroevolution of Augmenting Topologies`, or `NEAT` is what this project uses. The way standard
`neuroevolution` works is by randomly initializing a population of neural networks and
using survival of the fittest to get the best model. The best networks in each generations
are bred and some mutations are introduced. `NEAT` introduces features like speciation to
make a much more effective neuroevolution model. Neuroevolution is known to do better than standard
reinforcement learning models.<br>
#### How the commentary works
Using a `socketio` client for python, we can ge



