
import data
import  webbrowser
#from T_Gui import update_count
URL = "https://api.nasa.gov/planetary/apod"

def run():
    url_im = ""
    request = data.requests.get(URL, data.params)
    if request.status_code == 200:
        data.count_req = request.headers['X-RateLimit-Remaining']
        url_im = data.json.loads(request.text)["hdurl"]
    else:
        print("Error")

    if url_im:
        webbrowser.open(url_im, new=2)

