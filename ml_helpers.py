"""
AJ Clemendor ML - Seating

Devd as a gift for Mrs. Donaldson

2023
"""

import tensorflow as tf
from tensorflow.keras.layers import Dense, Input, Dropout
from tensorflow.keras.models import Model

def create_compatibility_model(input_dim=5, hidden_units=[64, 32], dropout_rate=0.5):
    input_layer = Input(shape=(input_dim,))
    x = input_layer

    for units in hidden_units:
        x = Dense(units, activation='relu')(x)
        x = Dropout(dropout_rate)(x)

    output_layer = Dense(1, activation='sigmoid')(x)

    model = Model(inputs=input_layer, outputs=output_layer)

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model
