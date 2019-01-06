from gtts import gTTS
import os
from time import sleep
import os
import pyglet

tts = gTTS(text='Hello World', lang='en')
filename = '/tmp/temp.mp3'


open("say.txt", "w").write("")
while True:
    with open("say.txt") as f:
        read = f.read()
    if read == "":
        continue
    to_say = read.replace("\n", "")
    with open("say.txt", "w") as f:
        with open("say.txt", "r") as file:
            f.write(file.read().replace(read, ""))
    tts = gTTS(to_say)
    tts.save(filename)

    #music = pyglet.media.load(filename, streaming=False)
    #music.play()

    #sleep(music.duration)
    #os.remove(filename)
    os.system(f"mpg123 {filename}")
    #engine.say(to_say)
    #engine.runAndWait()
