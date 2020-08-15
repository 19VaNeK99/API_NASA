import requests
import webbrowser
import json
key = "wr1ajr3l9XhJqt9EkpfEyZ9ylJk59jqphiJ2KZ4A"
URL = "https://api.nasa.gov/planetary/apod"

params = {
    "api_key":key
}
url_im = ""
zap = requests.get(URL, params)
if zap.status_code == 200:
    print(zap.headers['X-RateLimit-Remaining'])
    url_im = json.loads(zap.text)["hdurl"]

if url_im:
    webbrowser.open(url_im, new=2)