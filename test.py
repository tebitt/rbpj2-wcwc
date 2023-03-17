import os
from gtts import gTTS
import time

line1 = 'The lights will turn red in'
line2 = 'three'
line3 = 'two'
line4 = 'one'
line1_mp3 = gTTS(text=line1, lang='en', slow=False)
line1_mp3.save("line1.mp3")
line2_mp3 = gTTS(text=line2, lang='en', slow=False)
line2_mp3.save("line2.mp3")
line3_mp3 = gTTS(text=line3, lang='en', slow=False)
line3_mp3.save("line3.mp3")
line4_mp3 = gTTS(text=line4, lang='en', slow=False)
line4_mp3.save("line4.mp3")
delaynum = 10

i = delaynum
while i >= 0:
    time.sleep(1)
    if(i == 5):
        os.system("open line1.mp3")
    elif(i==3):
        os.system("open line2.mp3")
    elif(i==2):
        os.system("open line3.mp3")
    elif(i==1):
        os.system("open line4.mp3")
    print(i)
    i -= 1;