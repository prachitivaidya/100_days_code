#function with output


def format_name(fname, lname):
    #strname.title() capitalize string all the words
    fname.lower()
    lname.lower()
    fname = fname.capitalize()
    lname = lname.capitalize()
    return f"Your name is {fname} {lname}!"

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

output =format_name(fname, lname)
print(output)