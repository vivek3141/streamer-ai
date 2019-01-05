from gtts import gTTS
import os

open("say.txt", "w").write("")
while True:
    read = open("say.txt").read()
    if read == "":
        continue
    to_say = read.replace("\n", "")
    open("say.txt", "w").write(open("say.txt", "r").read().replace(read, ""))
    gTTS(to_say).save("said.mp3")
    os.system("mpg123 said.mp3")
