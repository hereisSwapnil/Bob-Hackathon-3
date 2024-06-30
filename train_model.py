import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd

# Load dataset
data = pd.read_csv('path/to/your/transaction_data.csv')
X = data.drop('target', axis=1)
y = data['target']

# Define model
model = Sequential([
    Dense(64, input_dim=X.shape[1], activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

# Save model
model.save('transaction_audit_model.h5')