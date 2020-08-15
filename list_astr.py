import main
import T_list_astr

URL = "https://api.nasa.gov/neo/rest/v1/feed"


def run():
    zap = main.requests.get(URL, main.params)
    count = zap.headers['X-RateLimit-Remaining']
    main.count_req = count
    text = main.json.loads(zap.text)
    list_astr = text['near_earth_objects']['2020-08-18']
    l_astr = ""
    for i in range(len(list_astr)):
        l = list_astr[i]
        l_astr+= str(l['name']) + "  "   + str(l['estimated_diameter']['kilometers']['estimated_diameter_max']) + "\n"
    t = T_list_astr.show_astr()
    t.show(l_astr)


