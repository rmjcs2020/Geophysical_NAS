from deephyper.benchmark import NaProblem
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__)) # useful to locate data files with respect to this file
sys.path.insert(0,HERE)

from load_data import load_data
from search_space import create_search_space
from deephyper.search.nas.model.preprocessing import minmaxstdscaler

Problem = NaProblem(seed=2019)

Problem.load_data(load_data)

# Problem.preprocessing(minmaxstdscaler)

Problem.search_space(create_search_space, num_layers=5)

Problem.hyperparameters(
    batch_size=32,
    learning_rate=0.001,
    optimizer='adam',
    num_epochs=20,
    callbacks=dict(
        EarlyStopping=dict(
            monitor='r2', # or 'val_acc' ?
            mode='max',
            verbose=0,
            patience=10
        )
    )
)

Problem.loss('mse') # or 'categorical_crossentropy' ?

Problem.metrics(['r2']) # or 'acc' ?

Problem.objective('val_r2__last') # or 'val_acc__last' ?

# Just to print your problem, to test its definition and imports in the current python environment.
if __name__ == '__main__':
    print(Problem)