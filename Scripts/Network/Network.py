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
BSE =
EBSD =
OM =

# INPUTS
input_1 = Input(shape=BSE_SHAPE)
input_2 = Input(shape=EBSD_SHAPE)
input_3 = Input(shape=OM_SHAPE)

# FIRST BRANCH
one = Conv2D(CONV_NODES[1], (3, 3), activation='relu', input_shape=BSE.shape[1:])
one = MaxPool2D(pool_size=(2, 2))(one)

one = Conv2D(CONV_NODES[1] * 2, 3, activation='relu')(one)
one = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(one)

one = Conv2D((CONV_NODES[1] / 2), 3, activation='relu')(one)
one = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(one)


# SECOND BRANCH
two = Conv2D(CONV_NODES[1], (3, 3), activation='relu', input_shape=EBSD.shape[1:])
two = MaxPool2D(pool_size=(2, 2))(two)

two = Conv2D(CONV_NODES[1] * 2, 3, activation='relu')(two)
two = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(two)

two = Conv2D((CONV_NODES[1] / 2), 3, activation='relu')(two)
two = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(two)

# THIRD BRANCH
three = Conv2D(CONV_NODES[1], (3, 3), activation='relu', input_shape=OM.shape[1:])
three = MaxPool2D(pool_size=(2, 2))(three)

three = Conv2D(CONV_NODES[1] * 2, 3, activation='relu')(three)
three = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(three)

three = Conv2D((CONV_NODES[1] / 2), 3, activation='relu')(three)
three = MaxPool2D(pool_size=(2, 2), strides=2, padding='valid')(three)

# COMBINE THE BRANCHES
combined = concatenate(one.output, two.output, three.output)

# END BRANCH
end = Dense(DENSE_NODES[0], activation='relu')(combined)
end = Dense(DENSE_NODES[0] / 2, activation='relu')(end)
end = Dense(1, activation='sigmoid')(end)

# MODEL
model = Model(inputs=[one.input, two.input, three.input], outputs=end)





