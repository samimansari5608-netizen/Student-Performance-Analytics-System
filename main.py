import pandas as pd
import numpy as np

data = pd.read_csv("students.csv")
marks = data[["Python", "Maths", "English"]].to_numpy()

print(data)
print(data.columns)
print("Total students:", len(data))
data.info()
data["Total_Marks"] = np.sum(marks, axis=1)
print(data)
data["Average"] = np.mean(marks, axis=1)
print(data)
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

data["Grade"] = data["Average"].apply(calculate_grade)
data["Result"] = data[["Python", "Maths", "English"]].ge(40).all(axis=1).map({True: "Pass", False: "Fail"})
print(data)
    
print("Highest Average:", data["Average"].max())
print("Lowest Average:", data["Average"].min())

top_student = data.loc[data["Average"].idxmax()]
print("Top Performer:", top_student["Name"])
print("Top Student Average:", top_student["Average"])
print("Total Passed:", (data["Result"] == "Pass").sum())
print("Total Failed:", (data["Result"] == "Fail").sum())
print("Overall Class Average:", data["Average"].mean())
print("Python Subject Average:", data["Python"].mean())
print("Maths Subject Average:", data["Maths"].mean())
print("English Subject Average:", data["English"].mean())
subject_averages = data[["Python", "Maths", "English"]].mean()
print("Best Performing Subject:", subject_averages.idxmax())
print("Highest Marks in Python:", data["Python"].max())
print("Lowest Marks in Python:", data["Python"].min())