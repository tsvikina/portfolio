import pandas as pd

# Load the data
df = pd.read_csv('adult.data.csv')

def calculate_demographic_data(print_data=True):
    """
    Calculate various demographic statistics from the dataset.
    """
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(2)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education']=='Bachelors').mean()*100, 2)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters','Doctorate'])
    higher_education_count = higher_education.sum()
    higher_salary = df['salary'] == '>50K'
    higher_education_rich_count = (higher_education&higher_salary).sum()

    # What percentage of people without advanced education make more than 50K?
    lower_education =  ~higher_education
    lower_education_count = lower_education.sum()
    lower_education_rich_count = (lower_education&higher_salary).sum()
    higher_education_rich = ((higher_education_rich_count/higher_education_count)*100).round(2)
    lower_education_rich= ((lower_education_rich_count/lower_education_count)*100).round(2)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K' ).mean() * 100 , 2)

    # What country has the highest percentage of people that earn >50K?
    country_groups = df.groupby('native-country')
    rich_percentage_by_country = (country_groups['salary'].apply(lambda x:(x == '>50K').mean())*100).round(2)
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = rich_percentage_by_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    rich_in_India = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = rich_in_India['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
