print("===== Student Management System =====")
st_name = None
st_age = None
st_marks = None
user_input = 0
while user_input != 3:
    print("Enter 1 to add student record")
    print("Enter 2 to view student record")
    print("Enter 3 to Exit")
    user_input = int(input("Enter a value"))
    if user_input == 1:
        st_name = input("Enter stdent's name ")
        st_age = int(input("Enter your age"))
        st_marks = int(input("Enter your marks"))
        print("Student added sucsessfully")
    elif user_input == 2:
        if st_name is None: # because even one value is misiing it needs to enter data
            print("No record found")
        else:
            print(f"Name : {st_name} \n age : {st_age} \n Marks : {st_marks}") 
    elif user_input == 3:
        print("Thank you for using system")
        break
    else:
        print("You entered invalid option, please select correct option")
