import pandas as pd
import numpy as np

# Defining the number of desired survey responses
num_responses = 100

# Defining the possible answers for each question
visit_frequency = ['Weekly', 'Monthly', 'Occasionally', 'Rarely']
event_type = ['Concerts', 'Workshops', 'Community meetings', 'Swapshop', 'Community kitchen', 'Other']
community_connection =['Yes', 'No']
benefits = ['Improved social connections', 'Enhanced cultural awareness', 'Other']
impact_rating = ['Very positive', 'Positive', 'Neutral', 'Negative', 'Very negative']

# Generate responses
responses = {
    'Visit Frequency' : np.random.choice(visit_frequency, num_responses),
    'Event Type' : np.random.choice(event_type, num_responses),
    'Community Connection' : np.random.choice(community_connection, num_responses),
    'Benefits' : np.random.choice(benefits, num_responses),
    'Impact Rating' : np.random.choice(impact_rating, num_responses)}

# Load the responses in a dataframe
survey_data = pd.DataFrame(responses)
print('Responses successfully added to a DataFrame')

# Save the df in an csv
survey_data.to_csv('generated_survey_responses.csv', index = False)

# Show the first five entries of the df
print(survey_data.head())
