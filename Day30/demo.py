# #FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'
# try:
#     file =  open("a_file.txt")
#     file.read()
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file =  open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_messege:
#     print(f"The key does {error_messege} not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This an error that i made up")
#


# #KeyError: 'non_existant_key'
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existant_key"]

# #TTypeError: can only concatenate str (not "int") to str
# text = "abc"
# print(text +5)



height = float(input("Enter height in meters: "))
weight = int(input("Enter weight in pounds: "))

if height>3:
    raise ValueError("human height should not be over than 3m")

bmi = weight / (height * height)
print(f"BMI is {bmi:.2f}")