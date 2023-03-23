import json

def ReadFromDB(table_name):
  f = open("db/"+table_name) 
  lines = f.readlines()
  f.close()
  datas = []
  for line in lines:
    datas.append(json.loads(line))
  return datas


def WriteToDB(datas, table_name):
  f = open("db/" + table_name, "w")
  for data in datas:
    json_data = json.dumps(data)
    f.write(json_data + "\n")
  f.close()


def TeacherTest():
  datas = []

  data = {}
  data["id"] = 1000
  data["name"] = "yby"
  data["desc"] = "this is yby"
  data["booking"] = []
  data["booking"].append(1)
  data["booking"].append(2)
  datas.append(data)

  data = {}
  data["id"] = 1001
  data["name"] = "jdb"
  data["desc"] = "this is jdb"
  data["booking"] = []
  data["booking"].append(3)
  data["booking"].append(4)
  datas.append(data)

  WriteToDB(datas, "teacher.db")
  print(ReadFromDB("teacher.db"))


def StudentTest():
  datas = []

  data = {}
  data["id"] = 10001
  data["name"] = "10001"
  data["tel"] = 1323232321
  data["booking"] = []
  data["booking"].append(1)
  datas.append(data)

  data = {}
  data["id"] = 10002
  data["name"] = "10002"
  data["tel"] = 1323231002
  data["booking"] = []
  data["booking"].append(2)
  datas.append(data)

  data = {}
  data["id"] = 10003
  data["name"] = "10003"
  data["tel"] = 1323231003
  data["booking"] = []
  data["booking"].append(3)
  datas.append(data)

  data = {}
  data["id"] = 10004
  data["name"] = "10004"
  data["tel"] = 1323231004
  data["booking"] = []
  data["booking"].append(4)
  datas.append(data)
  WriteToDB(datas, "student.db")
  print(ReadFromDB("student.db"))

def BookingTest():
  datas = []

  data = {}
  data["id"] = 1
  data["teacher_id"] = 1000
  data["student_id"] = 10001
  data["time"] = "2023-03-21 10:00-11:00"
  datas.append(data)

  data = {}
  data["id"] = 2
  data["teacher_id"] = 1000
  data["student_id"] = 10002
  data["time"] = "2023-03-21 14:00-15:00"
  datas.append(data)

  data = {}
  data["id"] = 3
  data["teacher_id"] = 1001
  data["student_id"] = 10003
  data["time"] = "2023-03-21 14:00-15:00"
  datas.append(data)

  data = {}
  data["id"] = 4
  data["teacher_id"] = 1001
  data["student_id"] = 10004
  data["time"] = "2023-03-21 14:00-15:00"
  datas.append(data)

  WriteToDB(datas, "booking.db")
  print(ReadFromDB("booking.db"))



#TeacherTest()
#StudentTest()
#BookingTest()
