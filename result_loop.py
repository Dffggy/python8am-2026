num=int(input('enter number of students: '))
x=1
students_marks=[]
while x<=num:
    print(f"==========Roll no.: {x} ===========")
    nep=int(input("enter ur marks of nep: "))
    eng=int(input("enter ur marks of nep: "))
    eco=int(input("enter ur marks of nep: "))
    mat=int(input("enter ur marks of nep: "))
    phy=int(input("enter ur marks of nep: "))
    che=int(input("enter ur marks of nep: "))
    total = nep+eng+eco+mat+phy+che
    students_marks,append(total)
    x+=1

for total in students_marks:
    per = total/5
    grade=""
    if per<35 and per>60:
        grade="C"
    elif per<60 and per>80:
        grade="B"
    elif per<80 and per >100:
        grade="A"
    else:
        grade="NG"
    print(f"total: {total} percentage: {per} grade")


#next way
student=[
    {'name': 'Ram', 'marks': [34,65,76,67,56]},
    {'name': 'Ram', 'marks': [34,65,76,67,56]},
    {'name': 'Ram', 'marks': [34,65,76,67,56]},
    {'name': 'Ram', 'marks': [34,65,76,67,56]},
    {'name': 'Ram', 'marks': [34,65,76,67,56]},

]