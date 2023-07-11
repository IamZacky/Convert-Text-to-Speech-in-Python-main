from tkinter import *
from gtts import gTTS
import os

def Text_to_speech():
    Message = entry_field.get()
    if Message:
        try:
            speech = gTTS(text=Message)
            speech.save('TextToSpeech.mp3')
            os.system('start TextToSpeech.mp3')
            status_message.config(text='Task is done', fg='green')
        except Exception as e:
            status_message.config(text='Something went wrong', fg='red')
    else:
        status_message.config(text='No text input', fg='red')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
    status_message.config(text='')

root = Tk()

# Calculate the position to center the window
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f'{window_width}x{window_height}+{x}+{y}')  # Set window dimensions and position


root.resizable(0, 0)
root.title('TextToSpeech')
root.config(bg='#a593e0')  # Set background color to a purple shade

heading = Label(root, text='TEXT TO SPEECH', font='Arial 20 bold', bg='#a593e0', fg='white')  # Set heading color to white
heading.pack(pady=10)

label_text = Label(root, text='Enter Text:', font='Arial 15', bg='#a593e0', fg='white')  # Set label color to white
label_text.pack(pady=5)

Msg = StringVar()
entry_field = Entry(root, textvariable=Msg, width=50)
entry_field.pack(pady=10)

play_button = Button(root, text='PLAY', font='Arial 15 bold', command=Text_to_speech, bg='#bc7cf7', fg='white')  # Set button color to a lighter purple shade and text color to white
play_button.pack()

reset_button = Button(root, text='RESET', font='Arial 15 bold', command=Reset, bg='#bc7cf7', fg='white')  # Set button color to a lighter purple shade and text color to white
reset_button.pack(pady=10)

exit_button = Button(root, text='EXIT', font='Arial 15 bold', command=Exit, bg='#bc7cf7', fg='white')  # Set button color to a lighter purple shade and text color to white
exit_button.pack(pady=10)

status_message = Label(root, text='', font='Arial 12', bg='#a593e0', fg='white')  # Set label color to white
status_message.pack(pady=10)

root.mainloop()