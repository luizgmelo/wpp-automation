import pywhatkit as kit
from time import sleep

with open("./numbers.txt") as numbers:
    for number in numbers: 
        kit.sendwhatmsg_instantly(phone_no=number,
                                message="Teste zapzap",
                                tab_close=True)
        sleep(30)