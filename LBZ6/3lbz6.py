import pandas as pd
import matplotlib.pyplot as plt

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=',', encoding='utf-8')
        print("Ok.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"No data in file: {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"Error parsing file: {file_path}")
        return None

def count_and_plot_gender(df):
    gender_counts = df['Стать'].value_counts()
    print("Gender Counts:")
    print(gender_counts)
    gender_counts.plot(kind='bar', title='Gender Distribution', legend=False)
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()

def count_and_plot_age_categories(df):
    bins = [0, 18, 30, 45, 60, float('inf')]
    labels = ['0-18', '19-30', '31-45', '46-60', '61+']

    current_year = pd.Timestamp.now().year
    df['Age'] = current_year - pd.to_datetime(df['Дата народження']).dt.year

    df['Age Category'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    age_category_counts = df['Age Category'].value_counts().sort_index()
    print("Age Category Counts:")
    print(age_category_counts)

    age_category_counts.plot(kind='bar', title='Age Category Distribution', legend=False)
    plt.xlabel('Age Category')
    plt.ylabel('Count')
    plt.show()


def count_and_plot_gender_by_age_categories(df):
    bins = [0, 18, 30, 45, 60, float('inf')]
    labels = ['0-18', '19-30', '31-45', '46-60', '61+']

    current_year = pd.Timestamp.now().year
    df['Age'] = current_year - pd.to_datetime(df['Дата народження']).dt.year

    df['Age Category'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    gender_by_age = df.groupby(['Age Category', 'Стать'],observed=False).size().unstack(fill_value=0)
    print("Gender by Age Category Counts:")
    print(gender_by_age)

    gender_by_age.plot(kind='bar', stacked=True, title='Gender by Age Category Distribution')
    plt.xlabel('Age Category')
    plt.ylabel('Count')
    plt.legend(title='Gender')
    plt.show()

file_path ="data.csv"
df = read_csv_file(file_path)
if df is not None:
    count_and_plot_gender(df)
    count_and_plot_age_categories(df)
    count_and_plot_gender_by_age_categories(df)
