import pandas as pd
import numpy as np
import pickle
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

df = pickle.load(open('data.sav', 'rb'))

x = df['states'].apply(lambda x: np.array(x.board.flat)).tolist()
y = df['best_move'].apply(lambda x: x[0]*3 + x[1]).tolist()

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=0)
model = LinearSVC()
model.fit(xtrain, ytrain)