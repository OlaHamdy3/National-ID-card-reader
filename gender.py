def gen(id):
    genderID = id[12:13]
    if(int(genderID)%2 == 0):
        gender="أنثى"
    else:
        gender="ذكر"
    return gender
