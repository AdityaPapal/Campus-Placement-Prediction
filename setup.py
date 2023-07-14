from tkinter import *
from tkinter import ttk
import joblib
import customtkinter as ct
import numpy as np
from sklearn import *
import tkinter.font as font
import pandas as pd

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

master = ct.CTk()
frame = ct.CTkFrame(master=master)
frame.grid(pady=20, padx=60, sticky="nsew")

appWidth, appHeight = 1182, 739


def show_entry_fields():
    text = clicked.get()
    if text == "Male":
        p1 = 1
    else:
        p1 = 0

    p2 = float(e2.get())
    # text = clicked1.get()
    # if text == "Central":
    #     p3 = 1
    #
    # else:
    #     p3 = 0

    p4 = float(e4.get())
    # text = clicked6.get()
    # if text == "Central":
    #     p5 = 1
    #
    # else:
    #     p5 = 0

    text = clicked2.get()
    if text == "Science":
        p6 = 2

    elif text == "Commerce":
        p6 = 1

    else:
        p6 = 0

    p7 = float(e7.get())
    text = clicked3.get()
    if text == "Sci&Tech":
        p8 = 2

    elif text == "Comm&Mgmt":
        p8 = 1

    else:
        p8 = 0

    text = clicked4.get()
    if text == "Yes":
        p9 = 1

    else:
        p9 = 0

    p10 = float(e10.get())
    text = clicked5.get()
    if text == "Mkt&HR":
        p11 = 1

    else:
        p11 = 0

    p12 = float(e12.get())

    model = joblib.load('model_joblib')
    # new_data = pd.DataFrame({
    #     'gender': p1,
    #     'ssc_p': p2,
    #     # 'ssc_b': p3,
    #     'hsc_p': p4,
    #     # 'hsc_b': p5,
    #     'hsc_s': p6,
    #     'degree_p': p7,
    #     'degree_t': p8,
    #     'workex': p9,
    #     'etest_p': p10,
    #     'specialisation': p11,
    #     'mba_p': p12,
    # }, index=[0])
    new_data = [[p1, p2, p4, p6, p7, p8, p9, p10, p11, p12]]
    result = model.predict(new_data)
    result1 = model.predict_proba(new_data)
    text1 = ""
    if result[0] == 0:
        text1 += "Can't Placed"
    else:
        text1 += f"Placement Probability is {round(result1[0][1], 2) * 100} %"
        # Label(master, text=round(result1[0][1], 2) * 100, font=("Roboto", 15)).grid(row=33)
        # Label(master, text="Percent", font=("Roboto", 15)).grid(row=34)
    return text1


master.title("Create by Aditya Papal")

label = ct.CTkLabel(master=frame, text="Campus Placement Prediction System", font=("Roboto", 25))
label.grid(row=0, column=1, columnspan=2, padx=20, pady=20)

ct.CTkLabel(master=frame, text="Gender", font=("Roboto", 15), ).grid(row=1, padx=12, pady=10, )
ct.CTkLabel(master=frame, text="SSC Grade", font=("Roboto", 15)).grid(row=2,  padx=12, pady=10, )
#ct.CTkLabel(master=frame, text="Board of Education", font=("Roboto", 15)).grid(row=2, column=2,  padx=12, pady=10, )
ct.CTkLabel(master=frame, text="HSC Grade", font=("Roboto", 15)).grid(row=4,  padx=5, pady=5, )
#ct.CTkLabel(master=frame, text="Board of Education", font=("Roboto", 15)).grid(row=4, column=2,    padx=12, pady=10, )
ct.CTkLabel(master=frame, text="Specialization in HSC", font=("Roboto", 15)).grid(row=5, column=2,   padx=12, pady=10,)
ct.CTkLabel(master=frame, text="Degree Percentage", font=("Roboto", 15)).grid(row=5,  padx=12, pady=10, )
ct.CTkLabel(master=frame, text="UG degree education", font=("Roboto", 15)).grid(row=6,  padx=12, pady=10, )
ct.CTkLabel(master=frame, text="Work Experience", font=("Roboto", 15)).grid(row=6, column=2, padx=12, pady=10,)
ct.CTkLabel(master=frame, text="Enter test percentage", font=("Roboto", 15)).grid(row=7, padx=12, pady=10,)
ct.CTkLabel(master=frame, text="Branch Specialization", font=("Roboto", 15)).grid(row=7, column=2,  padx=12, pady=10,  )
ct.CTkLabel(master=frame, text="MBA percentage", font=("Roboto", 15)).grid(row=8, padx=12, pady=10, )

clicked = StringVar()
options = ["Male", "Female"]

# clicked1 = StringVar()
# options1 = ["Central", "Others"]

clicked2 = StringVar()
options2 = ["Science", "Commerce", "Arts"]

clicked3 = StringVar()
options3 = ["Sci&Tech", "Comm&Mgmt", "Others"]

clicked4 = StringVar()
options4 = ["Yes", "No"]

clicked5 = StringVar()
options5 = ["Mkt&HR", "Mky&Fin"]

clicked6 = StringVar()
options6 = ["Central", "Others"]

maleRadioButton = ct.CTkRadioButton(master=frame, text="Male", variable=clicked, value="He is")
maleRadioButton.grid(row=1, column=1, padx=5, pady=5 )
femaleRadioButton = ct.CTkRadioButton(master=frame, text="Female", variable=clicked, value="She is")
femaleRadioButton.grid(row=1, column=2, padx=5, pady=5)

# e2 = Entry(master, bd=3)
e2 = ct.CTkEntry(master=frame, placeholder_text="Grade")
e2.grid(row=2, column=1,padx=5, pady=5)

# e3 = ct.CTkOptionMenu(master=frame, values=["Select", "Central", "Others"])
# e3.grid(row=2, column=3,padx=20, pady=5)

e4 = ct.CTkEntry(master=frame, placeholder_text="Grade")
e4.grid(row=4, column=1, padx=5, pady=5)

# e5 = ct.CTkOptionMenu(master=frame, values=["Select", "Central", "Others"])
# e5.grid(row=4, column=3, padx=5, pady=5)

e6 = ct.CTkOptionMenu(master=frame, values=["Select", "Science", "Commerce", "Arts"])
e6.grid(row=5, column=3,padx=5, pady=5)

e7 = ct.CTkEntry(master=frame, placeholder_text="Grade")
e7.grid(row=5, column=1,padx=5, pady=5)

e8 = ct.CTkOptionMenu(master=frame, values=["Select", "Sci&Tech", "Comm&Mgmt", "Others"])
e8.grid(row=6, column=1,padx=5, pady=5)

e9 = ct.CTkOptionMenu(master=frame, values=["Select", "Yes", "No"])
e9.grid(row=6, column=3,padx=5, pady=5)

e10 = ct.CTkEntry(master=frame, placeholder_text="Grade")
e10.grid(row=7, column=1, padx=5, pady=5)

e11 = ct.CTkOptionMenu(master=frame, values=["Select", "Mkt&HR", "Mky&Fin"])
e11.grid(row=7, column=3,padx=5, pady=5)

e12 = ct.CTkEntry(master=frame, placeholder_text="Grade")
e12.grid(row=8, column=1,padx=5, pady=5)

displayBox = ct.CTkTextbox(master=frame, width=300, height=25)
displayBox.grid(row=10, column=1, columnspan=2,  padx=12, pady=20)


def generateResults():
    displayBox.delete("0.0", "200.0")
    text = show_entry_fields()
    displayBox.insert("0.0", text)


ct.CTkButton(master=frame, text="Generate Results"
             , command=generateResults).grid(row=9, column=1, columnspan=2,  padx=12, pady=10)

master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

master.mainloop()
