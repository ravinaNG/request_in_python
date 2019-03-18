import requests 
base_url = "http://saral.navgurukul.org/api/courses"
request = requests.get(base_url)
responce = request.json()
# print (responce)
data = responce['availableCourses']
# print (data)
count = 0
course_id_list = []
while(count < len(data)):
    course_id_list.append(data[count]['id'])
    course_name=data[count]['name']
    # course_id_list.append(key_value)
    print (count, course_name)
    count = count + 1
