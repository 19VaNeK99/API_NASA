from  tkinter import *
import img_day
import list_astr
import main

def get_img():
    img_day.run()
    update_count()

def get_list_astr():
    list_astr.run()
    update_count()

def update_count():
    count_req_Lab.configure(text = str(main.count_req))

window = Tk()

window.geometry("500x500")
window.title("NASA")

#Отображение количества доступных запросов
count_req_Lab = Label(window, text = main.count_req )
count_req_Lab.place(x= 350, y = 30)

#Кнопка для получения картинки дня
but_img_day = Button(window, text = "Получить картинку дня", font=("Ariel Bold", 10), width = 20, command = get_img)
but_img_day.place(x = 160, y = 100)
#Получить список околоземных астеройдов
but_list_astr = Button(window, text = "Получить список околоземных астеройдов",  width = 35, command = get_list_astr)
but_list_astr.place(x = 130, y = 150)

window.mainloop()


