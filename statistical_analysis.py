import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# !-----Step 1: Function to read Worldbank format and return transposed dataframes-----!
def read_worldbank_data(filename):
    # Reading the dataset
    # Extra rows are deducted manually in the dataset
    df = pd.read_csv(filename)

    # Transposing our dataframe
    df_transposed = df.T

    # Setting the first row as the header
    df_transposed.columns = df_transposed.iloc[0]

    # Dropping the first row (header) and resetting the index
    df_transposed = df_transposed[1:].reset_index()

    # Converting years to numeric because in world bank format the year is in string
    df_transposed = df_transposed.apply(pd.to_numeric, errors='ignore')

    return df, df_transposed


# !-----Step 2: Function to explore statistical properties and produce summary statistics-----!
def explore_statistics2(df, countries=[]):
    # Dropping the first three rows
    # Because in transposed df, these rows are Country Code, Indicator Name and Indicator Code
    dropped_data = df.iloc[3:]

    # Selecting relevant columns (only the country which we will select)
    selected_data = dropped_data[countries]

    # Converting all columns to numeric
    selected_data = selected_data.apply(pd.to_numeric, errors='coerce')

    print('Information Of Dataset')
    # Information method for getting information about dataset
    # 'info_of_data' this method is automatically printed on the console,
    # Because of the fact that when we use info() in print statement it will return null
    info_of_data = selected_data.info()

    # Describe method for summary statistics
    summary_stats = selected_data.describe()

    # Correlation Matrix (to see the corr relation between selected countries
    correlation_matrix = selected_data.corr()

    # Printing the results as needed
    print("\nSummary Statistics:")
    print(summary_stats)

    print("\nCorrelation Matrix:")
    print(correlation_matrix)


# Function to visualize time series analysis for each country
def visualize_time_series(df, countries=[]):
    # Dropping the first three rows
    # because in transposed df, these rows are Country Code, Indicator Name and Indicator Code
    selected_data = df.iloc[3:]

    # Converting all columns to numeric
    selected_data = selected_data.apply(pd.to_numeric, errors='coerce')

    # Setting the index to be the years from 1990 to 2015
    selected_data.index = range(1990, 2016)

    # Plotting time series for each country
    plt.figure(figsize=(12, 6))
    plt.title(f'Time Series Analysis')

    for country in countries:
        plt.plot(selected_data[country], label=country)

    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


# Function to visualize correlation heatmap
def visualize_correlation_heatmap(df, countries=[]):
    # Dropping the first three rows
    # because in transposed df, these rows are Country Code, Indicator Name and Indicator Code
    selected_data = df.iloc[3:]

    # Converting all columns to be numeric
    selected_data = selected_data.apply(pd.to_numeric, errors='coerce')

    # Calculating correlation matrix
    correlation_matrix = selected_data.corr()

    # Setting the index to be the years from 1990 to 2015
    selected_data.index = range(1990, 2016)

    # Selecting only the correlations for the selected countries
    correlation_subset = correlation_matrix.loc[countries, countries]

    # Plotting heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_subset, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.show()


# !-----Step 3: Reading and exploring data for Renewable Electricity Output-----!
output_filename = 'Ren_Elec_Output.csv'
output_df, output_df_transposed = read_worldbank_data(output_filename)


# !-----Step 4: Reading and exploring data for Renewable Electricity Consumption-----!
consumption_filename = 'Ren_Elec_Consumption.csv'
consumption_df, consumption_df_transposed = read_worldbank_data(consumption_filename)


print(output_df.head())
print('\n')
print(output_df_transposed.head())
print('\n')
print(consumption_df.head())
print('\n')
print(consumption_df_transposed.head())
print('\n')


# !-----Step 5: Exploring statistical properties for selected indicators and countries-----!
selected_countries = ['Africa Eastern and Southern', 'Afghanistan', 'Africa Western and Central']

print("\nRenewable Electricity Output Statistics:")
print(explore_statistics(output_df_transposed, selected_countries))
print("\n\nRenewable Electricity Consumption Statistics:")
print(explore_statistics(consumption_df_transposed, selected_countries))


# Visualising the Renewable Electricity Output for selected countries through years
# And Visualising the Corellation bwtween seleted for Renewable Electricity Output
print('\t\t\t\t\t   !!!!!-----Renewable Electricity Output-----!!!!!')
print(visualize_time_series(output_df_transposed, selected_countries))
print(visualize_correlation_heatmap(output_df_transposed, selected_countries))

# Visualising the Renewable Electricity Consumption for selected countries through years
# And Visualising the Corellation bwtween seleted for Renewable Electricity Consumption
print('\t\t\t\t\t !!!!!-----Renewable Electricity Consumption-----!!!!!')
print(visualize_time_series(consumption_df_transposed, selected_countries))
print(visualize_correlation_heatmap(consumption_df_transposed, selected_countries))
