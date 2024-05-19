from solvers import *
from dataset import GamesDataset
from tqdm import tqdm
import pickle

generator = GamesDataset(difficulty=10)
final_states = ['MAX', 'MIN', 'DRAW', None]
for i in tqdm(range(10000)):
    state = generator.generateState()
    if state[1] in final_states:
        continue
    generator.loc[len(generator)] = state
print(len(generator))
generator.to_csv('data.csv')
pickle.dump(generator, open('data.sav', 'wb'))