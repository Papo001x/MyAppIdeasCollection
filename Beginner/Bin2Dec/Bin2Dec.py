#Binary-to-Decimal number converter
# Tier: 1-Beginner

# Binary is the number system all digital computers are based on. Therefore it's important for developers to understand binary, or base 2, mathematics. The purpose of Bin2Dec is to provide practice and understanding of how binary calculations.

# Bin2Dec allows the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then displays its decimal equivalent.

# This challenge requires that the developer implementing it follow these constraints:

#     Arrays may not be used to contain the binary digits entered by the user
#     Determining the decimal equivalent of a particular binary digit in the sequence must be calculated using a single mathematical function, for example the natural logarithm. It's up to you to figure out which function to use.
# User Stories

#     User can enter up to 8 binary digits in one input field
#     User must be notified if anything other than a 0 or 1 was entered
#     User views the results in a single output field containing the decimal (base 10) equivalent of the binary number that was entered

# Bonus features

#     User can enter a variable number of binary digits
from tkinter import * 
from tkinter import messagebox

def conver_bin_dec():
    numero=txt.get()
    contador=0
    banderadealerta=False
    for test in numero:
        variabletest=int(test)
        contador=contador+1
        if not 0<=variabletest<= 1:
            banderadealerta=True
    if banderadealerta==True:
        messagebox.showinfo('Alerta', 'Solo 0 y 1')
    if contador>8:
        messagebox.showinfo('Alerta', 'Un numero binario no mayor a 8 digitos')
    Valorfinal=int(numero,2)
    label5.configure(text=Valorfinal)
window = Tk()
window.title("Bin2Dec")

label1=Label(window,text='Bin2Dec',font=('Helvetica Neue',20))
label1.grid(column=0,row=0)
label2=Label(window,text='Convertidor de binario a decimal',font='Helvetica')
label2.grid(column=0,row=1)
label3=Label(window,text='Binario: ',font='Helvetica')
label3.grid(column=0,row=2)
txt=Entry(window,width=8)
txt.grid(column=1,row=2)
label4=Label(window,text='Decimal: ',font='Helvetica')
label4.grid(column=0,row=3)
label5=Label(window,text='',font='Helvetica')
label5.grid(column=1,row=3)
boton=Button(window,text='Convertir',command=conver_bin_dec)
boton.grid(column=1,row=4)




window.mainloop()
