import pandas as pd


def preprocess_data(input_data):
    # Convert input data to a pandas dataframe
    input_df = pd.DataFrame(input_data, index=[0])
    print("work")

    # Convert the 'YearsExperience' column to numeric, handling non-numeric values
    input_df['YearsExperience'] = pd.to_numeric(input_df['YearsExperience'], errors='coerce')

    # Drop any rows with NaN values
    input_df.dropna(inplace=True)

    # Return the preprocessed data as a dictionary
    return input_df.to_dict('records')[0]
