import pandas as pd
import matplotlib.pyplot as plot

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
#Заголовки для стовпців
headers = [
    "number_of_times_pregnant",
    "plasma_glucose_concentration",
    "diastolic_blood_pressure",
    "triceps_skin_fold_thickness",
    "2_hour_serum_insulin",
    "body_mass_index",
    "diabetes_pedigree_function",
    "age",
    "class_variable"
]
#Стовпці в яких значення не може бути нульовим
nonPossibleZeroColumn = [
    "plasma_glucose_concentration",
    "diastolic_blood_pressure",
    "triceps_skin_fold_thickness",
    "2_hour_serum_insulin",
    "body_mass_index",
    "diabetes_pedigree_function",
    "age"
]
#Парсинг даних
data = pd.read_csv(url, names = headers)

#Вивід розміру масиву
print("Number of columns: ", data.shape[0], " Number of rows: ", data.shape[1])

#Опрацювання пустих даних
data[nonPossibleZeroColumn] = data[nonPossibleZeroColumn].replace(0, pd.NA)
missing_data = data.isnull().sum()
#Вивід кількості пустих даних
print("Missing Data:")
print(missing_data, "\n")

#Обчислення середнього арифметичного, дисперсії, та середнє квадратичного значення
meanValues = data.mean()
varianceValues = data.var()
stdDeviationValues = data.std()

#Вивід середнього арифметичного, дисперсії, та середнє квадратичного значення
print("Mean values\n")
print(meanValues, "\n")
print("Variance values\n")
print(varianceValues, "\n")
print("Standart deviation values\n")
print(stdDeviationValues, "\n")

#Виключеня рядків з недійсними даними
data = data.dropna()

#Формування гістограм даних
plot.figure(figsize=(12, 10))
for i, column in enumerate(data.columns):
    if column != 'class_variable':
        plot.subplot(3, 3, i + 1)
        plot.hist(data[column], bins=20, alpha=0.5)
        plot.title(column)
        plot.xlabel('Values')
        plot.ylabel('Frequency')

plot.tight_layout()
plot.show()