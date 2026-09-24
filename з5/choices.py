import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('з5/choices.xlsx')

to_plot = pd.DataFrame(data['Choice_1'].value_counts())
to_plot.columns = ['Amount']
to_plot = to_plot.sort_index()

plt.bar(to_plot.index, to_plot['Amount'])
plt.xticks(rotation = 'vertical')
plt.show()

full_to_plot = pd.DataFrame(pd.DataFrame(data.values.reshape(-1))[0].value_counts())
full_to_plot.columns = ['Amount']
full_to_plot = full_to_plot.sort_index()

plt.pie(full_to_plot['Amount'], labels = full_to_plot.index)
plt.show()