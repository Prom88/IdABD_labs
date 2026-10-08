import pandas as pd

salaryData = pd.read_csv('з10/rosstat_salary_ru.csv')
salaryData.index += 1
salaryData = salaryData.sort_values(by = ["salary"])
print("среднее:", salaryData["salary"].mean())
print("медиана:", salaryData["salary"].median())
