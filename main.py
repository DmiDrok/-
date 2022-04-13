import tkinter as tk
from tkinter import messagebox
from random import randint

class Window:

    ##Свойства класса Window
    FONT = ("Tahoma", 13)
    BACKGROUND = "#F8F8FA"

    ##Инициализотор
    def __init__(self, width=500, height=150, title="Рандомайзер", resizable=(False, False)):
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}+{(self.root.winfo_screenwidth()-self.root.winfo_reqwidth())//2-100}+{(self.root.winfo_screenheight()-self.root.winfo_reqheight())//2}")
        self.root.title(title)
        self.root.resizable(*resizable)
        self.root["background"] = self.BACKGROUND
        self.root.configure(pady=10, padx=100)
        self.root.iconbitmap(r"C:\Users\user\Desktop\Рандомайзер\icons\icon.ico") ##Устанавливаем иконку

        self._widgets_draw() ##Рисуем виджеты
        self._loop_window() ##Циклим окно
    
    ##Метод отрисовки виджетов
    def _widgets_draw(self):
        def listen_keys(event):
            ##Если был нажат Enter - выполняем функцию show_res
            if event.char == "\r":
                show_res()
                return True

            ##Метод .focus_get() возвращает элемент с фокусом
            if event.char in "0123456789": ##Если значение нажатой кнопки в строке цифр
                self.root.focus_get().delete(len(self.root.focus_get().get())-1, tk.END)
                self.root.focus_get().insert(tk.END, event.char)
            elif event.char == "\x08": ##Если это backspace - то не делаем ничего и даём удалить ему символ
                pass
            elif event.char == "-": ##Если это '-' - то пускай пишется
                pass
            else: ##Иначе - если это буквы - они моментально вставятся и моментально удалятся
                self.root.focus_get().delete(len(self.root.focus_get().get())-1, tk.END)

        def show_res():
            #isdigit = lambda num: num.isdigit() ##Лямбда функция с целью укоротить код
            num_first = entry_number_first.get() ##Получаем первое число ОТ
            num_second = entry_number_second.get() ##Получаем второе число ДО
            print(num_first, num_second, len(num_first), len(num_second))
            ##Проверка на целочисленность данных
            #if not isdigit(num_first) or not isdigit(num_second):
                #messagebox.showerror("Ошибка", "Необходимо вводить целые числа")

            ##Если ОТ будет больше ДО
            if num_first > num_second and len(num_first) > 0 and len(num_second) > 0:
                res = randint(int(num_second), int(num_first))
                messagebox.showinfo("Уведомление", str(res))
            else:
                if len(num_first) == 0 and len(num_second) == 0:
                    messagebox.showerror("Ошибка", "Введите значение \"От\" и \"До\"")
                elif len(num_first) == 0:
                    messagebox.showerror("Ошибка", "Введите значение \"От\"")
                elif len(num_second) == 0:
                    messagebox.showerror("Ошибка", "Введите значение \"До\"")
                else: ##Если не строки и не дроби
                    res = randint(int(num_first), int(num_second))
                    messagebox.showinfo("Уведомление", str(res))

        self.root.bind("<Key>", listen_keys) ##Обработку нажатий отдаём функции listen_keys

        label_number_first = tk.Label(self.root, text="От:", font=("Georgia", 15), background=self.BACKGROUND)
        entry_number_first = tk.Entry(self.root,
            font=self.FONT,
            width=5,
            background="#ffffff",
            border=3,
            )

        label_number_second = tk.Label(self.root, text="До: ", font=("Georgia", 15), background=self.BACKGROUND)
        entry_number_second = tk.Entry(self.root,
            font=self.FONT,
            width=5,
            background="#ffffff",
            border=3,
            )

        btn_show_res = tk.Button(self.root, text="Рандом!", font=("Georgia", 13), background="#ffffff",
            border=3,
            cursor="hand2",
            command=show_res
            )

        label_number_first.place(x=0, y=10)
        label_number_second.place(x=250, y=10)
        entry_number_first.place(x=-7, y=40)
        entry_number_second.place(x=243, y=40)
        btn_show_res.place(x=103, y=90)

    ##Метод вгоняющий главное окно в вечный цикл
    def _loop_window(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = Window()