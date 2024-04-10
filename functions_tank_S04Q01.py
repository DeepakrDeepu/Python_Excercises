def do_action(present,redmark,bluemark):
    if present > redmark:
        print("Raise an alarm to close the valve")
    elif present < bluemark:
        print("Send an SMS to fill liquid to the tank")
    else: 
        print("Do nothing, Since the tank level is in between 20% & 80%")

def get_current_level():
    return float(input("Enter the current tank capacity level:"))

capacity = 900
High = capacity * 0.8
Low = capacity * 0.2
level = get_current_level()
do_action(level,High,Low)
