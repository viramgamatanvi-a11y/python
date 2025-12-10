import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta

class LibraryDashboard:
    def __init__(self):
        self.transactions_df = pd.DataFrame()
        self.statistics = {}

    def load_data(self, file_path):
        print(f"Loading data from: {file_path}...")
        try:
            df = pd.read_csv(file_path)
            df.columns = ['Transaction_ID', 'Date', 'User_ID', 'Book_Title', 'Genre', 'Duration_Days']
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            initial_count = len(df)
            df.drop_duplicates(inplace=True)
            print(f"Removed {initial_count - len(df)} duplicate rows.")
            df.dropna(subset=['Date', 'Book_Title', 'Duration_Days'], inplace=True)
            df['Duration_Days'] = df['Duration_Days'].astype(int)
            self.transactions_df = df
            print(f"Data loaded, cleaned, and validated successfully. Total transactions: {len(df)}")
            return True         
            
        except Exception as e:
            print(f"An unexpected error occurred during data loading: {e}")
            return False

    def calculate_statistics(self):
        if self.transactions_df.empty:
            print("Cannot calculate statistics: Data not loaded.")
            return

        df = self.transactions_df.copy()

        book_counts = df['Book_Title'].value_counts()
        most_borrowed_book = book_counts.idxmax()
        most_borrowed_count = int(book_counts.max())
        self.statistics['most_borrowed_book'] = most_borrowed_book
        self.statistics['most_borrowed_count'] = most_borrowed_count

        duration_array = df['Duration_Days'].astype(float)
        average_borrowing_time = round(duration_array.mean(), 2)
        self.statistics['average_borrowing_time'] = average_borrowing_time

        df['Date_Only'] = df['Date'].dt.date 
        day_counts = df['Date_Only'].value_counts()
        busiest_day_date = str(day_counts.idxmax())
        busiest_day_count = int(day_counts.max())
        self.statistics['busiest_day_date'] = busiest_day_date
        self.statistics['busiest_day_count'] = busiest_day_count
        
        print(f"Most Borrowed Book      : {most_borrowed_book} ({most_borrowed_count} times)")
        print(f"Average Borrowing Time  : {average_borrowing_time:.2f} days")
        print(f"Busiest Day             : {busiest_day_date} ({busiest_day_count} transactions)")

    def filter_transactions(self, condition):
        if self.transactions_df.empty:
            print("Cannot filter transactions: Data not loaded or is empty.")
            return pd.DataFrame()      
        try:
            filtered_df = self.transactions_df.query(condition, engine='python')
            print(f"Filter successful with condition '{condition}'. Found {len(filtered_df)} transactions.")
            return filtered_df
        except Exception as e:
            print(f"Error during filtering with condition '{condition}': {e}")
            return pd.DataFrame()  
                
    def generate_report(self):
        
        if self.transactions_df.empty:
            print("Cannot generate report: No data loaded.")
            return

        total_transactions = len(self.transactions_df)

        most_borrowed_count = self.transactions_df['Book_Title'].value_counts().max()
        most_borrowed_book = self.transactions_df['Book_Title'].value_counts().idxmax()

        average_duration = self.transactions_df['Duration_Days'].mean()

        borrow_count = self.transactions_df['Book_Title'].value_counts()

        print("\nLibrary Summary Report:")
        print(f"Total Transactions      : {total_transactions}")
        print(f"Most Borrowed Book      : {most_borrowed_book} ({most_borrowed_count} times)")
        print(f"Average Borrowing Time  : {average_duration:.2f} days")
        print("\nBorrow Count by Book:\n", borrow_count)

    def calculate_duration_statistics(self):        
        duration_array = self.transactions_df['Duration_Days'].values.astype(float)
        duration_stats = {
            'count': int(len(duration_array)),
            'mean': np.mean(duration_array).round(2),
            'median': np.median(duration_array).round(2),
            'std_dev': np.std(duration_array).round(2),
            'min': np.min(duration_array).round(2),
            'max': np.max(duration_array).round(2)
        }
        
        print("\n--- Borrowing Duration Statistics (NumPy) ---")
        print(f"Average Duration (Mean): {duration_stats['mean']} days")
        print(f"Median Duration: {duration_stats['median']} days")
        print(f"Standard Deviation: {duration_stats['std_dev']} days")
        
        return duration_stats

    def generate_visualizations(self):
        if self.transactions_df.empty:
            print("Cannot generate visualizations: Data not loaded.")
            return

        df = self.transactions_df.copy()

        top_books = df['Book_Title'].value_counts().head(5)
        plt.figure(figsize=(8,5))
        sns.barplot(x=top_books.values, y=top_books.index, palette="viridis")
        plt.title('Top 5 Most Borrowed Books')
        plt.xlabel('Number of Borrowings')
        plt.ylabel('Book Title')
        plt.show()

        df['Month'] = df['Date'].dt.to_period('M')
        monthly_trends = df.groupby('Month').size()
        plt.figure(figsize=(8,5))
        sns.lineplot(x=monthly_trends.index.astype(str), y=monthly_trends.values, marker='o', color='darkorange')
        plt.title('Monthly Borrowing Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Borrowings')
        plt.xticks(rotation=45)
        plt.show()

        genre_counts = df['Genre'].value_counts()
        plt.figure(figsize=(6,6))
        plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)
        plt.title('Distribution of Books Borrowed by Genre')
        plt.show()

        df['Day'] = df['Date'].dt.day_name()
        df['Hour_Group'] = df['Date'].dt.hour // 3 * 3
        heatmap_data = df.groupby(['Day', 'Hour_Group']).size().unstack(fill_value=0)
        
        day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        heatmap_data = heatmap_data.reindex(day_order).fillna(0)
        
        plt.figure(figsize=(10,6))
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu')
        plt.title('Borrowing Activity by Day and Time (3-hour blocks)')
        plt.xlabel('Hour Block')
        plt.ylabel('Day of Week')
        plt.show()


dashboard = LibraryDashboard()

while True:
    print("Welcome to E-Library Data Insights Dashboard")

    print("1. Load Data")
    print("2. calculate statistics")
    print("3. filter transactions")
    print("4. generate report")
    print("5. calculate duration statistics")
    print("6. generate_visualizations")
    print("7. Exit")
    
    choice=int(input("Enter your choice : "))
    if choice==1:
        file = input("Enter CSV file path: ")
        dashboard.load_data(file)

    elif choice==2:
        dashboard.calculate_statistics()
        
    elif choice==3:
        condition = input("Enter filter condition (example: Genre == 'Fiction' or Duration_Days > 10): ")
        filtered = dashboard.filter_transactions(condition)
        print(filtered)
        
    elif choice==4:
        dashboard.generate_report()
        
    elif choice==5:
        dashboard.calculate_duration_statistics()
        
    elif choice==6:
        dashboard.generate_visualizations()
        
    elif choice==7:
        print("Exiting")
        break
    
    else:
        print("Your choice is not valid!")
        break
    