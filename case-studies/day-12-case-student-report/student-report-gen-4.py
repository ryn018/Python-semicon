import json
with open(r'C:\Users\292905\Desktop\Python semicon\case-studies\day-12-case-student-report\student.json') as f:
  data = json.load(f)

class_dict = {x['regid'] : x for x in data }
for regid in class_dict.keys():
    sum_of_subjects = float(class_dict[regid]['phy']) + float(class_dict[regid]['chem']) + \
                      float(class_dict[regid]['math']) + float(class_dict[regid]['bio'])
    class_dict[regid]['avg'] = sum_of_subjects / 4

avg_list = set([class_dict[regid]['avg'] for regid in class_dict.keys()])
avgs = list(avg_list)
avgs.sort(reverse=True)
for regid in class_dict.keys():
    
    class_dict[regid]['rank'] = avgs.index(class_dict[regid]['avg']) + 1 


with open(r'C:\Users\292905\Desktop\Python semicon\case-studies\day-12-case-student-report\student-report.json', 'w') as json_file:
    json.dump(class_dict, json_file, indent=4)
