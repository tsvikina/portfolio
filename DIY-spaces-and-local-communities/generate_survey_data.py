import pandas as pd
import numpy as np

# Defining the number of desired survey responses
num_responses = 100

# Defining the possible answers for each question
visit_frequency = ['Weekly', 'Monthly', 'Occasionally', 'Rarely']
event_type = ['Concert', 'DIY Cinema', 'Exhibition', 'Debates', 'Queer bar', 'Community meetings', 'Swapshop', 'Free kitchen', 'Other']
impact_rating = ['Very positive', 'Positive', 'Neutral', 'Negative', 'Very negative']
benefits = [
    'Improved Social Connections',
    'Enhanced Cultural Awareness',
    'Inspiration and Creativity',
    'Sense of Belonging to a Community',
    'Support for Local Artists and Initiatives',
    'Emotional Well-being'
]

# Adjusting the probabilities for impact ratings to reduce negative/neutral responses
impact_probs = [0.4, 0.4, 0.1, 0.05, 0.05]  # Higher chance of positive ratings

# Generate impact ratings with specified probabilities
impact_responses = np.random.choice(impact_rating, num_responses, p=impact_probs)

# Initialize the DataFrame
data = {
    'Impact Rating': impact_responses
}

# For respondents with impact rating above 'Neutral', generate responses for other questions
for i in range(num_responses):
    if impact_responses[i] in ['Very positive', 'Positive']:
        data.setdefault('Overall Visit Frequency', []).append(np.random.choice(visit_frequency))
        for event in event_type:
            data.setdefault(f'{event} Frequency', []).append(np.random.choice(visit_frequency))
            data.setdefault(f'{event} Benefits', []).append(np.random.choice(benefits))
    else:
        data.setdefault('Overall Visit Frequency', []).append(np.nan)
        for event in event_type:
            data.setdefault(f'{event} Frequency', []).append(np.nan)
            data.setdefault(f'{event} Benefits', []).append(np.nan)

# Load the responses into a DataFrame
survey_data = pd.DataFrame(data)
print('Responses successfully added to a DataFrame')

# Save the DataFrame to a CSV file
survey_data.to_csv('generated_event_impact_survey_responses.csv', index=False)

# Show the first five entries of the DataFrame
print(survey_data.head())
print('Blabla')
