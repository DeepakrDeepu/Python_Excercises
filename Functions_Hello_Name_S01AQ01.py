
# To prompt for user’s name and then wish the user by saying Hello followed by his name


def get_username():
    return input("Enter your name: ")
    
    

def say_hello(user):
    print("Hello",user,"!!")

def main():
    name = get_username()
    say_hello(name)
    
main()
