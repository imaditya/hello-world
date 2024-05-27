import pyfiglet

user_text = input("Enter the text you want to convert to ASCII art: ")
ascii_art = pyfiglet.figlet_format(user_text)
print(ascii_art)
