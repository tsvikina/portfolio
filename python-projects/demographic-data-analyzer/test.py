import pandas as pd

# Load the data
df = pd.read_csv('adult.data.csv')

def calculate_demographic_data(print_data=True):
    """
    Calculate various demographic statistics from the dataset.
    """
    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(2)

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 2)

    # People with advanced education and their earnings
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / higher_education.sum()) * 100, 2)
    
    # People without advanced education and their earnings
    lower_education_rich = round((df[~higher_education & (df['salary'] == '>50K')].shape[0] / (~higher_education).sum()) * 100, 2)

    # Minimum work hours and percentage of rich among them
    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 2)

    # Country with the highest percentage of rich people
    rich_percentage_by_country = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100).round(2)
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = rich_percentage_by_country.max()

    # Top occupation in India for rich earners
    rich_in_India = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = rich_in_India['occupation'].value_counts().idxmax()

    # Print and return results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelor's degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
