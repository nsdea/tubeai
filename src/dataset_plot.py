import dataset
import matplotlib.pyplot as plt

data_dict = dataset.views_per_like__like_percentage
data_dict = {k: v for k, v in sorted(list(data_dict.items()))}

plt.plot(data_dict.keys(), data_dict.values(), 'o:')
plt.xlabel('Views per like')
plt.ylabel('Like Percentage')
plt.show()