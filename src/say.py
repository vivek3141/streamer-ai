from gtts import gTTS
import os
import pyttsx3

engine = pyttsx3.init()
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
    # gTTS(to_say).save("said.mp3")
    # os.system("mpg123 said.mp3")
    engine.say(to_say)
    engine.runAndWait()
