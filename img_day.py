
import main
import  webbrowser
#from T_Gui import update_count
URL = "https://api.nasa.gov/planetary/apod"

def run():
    url_im = ""
    zap = main.requests.get(URL, main.params)
    if zap.status_code == 200:
        main.count_req = zap.headers['X-RateLimit-Remaining']
        url_im = main.json.loads(zap.text)["hdurl"]

    if url_im:
        webbrowser.open(url_im, new=2)

