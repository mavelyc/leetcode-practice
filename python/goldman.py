#hackerrank Goldman Sachs question

def latestStudent(attendanceData):
    average_late = []
    students = []
    currdate = attendanceData[0][0]
    total = 0
    div = 0

    for i in attendanceData:
        if (i[0] == currdate):
            total += int(i[3]) - int(i[2])
            div += 1
        else:
            ave = total/div
            tmp = [currdate, ave]
            average_late.append(tmp)
            currdate = i[0]
            total = int(i[3]) - int(i[2])
            div = 1
    ave = total/div
    tmp = [currdate, ave]
    average_late.append(tmp)

    count = 0

    for j in attendanceData:
        if (j[0] == average_late[count][0]):
            rel = int(j[3]) - int(j[2]) - average_late[count][1]
            if rel < 0: rel = 0
            tmp = [j[1],rel]
            students.append(tmp)
        else:
            count+=1
            rel = int(j[3]) - int(j[2]) - average_late[count][1]
            if rel < 0: rel = 0
            tmp = [j[1],rel]
            students.append(tmp)
        #print average_late[count][1], j[1]

    print average_late
    print students
    bar = students[0]
    count1 = 0
    for l in students:
        if (l[1] > bar[1]):
            bar = students[count1]
        count1+=1

    print bar[0]



yo = [["06-22","Chuck","540","540"],["06-23","Debby","540","555"],["06-23","Chuck","540","540"]]
latestStudent(yo)

