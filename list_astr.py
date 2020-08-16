import data
import T_list_astr

URL = "https://api.nasa.gov/neo/rest/v1/feed"


def run():
    request = data.requests.get(URL, data.params)
    count = request.headers['X-RateLimit-Remaining']
    data.count_req = count
    text = data.json.loads(request.text)
    list_astr = text['near_earth_objects']['2020-08-18']
    l_astr = ""
    for i in range(len(list_astr)):
        l = list_astr[i]
        l_astr+= str(l['name']) + "  "   + str(l['estimated_diameter']['kilometers']['estimated_diameter_max']) + "\n"
    t = T_list_astr.show_astr()
    t.show(l_astr)


