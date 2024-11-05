import pandas as pd
import numpy as np

# Defining the number of desired survey responses
num_responses = 500

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
age = ['under 18', '18-30', '31-44', '45-55', '56 and above']
gender = ['female', 'male', 'other']

# Adjusting the probabilities for impact ratings to reduce negative/neutral responses
impact_probs = [0.4, 0.4, 0.1, 0.05, 0.05]  # Higher chance of positive ratings

# Generate impact ratings with specified probabilities
impact_responses = np.random.choice(impact_rating, num_responses, p=impact_probs)

# Initialize the DataFrame
data = {
    'Impact Rating': impact_responses,
    'Most Visited Event': [],
    'Visit Frequency': [],
    'Benefits': [],
    'Age': [],
    'Gender': []
}

# Generate responses for all impact ratings, regardless of whether they are positive, neutral, or negative
for i in range(num_responses):
    # Create dictionaries to track event frequencies
    event_data = {event: np.random.choice(visit_frequency) for event in event_type}
    
    # Find the most visited event (Weekly > Monthly > Occasionally > Rarely)
    frequency_order = {'Weekly': 4, 'Monthly': 3, 'Occasionally': 2, 'Rarely': 1}
    most_visited = max(event_data, key=lambda k: frequency_order[event_data[k]])
    
    # Append the most visited event and corresponding data
    data['Most Visited Event'].append(most_visited)
    data['Visit Frequency'].append(event_data[most_visited])
    data['Benefits'].append(np.random.choice(benefits))
    data['Age'].append(np.random.choice(age))
    data['Gender'].append(np.random.choice(gender))

# Load the responses into a DataFrame
survey_data = pd.DataFrame(data)
print('Responses successfully added to a DataFrame')

# Save the DataFrame to a CSV file
survey_data.to_csv('simplified_responses.csv', index=False)

# Show the first five entries of the DataFrame
print(survey_data.head())
