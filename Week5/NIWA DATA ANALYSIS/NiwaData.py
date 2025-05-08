import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


class SimpleDataAnalyzer:
    def __init__(self, filename="1026__monthly__Total_Heating_Degree_Days_for_18C__days.csv"):
        self.base_directory = os.path.dirname(os.path.abspath(__file__))  # noqa #get the current directory
        self.csv_path = os.path.join(self.base_directory, filename)      # noqa #join current directory and the filename
        self.df = None                                                   # noqa #for storing the panda data frame

    def load_data(self):
        try:
            self.df = pd.read_csv(self.csv_path, dtype={'YEAR': str})   # noqa #this line reads the file
            print(f"Data loaded successfully from {self.csv_path}")
        except FileNotFoundError:                                       # noqa #error handling incase there is no file with described file name
            print(f"Error: The file '{self.csv_path}' was not found.")
            sys.exit(1)                                                 # noqa #ends the program when error occurs
        except Exception as e:                                          # noqa #error handling for other error that will occur
            print(f"An error occurred while loading the data: {e}")
            sys.exit(1)                                                 # noqa #ends the program when error occurs

    def show_average_per_year(self):
        print("Average Stats Value per Year:")
        yearly_avg = self.df.groupby('YEAR')['STATS_VALUE'].mean().round(2)
        print(yearly_avg.to_string())
        print("\n")

    def row_with_highest_value(self):
        print("Row with the highest Stats Value:")
        highest_value = self.df['STATS_VALUE'].max()                             # noqa #this line filters the highest value in STATS_VALUE column
        highest_row = self.df[self.df['STATS_VALUE'] == highest_value].iloc[0]   # noqa #iloc is integer location, and zero means the first record of the filtered dataframe
        print(highest_row.to_string())                                           # noqa #to_string() function to get rid of the Name and dtype
        print("\n")

    def row_with_lowest_value(self):
        print("Row with the lowest Stats Value:")
        lowest_value = self.df['STATS_VALUE'].min()                              # noqa #this line filters the lowest value in STATS_VALUE column
        lowest_row = self.df[self.df['STATS_VALUE'] == lowest_value].iloc[0]     # noqa #self.df outside is the dataframe or the file that needs to be filtered. the self.df inside the bracket applies the actual filter
        print(lowest_row.to_string())
        print("\n")

    def row_high_topten(self):
        print("Top 10 highest Stats Value:")
        top_value = self.df.sort_values(by=['STATS_VALUE'], ascending=False)     # noqa  #sorts the dataframe in descending order. sort_value function does not have descending
        top_row = top_value.head(10)                                             # noqa #this list the top 10 records
        print(top_row)
        print("\n")

    def row_low_topten(self):
        print("Top 10 lowest Stats Value:")
        low_value = self.df.sort_values(by=['STATS_VALUE'], ascending=True)
        low_row = low_value.head(10)
        print(low_row)
        print("\n")

    def plot_data_highest(self):

        fig, (ax1) = plt.subplots(1, figsize=(12, 5))                                             # noqa # creates a single subplot with size 12width x 5height

        # Plot 1: Monthly values over time
        self.df.plot(x='YEAR', y='STATS_VALUE', ax=ax1, marker='o', linestyle='-', markersize=4)  # noqa # this is the attributes of the plot
        ax1.set_title('Monthly Heating Degree Days Over Time')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Heating Degree Days')
        ax1.grid(True)                                                                            # noqa #shows the gridlines for guides
        # Adjust layout and display
        plt.tight_layout()                                                                        # noqa #this is to auto adjust spacings to avoid overlapping of plot
        plt.show()                                                                                # noqa #to show the window of the plot


def main():
    analyzer = SimpleDataAnalyzer()
    analyzer.load_data()
    analyzer.show_average_per_year()
    analyzer.row_with_highest_value()
    analyzer.row_with_lowest_value()
    analyzer.row_high_topten()
    analyzer.row_low_topten()
    analyzer.plot_data_highest()


if __name__ == "__main__":
    main()
