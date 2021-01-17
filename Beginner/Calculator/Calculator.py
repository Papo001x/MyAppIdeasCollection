# Calculator

# Tier: 1-Beginner

# Calculators are not only one of the most useful tools available, but they are also a great way to understand UI and event processing in an application. In this problem you will create a calculator that supports basic arithmetic calculations on integers.

# The styling is up to you so use your imagination and get creative! You might also find it worth your time to experiment with the calculator app on your mobile device to better understand basic functionality and edge cases.
# Constraints

# User Stories

#     User can see a display showing the current number entered or the result of the last operation.
#     User can see an entry pad containing buttons for the digits 0-9, operations - '+', '-', '/', and '=', a 'C' button (for clear), and an 'AC' button (for clear all).
#     User can enter numbers as sequences up to 8 digits long by clicking on digits in the entry pad. Entry of any digits more than 8 will be ignored.
#     User can click on an operation button to display the result of that operation on:
#         the result of the preceding operation and the last number entered OR
#         the last two numbers entered OR
#         the last number entered
#     User can click the 'C' button to clear the last number or the last operation. If the users last entry was an operation the display will be updated to the value that preceded it.
#     User can click the 'AC' button to clear all internal work areas and to set the display to 0.
#     User can see 'ERR' displayed if any operation would exceed the 8 digit maximum.

from tkinter import * 

i=0

def get_numbers(n):
    global i
    lcd.insert(i,n)
    i+=1
    
def get_operador(operador):
    global i
    lcd.insert(i,operador)
    i+=operador
    
def clear_lcd():
    lcd.delete(0,END)
    
def clear_index():
    lcd_estado = lcd.get()
    if len(lcd_estado):
        lcd_nuevo_estado = lcd_estado[:-1]
        clear_lcd()
        lcd.insert(0,lcd_nuevo_estado)
    else:
        clear_lcd()
        lcd.insert(0,'Error')   
     
def calculo():
    operacion=lcd.get()
    resultado= eval(operacion)
    lcd.delete(0,END)
    lcd.insert(0,resultado)

window = Tk()
window.title("Calculadora")
lcd=Entry(window,bg="black",fg="white",font=('Helvetica Neue',20))
lcd.grid(column=0,row=0,columnspan=4,sticky=N+S+W+E)
botonCA=Button(window,text='AC',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:clear_lcd())
botonCA.grid(column=0,row=1,sticky=N+S+W+E)
botondiv=Button(window,text='÷',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_operador('/'))
botondiv.grid(column=1,row=1,sticky=N+S+W+E)
botonmul=Button(window,text='x',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_operador('*'))
botonmul.grid(column=2,row=1,sticky=N+S+W+E)
botondel=Button(window,text='«',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:clear_index())
botondel.grid(column=3,row=1,sticky=N+S+W+E)
boton7=Button(window,text='7',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('7'))
boton7.grid(column=0,row=2,sticky=N+S+W+E)
boton8=Button(window,text='8',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('8'))
boton8.grid(column=1,row=2,sticky=N+S+W+E)
boton9=Button(window,text='9',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('9'))
boton9.grid(column=2,row=2,sticky=N+S+W+E)
botonmenos=Button(window,text='-',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_operador('-'))
botonmenos.grid(column=3,row=2,sticky=N+S+W+E)
boton4=Button(window,text='4',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('4'))
boton4.grid(column=0,row=3,sticky=N+S+W+E)
boton5=Button(window,text='5',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('5'))
boton5.grid(column=1,row=3,sticky=N+S+W+E)
boton6=Button(window,text='6',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('6'))
boton6.grid(column=2,row=3,sticky=N+S+W+E)
botonmas=Button(window,text='+',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_operador('+'))
botonmas.grid(column=3,row=3,sticky=N+S+W+E)
boton1=Button(window,text='1',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('1'))
boton1.grid(column=0,row=4,sticky=N+S+W+E)
boton2=Button(window,text='2',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('2'))
boton2.grid(column=1,row=4,sticky=N+S+W+E)
boton3=Button(window,text='3',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('3'))
boton3.grid(column=2,row=4,sticky=N+S+W+E)
botonigual=Button(window,text='=',bg="blue",fg="white",font=('Helvetica Neue',15),command=lambda:calculo())
botonigual.grid(column=3,row=4,rowspan=2,sticky=N+S+W+E)
botoncero=Button(window,text='0',bg="grey",fg="white",font=('Helvetica Neue',15),command=lambda:get_numbers('0'))
botoncero.grid(column=0,row=5,columnspan=3,sticky=N+S+W+E)


for i in range(4):
    window.columnconfigure(i, weight=1, minsize=75)
for i in range(6):
    window.rowconfigure(i, weight=1, minsize=50) 

window.mainloop()