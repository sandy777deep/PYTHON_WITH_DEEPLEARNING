
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


dataset = pd.read_csv('train.csv')

dataset['Sex'] = dataset['Sex'].map( {'female': 1, 'male': 0} )

print(dataset['Survived'].corr(dataset['Sex']))

# plotting for all the columns
corr = dataset.corr()
sm.graphics.plot_corr(corr, xnames=list(corr.columns))
plt.show()