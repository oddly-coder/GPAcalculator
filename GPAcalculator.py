#  GPA calculator to calculate your GPA with ease
total_course_unit=0
points=[]
print("please type 'done' when you've inputted all courses\n")
while True: 
    value=input("\n type a course\n")
    if value==("done"):
        total_point=sum(points)
        result=int(total_point)/(total_course_unit)
        print("\n your GPA is")
        print(result)
        break 
    else:
        value0=int(input("\n what's the course unit? \n"))
        total_course_unit+=(value0)
        value1=input("\n type your grade in the course in uppercase\n")
        if value1==("A"):
            point=5*(value0)
            points.append(point)
        elif value1==("B"):
            point=4*(value0)
            points.append(point)
        elif value1==("C"):
            point=3*(value0)
            points.append(point)
        elif value1==("D"):
            point=2*(value0)
            points.append(point)
        elif value1==("E"):
            point=1*(value0)
            points.append(point)
        elif value1==("F"):
            point=0*(value0)
            points.append(point)
        else:
            print("grade error")
