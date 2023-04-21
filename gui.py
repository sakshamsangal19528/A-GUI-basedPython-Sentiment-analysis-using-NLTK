from tkinter import *
import os
from tkinter import filedialog

window = Tk()


def openfile():
    file = filedialog.askopenfile(filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    if file:
        filepath = os.path.abspath(file.name)
        window.create_text(400, 490, text="The File is located at : " + str(filepath), font='Aerial 11')
        f = open("C:\\Users\\Beta enviornment\\Desktop\\sem6 project\\path.txt", 'w')
        f.write(filepath)


def run():
    os.startfile('C:\\Users\\Beta enviornment\\Desktop\\sem6 project\\script\\sentiment.py')


window.title('Sentiment analysis')

window = Canvas(window, bg="light grey", width=850, height=650)

window.create_text(425, 50, text="INSTRUCTIONS-", fill="black", font='Times 15')

window.create_text(425, 90, text="make sure your CSV file has the same format as shown below and has similar data .",
                   fill="black", font='Times 15')

window.create_text(335, 450, text="select your CSV file   :", fill="black", font='Times 15')

btn = Button(window, text='    upload    ', command=openfile, font='Times 12')
btn.place(x=450, y=435)

btn = Button(window, text='      START       ', command=run, font='Times 13')
btn.place(x=360, y=520)

window.pack()
image = PhotoImage(file='C:\\Users\\Beta enviornment\\Desktop\\sem6 project\\gui\\gui images\\Capture.PNG')
window.create_image(430, 250, anchor=CENTER, image=image)


window.mainloop()
