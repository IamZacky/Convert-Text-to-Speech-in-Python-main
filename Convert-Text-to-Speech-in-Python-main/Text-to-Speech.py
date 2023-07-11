from tkinter import *
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def modify_audio_speed(audio, speed):
    return audio.speedup(playback_speed=speed)

def modify_audio_pitch(audio, pitch):
    return audio._spawn(audio.raw_data, overrides={'frame_rate': int(audio.frame_rate * pitch)})


def Text_to_speech():
    Message = entry_field.get()
    if Message:
        try:
            # Modify the text to increase speed and pitch
            modified_text = Message + '!'  # Add exclamation mark to increase enthusiasm
            output_format = format_var.get().lower()
            
            if output_format == 'mp3':
                speech = gTTS(text=modified_text, lang='en', slow=False)
                output_file = 'TextToSpeech.mp3'
            elif output_format == 'wav':
                speech = gTTS(text=modified_text, lang='en', slow=False)
                output_file = 'TextToSpeech.wav'
            elif output_format == 'aac':
                speech = gTTS(text=modified_text, lang='en', slow=False)
                output_file = 'TextToSpeech.aac'
            else:
                raise ValueError('Invalid output format')
            
            speech.save(output_file)

            # Open the saved audio file using pydub
            audio = AudioSegment.from_file(output_file, format=output_format)

            # Get the speed and pitch values from the scrollbars
            speed = speed_scale.get()
            pitch = pitch_scale.get()

            # Modify the speed and pitch of the audio
            modified_audio = modify_audio_speed(audio, speed)
            modified_audio = modify_audio_pitch(modified_audio, pitch)

            # Export the modified audio to the output file
            modified_audio.export(output_file, format=output_format)

            os.system(f'start {output_file}')
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
window_height = 650
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

format_var = StringVar()
format_var.set('MP3')  # Set default output format to MP3

format_label = Label(root, text='Output Format:', font='Arial 15', bg='#a593e0', fg='white')
format_label.pack(pady=5)

format_dropdown = OptionMenu(root, format_var, 'MP3', 'WAV', 'AAC')
format_dropdown.pack(pady=5)

# Add scrollbars for adjusting speed and pitch
speed_label = Label(root, text='Speed:', font='Arial 12', bg='#a593e0', fg='white')
speed_label.pack(pady=10)

speed_scale = Scale(root, from_=1.1, to=2.0, resolution=0.1, orient=HORIZONTAL, length=200)
speed_scale.set(1.0)  # Set default speed value
speed_scale.pack(pady=10)

pitch_label = Label(root, text='Pitch:', font='Arial 12', bg='#a593e0', fg='white')
pitch_label.pack(pady=10)

pitch_scale = Scale(root, from_=0.7, to=1.3, resolution=0.1, orient=HORIZONTAL, length=200)
pitch_scale.set(1.0)  # Set default pitch value
pitch_scale.pack(pady=10)

play_button = Button(root, text='PLAY', font='Arial 15 bold', command=Text_to_speech, bg='#bc7cf7', fg='white')  # Set button color to a lighter purple shade and text color to white
play_button.pack(pady=10)

reset_button = Button(root, text='RESET', font='Arial 15 bold', command=Reset, bg='#bc7cf7', fg='white')  # Set button color to a lighter purple shade and text color to white
reset_button.pack(pady=10)

exit_button = Button(root, text='EXIT', font='Arial 15 bold', command=Exit, bg='#bc7cf7', fg='white')  # Set button color to a lighter purple shade and text color to white
exit_button.pack(pady=10)

status_message = Label(root, text='', font='Arial 12', bg='#a593e0', fg='white')  # Set label color to white
status_message.pack(pady=10)

root.mainloop()
