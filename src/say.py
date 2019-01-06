from gtts import gTTS
import os

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

    os.system(f"mpg123 {filename}")
