# Step 1
# Read the content

path = r"C:\Users\292905\Desktop\Python semicon\case-studies\day-12-case-student-report\students.csv"
f = open(path)
content = f.readlines()
f.close()

print("INFO -> step 1", content)

# Step 2
# Process the content and store in a data structure
# What data structure will be good here? Sanjeev -> Dictionary
# student_dict -> class_dict

class_dict = {}
rank_dict = {}
columns = [item.strip() for item in content[0].split(',')] # Keys of the student dictionary
for dataitem in content[1:]:
    values = [item.strip() for item in dataitem.split(',')] # Values for the student dictionary
    student_dict = dict(zip(columns, values)) # Zipping keys and values to form the student dictionary
    class_dict[student_dict['regid']] = student_dict # Adding student dictionery to class dictionary


print("\n" + "-"*100)
print("INFO -> step 2 \n", class_dict)


# Step 3
# Calculate the average
print("***********************444")
highest = 0
for item in class_dict:
    avg = (
    int(class_dict[item]['phy']) +
    int(class_dict[item]['chem']) +
    int(class_dict[item]['math']) +
    int(class_dict[item]['bio'])
) / 4  

    # avg = (class_dict[item]['phy'] + class_dict[item]['chem'] + class_dict[item]['math'] + class_dict[item]['bio'])/4
    class_dict[item]['avg'] = avg
    # sorted(class_dict[item][avg])
    rank_dict[class_dict[item]['name']] = avg

# print(class_dict[item])
# print(rank_dict)
sorted_rank = dict(sorted(rank_dict.items(), key=lambda item: item[1],reverse=True))
print(sorted_rank)
num = 1
for item in sorted_rank:
    
    sorted_rank[item] =  num
    num += 1
print(sorted_rank)



print("\n" + "-"*100)
print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)

# Step 4
# Calculate the rank






print("\n" + "-"*100)
print("INFO -> step 4 -> Class dictionary after ranks updated\n", class_dict)

# Step 5
# Display the report