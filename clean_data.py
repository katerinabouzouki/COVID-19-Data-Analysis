import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    df = pd.read_csv(
    r"C:\Users\PC\Desktop\COVID-19 Data Analysis\covid_19_clean_complete_1.csv",
    sep=';',
    parse_dates=['Date'],
    dayfirst = True
    )

    df.columns = df.columns.str.strip()
    return df

def plot_greece(df):
    greece_df = df[df['Country/Region'] == 'Greece']
    greece_df = greece_df.groupby('Date')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()

    print(greece_df)

    plt.figure(figsize=(14,6))
    plt.plot(greece_df['Date'], greece_df['Confirmed'], label='Confirmed Cases', color='blue')
    plt.plot(greece_df['Date'], greece_df['Deaths'], label='Deaths', color='red')
    plt.plot(greece_df['Date'], greece_df['Recovered'], label='Recovered', color='green')

    plt.title('Evolution of COVID-19 Cases in Greece')
    plt.xlabel('Date')
    plt.ylabel('Number of people')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

def compare_countries(df):
    countries = ['Greece', 'Italy']
    df_countries = df[df['Country/Region'].isin(countries)]
    df_countries = df_countries.groupby(['Date', 'Country/Region'])[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()
    
    plt.figure(figsize=(14,7))
    for country in countries:
        country_data = df_countries[df_countries['Country/Region'] == country]
        plt.plot(country_data['Date'], country_data['Confirmed'], label=f'Cases - {country}')

    plt.title('Comparison of Confirmed COVID-19 Cases: Greece vs Italy')
    plt.xlabel('Date')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def top_countries_by_cases(df, top_n=10):
    latest_confirmed = df.groupby(['Country/Region'])['Confirmed'].max().sort_values(ascending=False).head(top_n)
    
    plt.figure(figsize=(10,6))
    latest_confirmed.sort_values().plot(kind='barh', color='skyblue')
    plt.title(f'Top {top_n} Countries with the most confirmed cases')
    plt.xlabel('Confirmed Cases')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_data()
    #plot_greece(df)
    #compare_countries(df)
    top_countries_by_cases(df, top_n=10)







