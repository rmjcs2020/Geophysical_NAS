import numpy as np
np.random.seed(2018)
from sklearn.preprocessing import MinMaxScaler

import os
HERE = os.path.dirname(os.path.abspath(__file__)) # useful to locate data files with respect to this file



def load_data():
    """
    Generate data for linear function -sum(x_i).

    Return:
        Tuple of Numpy arrays: ``(train_X, train_y), (valid_X, valid_y)``.
    """

    train_data = np.load(HERE+'/True_Train.npy')
    valid_data = np.load(HERE+'/True_Test.npy')

    features_train = np.transpose(train_data)
    features_valid = np.transpose(valid_data)[:700,:]
    features = np.concatenate((features_train,features_valid),axis=0)

    states = np.copy(features[:,:]) #Rows are time, Columns are state values

    scaler = MinMaxScaler()
    states = scaler.fit_transform(states)

    seq_num = 8

    # Need to make batches of 10 input sequences and 1 output
    total_size = np.shape(features)[0] - 2*seq_num
    input_seq = np.zeros(shape=(total_size,seq_num,np.shape(states)[1]))
    output_seq = np.zeros(shape=(total_size,seq_num,np.shape(states)[1]))

    for t in range(total_size):
        input_seq[t,:,:] = states[None,t:t+seq_num,:]
        output_seq[t,:,:] = states[None,t+seq_num:t+2*seq_num,:]

    idx = np.arange(total_size)
    np.random.shuffle(idx)
    
    input_seq = input_seq[idx,:,:]
    output_seq = output_seq[idx,:]

    num_samples_train = 900

    input_seq_train = input_seq[:num_samples_train,:,:]
    output_seq_train = output_seq[:num_samples_train,:,:]

    input_seq_valid = input_seq[num_samples_train:,:,:]
    output_seq_valid = output_seq[num_samples_train:,:,:]

    # # Interface to run training data must me respected
    return (input_seq_train, output_seq_train), (input_seq_valid, output_seq_valid)

if __name__ == '__main__':
    load_data()
