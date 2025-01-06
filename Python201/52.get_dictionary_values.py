courses = {
    "js": "JavaScript 101",
    "python": ["Python 101", "Python 201"],
    "html": "HTML 101"
}

#print(courses.get("js","default text in here"))

if courses.get("css",None):
    print("you are enrolled in CSS 101")
else:
    print("you are not enrolled in CSS 101")