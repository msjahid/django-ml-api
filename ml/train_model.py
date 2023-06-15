import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression


# Load the dataset
df = pd.read_csv('../data/salary_data.csv')

# Split the data into training and testing sets
train_df = df.sample(frac=0.8, random_state=123)
test_df = df.drop(train_df.index)

# Extract the input and output variables for the training and testing sets
train_X = train_df.drop('Salary', axis=1)
train_y = train_df['Salary']
test_X = test_df.drop('Salary', axis=1)
test_y = test_df['Salary']

# Fit a linear regression model to the training data
model = LinearRegression()
model.fit(train_X, train_y)

# Make predictions on the testing data
predictions = model.predict(test_X)

# # Save the trained model to a pickle file
# with open('salary_model.pkl', 'wb') as f:
#     pickle.dump(model, f)