def student_marks ():
    try:
        s = str(input("Which student's marks do you want to amend ?"))
        m = int(input("Enter the index you want to amend"))
        marks = int(input("How much marks do you want to award ?"))
        student_dict[s][m] = marks  # Changing the value from 88 to 90
        # student_dict["DEF"] = [78,76,89,90]
        return 1

    except:
        print("Your choice is invalid")
        return 0

    finally:
        print("Finally Block :: Will run irrespective of error")
        print("Marks list")
        for name, grades in student_dict.items():
            print(f"Name: {name}, Grades: {grades}")

student_dict = {"ABC": [80, 85, 90, 78],
                "DEF": [78, 76, 89, 90],
                "RTI": [75, 89, 98, 100]}

print(type(student_dict))
print(len(student_dict))

x= student_marks()
print("Marks list")
# for name, grades in student_dict.items():
#     print(f"Name: {name}, Grades: {grades}")

    # for name, grades in student_dict.items():
    #     print(f"Name: {name}, Grades: {grades}", end='\n')

print("Thanks for using the application")

# print ("After Change")
# for name, grades in student_dict.items():
#         print (f"Name: {name}, Grades: {grades}", end='\n')
# print (student_dict)