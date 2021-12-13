from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
from pandas import DataFrame as df
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    'filename', type=str, help='File for training the model')
args = parser.parse_args()

class AirQuality:
    def __init__(self, filename):
        self.file = pd.read_csv(filename)
        self.RFR = RandomForestRegressor()
        self.ABR = AdaBoostRegressor()

    def show(self):
        print(self.file.head()) # Show first 5 rows of the data

    def prepareData(self):
        data = self.file.drop(['Date', 'AIQ'], axis=1)
        target = self.file['AIQ']

        return data, target

    def trainRFR(self, data, target):
        self.RFR.fit(data, target)
        print(self.RFR.score(data, target) * 100)

    def trainABR(self, data, target):
        self.ABR.fit(data, target)
        print(self.ABR.score(data, target) * 100)

if __name__ == '__main__':
    m = AirQuality(args.filename)
    data, target = m.prepareData()
    m.trainABR(data, target)
    m.trainRFR(data, target)
