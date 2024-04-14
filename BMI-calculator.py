from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Body Mass Index : BMI')
GUI.geometry('500x500')


L1 = Label(GUI,text='กรุณากรอกน้ำหนักตัว(kg.)',font=(None,16))
L1.pack(pady=20)

v_weight = StringVar() # ตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_weight, font=(None,16))
E1.pack()

L2 = Label(GUI,text='กรุณากรอกส่วนสูง(cm.)',font=(None,16))
L2.pack(pady=20)

v_height = StringVar() # ตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E2 = ttk.Entry(GUI, textvariable=v_height, font=(None,16))
E2.pack()

def BMI():
    we = int(v_weight.get())
    he = int(v_height.get())
    he = he/100
    bmi = we / (he*he)
    messagebox.showinfo('BMI','ค่าดัชนีมวลกายของคุณ : {}'.format(bmi))


    if bmi > 35.0:
        messagebox.showinfo('BMI','คุณอยู่ในเกณฑ์ : อ้วนมากผิดปกติ')
    elif bmi>30.0 and bmi<35.0:
        messagebox.showinfo('BMI','คุณอยู่ในเกณฑ์ : อ้วน')
    elif bmi>25.0 and bmi<30.0:
        messagebox.showinfo('BMI','คุณอยู่ในเกณฑ์ : เริ่มอ้วน')
    elif bmi>18.5 and bmi<25.0:
        messagebox.showinfo('BMI','คุณอยู่ในเกณฑ์ : น้ำหนักปกติ-น้ำหนักเหมาะสม')
    else :
        messagebox.showinfo('BMI','คุณอยู่ในเกณฑ์ : ผอมเกินไป - น้ำหนักน้อยกว่าปกติ')
 

B = ttk.Button(GUI, text='คำนวน ⭣',command=BMI)
B.pack(ipadx=15,ipady=10,pady=20)


GUI.mainloop()