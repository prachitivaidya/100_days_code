#function with output


def format_name(fname, lname):
    #strname.title() capitalize string all the words
    #these three double quotes are used to document the functions
    """"this function takes first and last name and format it to make first letter in each wors capitilize"""
    fname.lower()
    lname.lower()
    fname = fname.capitalize()
    lname = lname.capitalize()
    return f"Your name is {fname} {lname}!"

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

output =format_name(fname, lname)
print(output)
