from tkinter import * # загружает tkinter из библиотеки

def cAction (): # функция - подпрограмма для кнопки рассчета
    try:
        m = float (m_e.get())
        h = float (h_e.get())
        
    except ValueError:
        result.config(text="Invalid input")
        result_2.config(text="")
        return
    
    h = h/100
    bmi = (m/(h**2))
    bmi = round(bmi, 1)
    result.config (text = bmi)

    if bmi <= 18.5:
        result_2.config (text = 'Underweight (BMI = 18.5 or less)', fg = 'blue')
    elif bmi >= 30:
        result_2.config (text = 'Obesity (BMI = 30 or more)', fg = 'red')
    elif bmi >= 25 and bmi < 30:
        result_2.config (text = 'Overweight (BMI 25-29.9)', fg = 'orange2')
    else:
        result_2.config (text = 'Normal weight (BMI 18.5 - 24.9)', fg = 'black')


        
app = Tk() # создает окно tkiner
app.geometry ('440x440') # задаем размер окна
app.title ('BMI Calculator') # задаем заголовок окну

label_0 = Label (app, text = 'BMI Calculator', background = 'spring green')
label_1 = Label (app, text = 'Note: BMI is a simplified indicator.')
label_2 = Label (app, text = 'Body composition analysis is more accurate.')
label_3 = Label (app, text = ' ')
label_0.pack()
label_1.pack()
label_2.pack()
label_3.pack()

m_l = Label (app, text = 'Weight (kg):')
m_e = Entry (app, width = 10) # поле ввода
h_l = Label (app, text = 'Height (cm):')
h_e = Entry (app, width = 10)
m_l.pack() # запаковать нужно обязательно, иначе не отобразится!
m_e.pack()
h_l.pack()
h_e.pack()

button_C = Button (app, text = 'Calculate', command = cAction, fg = 'blue')
button_C.pack()

result = Label (app, text = 'Your result:', width = 440, bg = 'sky blue')
result.config()
result. pack()

result_2 = Label (app, text = ' ', width = 440)
result_2.config()
result_2.pack()

# BMI (ИМТ) = кг/м2

