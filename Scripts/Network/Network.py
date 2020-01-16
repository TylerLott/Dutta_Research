# This is a multi-input neural network for additive manufacturing research
# Input is three images and output is a single number

# IMPORTS
import tensorflow as tf
import numpy as np
from keras.models import Input, Model
from keras.layers import Conv2D, MaxPool2D, concatenate, Dense, Conv3D, MaxPool3D

# CONSTANTS
BSE_SHAPE = (500, 500, 1)
EBSD_SHAPE = (200, 200, 3)
OM_SHAPE = (1000, 1000, 1)

# VARIABLES
CONV_NODES = [64, 128, 256, 512]
DENSE_NODES = [32, 64, 128]

# TRAIN DATA IMPORT
BSE = 'path'
EBSD = 'path'
OM = 'path'

# NESTED FOR LOOPS
# This is to allow the variables to test different node variations
for dense_nodes in DENSE_NODES:
    for conv_nodes in CONV_NODES:

        # INPUTS
        input_1 = Input(shape=BSE_SHAPE)
        input_2 = Input(shape=EBSD_SHAPE)
        input_3 = Input(shape=OM_SHAPE)

        # FIRST BRANCH
        # BSE
        # needs to accept a black and white image
        one = Conv2D(conv_nodes, (3, 3), activation='relu', input_shape=BSE.shape[1:])
        one = MaxPool2D(pool_size=(2, 2))(one)

        one = Conv2D(conv_nodes * 2, 3, activation='relu')(one)
        one = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(one)

        one = Conv2D((conv_nodes / 2), 3, activation='relu')(one)
        one = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(one)


        # SECOND BRANCH
        # EBSD
        # needs to accept a RGB image
        two = Conv2D(conv_nodes, (3, 3), activation='relu', input_shape=EBSD.shape[1:])
        two = MaxPool2D(pool_size=(2, 2))(two)

        two = Conv2D(conv_nodes * 2, 3, activation='relu')(two)
        two = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(two)

        two = Conv2D((conv_nodes / 2), 3, activation='relu')(two)
        two = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(two)

        # THIRD BRANCH
        # OM
        # needs to accept a black and white image
        three = Conv2D(conv_nodes, (3, 3), activation='relu', input_shape=OM.shape[1:])
        three = MaxPool2D(pool_size=(2, 2))(three)

        three = Conv2D(conv_nodes * 2, 3, activation='relu')(three)
        three = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(three)

        three = Conv2D((conv_nodes / 2), 3, activation='relu')(three)
        three = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(three)

        # COMBINE THE BRANCHES
        # concatenates the three branches all together into one
        combined = concatenate(one.output, two.output)
        combined = concatenate(combined, three.output)

        # END BRANCH
        end = Dense(dense_nodes, activation='relu')(combined)
        end = Dense(dense_nodes / 2, activation='relu')(end)
        end = Dense(1, activation='sigmoid')(end)

        # MODEL
        model = Model(inputs=[one.input, two.input, three.input], outputs=end)

        # COMPILE MODEL
        model.compile(loss='loss', optimizer='adam', metrics=['accuracy'])

        # FIT MODEL
        model.fit(validation_split=0.2)





