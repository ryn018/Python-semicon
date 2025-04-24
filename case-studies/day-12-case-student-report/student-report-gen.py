# Step 1
"""
f = open(r"C:\Users\292905\Desktop\Python semicon\case-studies\day-12-case-student-report\students.csv")
content = f.readline().split(",")
for i in range(11):
    content = f.readline().split(',')
    print(f"{content[2]} | {content[0]} | {content[1]} | {content[3]} | {content[4]} | {content[5]} | {content[6]} | {content[7]}")

    # print(content)

"""
# Step 1
# Read the content
file_path = r"C:\Users\292905\Desktop\Python semicon\case-studies\day-12-case-student-report\students.csv"

with open(file_path, "r") as f:
    content = f.readlines()


print("INFO -> step 1", content)

# Step 2
# Process the content and store in a data structure
# What data structure will be good here? Sanjeev -> Dictionary
# student_dict -> class_dict

class_dict = {}
columns = [item.strip() for item in content[0].split(',')] # Keys of the student dictionary
for dataitem in content[1:]:
    values = [item.strip() for item in dataitem.split(',')] # Values for the student dictionary
    student_dict = dict(zip(columns, values)) # Zipping keys and values to form the student dictionary
    class_dict[student_dict['regid']] = student_dict # Adding student dictionery to class dictionary


print(class_dict)
print("\n" + "-"*100)
print("INFO -> step 2 \n", class_dict)

# Step 3
# Calculate the average


print("\n" + "-"*100)
print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)

# Step 4
# Calculate the rank


print("\n" + "-"*100)
print("INFO -> step 4 -> Class dictionary after ranks updated\n", class_dict)

# Step 5
# Display the report