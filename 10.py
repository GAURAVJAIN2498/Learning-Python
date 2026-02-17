import pywhatkit
def send_message(*mobiles):
    for m in mobiles:
        if m.startswith("91"):
            m = "+" + m
            pywhatkit.sendwhatmsg_instantly(m, "Hello")
            
send_message("9180068389**", "9176119671**")           
