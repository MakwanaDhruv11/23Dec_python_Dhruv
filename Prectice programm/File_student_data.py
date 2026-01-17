fl = open("student_data.txt","a")

num_stu = int(input("how many student do you want: "))

for i in range(num_stu):
    stid = input("enter a ID :")
    stnm = input("enter a Name :")
    stct = input("enter a City :")
    fl.write(f"ID:{stid}/nName:{stnm}\nCity:{stct}")
    fl.write("\n=================\n")
