import data
import T_show_img
import time
URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

camera = ['FHAZ', 'RHAZ', 'MAST', 'CHEMCAM', 'MAHLI', 'MARDI', 'NAVCAM']





def run():
    params = data.params.copy()
    params['page'] = 1
    params['sol'] = data.random.randint(0, 1000)
    params['camera'] = data.random.choices(camera)
    request = data.requests.get(URL, params)
    image = data.json.loads(request.text)['photos']
    count_req = 0
    while not image and count_req < 10:
        params['sol'] = data.random.randint(0, 1000)
        time.sleep(0.1)
        request = data.requests.get(URL, params)
        image = data.json.loads(request.text)['photos']
        count_req +=1
    if image:
        if request.status_code == 200:
            data.count_req = request.headers['X-RateLimit-Remaining']
        image = data.random.choices(image)
        image_request = data.requests.get(image[0]["img_src"])
        out = open("img.png", "wb")
        out.write(image_request.content)
        out.close()
        time.sleep(0.1)
        window_image = T_show_img.show()
    else:
        print("Ошибка, попробуйте позже")





