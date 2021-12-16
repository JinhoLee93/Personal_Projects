import pandas as pd
import argparse
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

parser = argparse.ArgumentParser()
parser.add_argument('trainfile', type=str, help='train file name')
#parser.add_argument('testfile', type=str, help='test file name')
args = parser.parse_args()

train_data = pd.read_csv(args.trainfile)

X = train_data.drop(['PoolQC', 'SalePrice','GarageQual', 'FireplaceQu','Fence',
                     'MiscFeature', 'Alley', 'LotFrontage'], axis=1)
y = train_data.SalePrice

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
houseModel = RandomForestRegressor(random_state=1)

sns.heatmap(X.isnull(), yticklabels=False,cbar=False,cmap='viridis')
plt.show()
