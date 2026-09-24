import pandas

stars = pandas.read_csv('з4\pulsar_star.csv')

result0 = stars.query('TG == 0 and 79.8125 <= MIP <= 81.5234375')
meanResult0 = result0['MIP'].mean()

result1 = stars.query('TG == 1 and 36.4140625 <= MIP <= 41.8828125')
meanResult1 = result1['MIP'].mean()


print(f"найдено строк TG == 0: {len(result0)}")
print(f"среднее MIP: {round(meanResult0, 3)}")
print("---------------------------------------")
print(f"найдено строк TG == 1: {len(result1)}")
print(f"среднее MIP: {round(meanResult1, 3)}")