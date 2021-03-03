import pandas
stu = []
for i in range (3):
    s = input("student: ")
    sc = input("score: ")
    stu = 
    data_dict = {
        "students": [s],
        "Scores": [sc]
    }
    data=pandas.DataFrame(data_dict)
    data.to_csv("24.Create_dataframe.csv")

