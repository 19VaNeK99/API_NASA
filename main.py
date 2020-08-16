from  tkinter import *
import img_day
import list_astr
import list_mars_img
import data

def get_img_mars():
    list_mars_img.run()
    update_count()

def get_img():
    img_day.run()
    update_count()

def get_list_astr():
    list_astr.run()
    update_count()

def update_count():
    count_req_Lab.configure(text = str(data.count_req))

window = Tk()

window.geometry("500x500")
window.title("NASA")

#Отображение количества доступных запросов
count_req_Lab = Label(window, text = data.count_req )
count_req_Lab.place(x= 350, y = 30)

#Кнопка для получения картинки дня
but_img_day = Button(window, text = "Получить картинку дня", font=("Ariel Bold", 10), width = 20, command = get_img)
but_img_day.place(x = 160, y = 100)
#Получить список околоземных астероидов
but_list_astr = Button(window, text = "Получить список околоземных астероидов",  width = 35, command = get_list_astr)
but_list_astr.place(x = 130, y = 150)
#Получить рандомную картинку с марсохода Curiosity
but_img_mars = Button(window, text = "Получить фотографию Марса", command = get_img_mars)
but_img_mars.place(x= 150, y = 200)

window.mainloop()


