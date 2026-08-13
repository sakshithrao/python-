## create a new file


# file = open("newfile.txt", "x")

# file.write("Hello")

# file.close()




## opening a file using write

# file = open("data.txt", "w")

# file.write("Hello Python")

# file.close()





## opening a file using append

# file = open("data.txt", "a")
# file.write("\nHello Python")
# file.close()




## opening a file using read

# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()

## open a file in read mode and handle the exception if the file is not found

# try:
#     file = open("data.txt", "r")
#     print(file.read())
#     file.close()

# except FileNotFoundError:
#     print("The requested file was not found")



## add 1 to n numbers in output.txt file inside try and except block and finally block

# file = None
# try:
#     file = open("output.txt", "w")
#     n = 10
#     for i in range(1, n + 1):
#         file.write(str(i) + "\n")
#     file.close()
# except FileNotFoundError:
#     print("The requested file was not found")
# finally:
#     if file is not None:
#         file.close()




#opening a file using with statement using try and except block and finally block

# import csv

# try:
#     with open("output.txt", newline="", mode="w") as file:
#         writer =csv.writer(file)
#         header = ["Name", "Age", "City"]
#         writer.writerow(header)
#         data = [["John", 25, "New York"],
#                 ["Alice", 30, "Los Angeles"],
#                 ["Bob", 22, "Chicago"]]
#         writer.writerows(data)
# except FileNotFoundError:
#     print("The requested file was not found")

    
    
    
# reading csv file content


# import csv
# try:
#     with open("output.txt", newline="", mode="r") as file:
#         reader = csv.reader(file)
#         print(list(reader))
#         for row in reader:
#             print(row)
#             print("content added successfully")
# except Exception as e:
#     print(f"An error occurred: {e}")


#updating the content of csv output.txt file using try and except block and finally block


# import csv

# try:
#     # Read the file
#     with open("students.csv", "r", newline="") as file:
#         reader = csv.reader(file)
#         data = list(reader)

#     name = input("Enter student name: ")
#     new_phone = input("Enter new phone number: ")

#     found = False

#     # Search for student
#     for row in data:

#         if row[0] == name:
#             row[2] = new_phone
#             found = True
#             break

#     # Write updated data
#     if found:
#         with open("students.csv", "w", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerows(data)

#         print("Phone number updated successfully")

#     else:
#         print("Student not found")

# except FileNotFoundError:
#     print("Student file does not exist")

# except Exception as e:
#     print("Error:", e)



#creating a csv file and adding student details using try and except block and finally block


# import csv

# try:
#     with open("students.csv", "w", newline="") as file:

#         writer = csv.writer(file)

#         # Header
#         writer.writerow(["Name", "Age", "Phone", "Marks"])

#         # Student details
#         writer.writerow(["Sakshith", 23, "9876543210", 85])
#         writer.writerow(["Rahul", 22, "9123456780", 78])
#         writer.writerow(["Priya", 21, "9988776655", 92])

#     print("Student details added successfully")

# except Exception as e:
#     print("Error:", e)
    



# to print the content of students.csvon the console using try and except block and finally block


# import csv


# with open("students.csv", "r", newline="") as file:

#     reader = csv.reader(file)

#     for row in reader:
#         print(row)
        
        
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Name", "Age", "Phone", "Marks"])

    # Student details
    writer.writerow(["Sakshith", 22, "8520896301", 100])
    writer.writerow(["Rahul", 22, "9123456780", 78])
    writer.writerow(["Priya", 21, "9988776655", 92])
    writer.writerow(["Anil", 23, "9000012345", 88])

print("students.csv created successfully")


import csv

try:
    # Read students.csv
    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Get input from user
    name = input("Enter student name: ")
    new_phone = input("Enter new phone number: ")

    found = False

    # Find student and update phone number
    for row in data:
        if row[0] == name:
            row[2] = new_phone
            found = True
            break

    # Write updated data
    if found:
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("Phone number updated successfully")

    else:
        print("Student not found")

except FileNotFoundError:
    print("students.csv file not found")

except Exception as e:
    print("Error:", e)