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
            print("Cannot calculate statistics: Data not loaded or is empty.")
            return                 
           
        df = self.transactions_df.copy()
        
        most_borrowed = df['Book_Title'].value_counts().idxmax()
        most_borrowed_count = df['Book_Title'].value_counts().max()
        self.statistics['most_borrowed_book'] = most_borrowed
        self.statistics['most_borrowed_count'] = int(most_borrowed_count)    
        
        df['Date_Only'] = df['Date'].dt.date
        busiest_day = df['Date_Only'].value_counts().idxmax()
        busiest_day_count = df['Date_Only'].value_counts().max()
        self.statistics['busiest_day_date'] = str(busiest_day)
        self.statistics['busiest_day_count'] = int(busiest_day_count)      
                    
        duration_array = df['Duration_Days'].values.astype(float)

        self.statistics['duration_stats'] = {
            'count': int(len(duration_array)),
            'mean': np.mean(duration_array).round(2),
            'median': np.median(duration_array).round(2),
            'std_dev': np.std(duration_array).round(2),
            'min': np.min(duration_array).round(2),
            'max': np.max(duration_array).round(2)
        }
        self.statistics['avg_borrowing_time'] = self.statistics['duration_stats']['mean']
        
        self.statistics['total_borrowings_per_book'] = df.groupby('Book_Title').size().sort_values(ascending=False)
        self.statistics['borrowings_by_genre'] = df.groupby('Genre').size().sort_values(ascending=False)
        self.statistics['borrowings_by_month'] = df.set_index('Date').resample('M').size()
        
        print("Comprehensive statistics and aggregations calculated.")
      
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
        self.calculate_statistics()                

        if self.transactions_df.empty:
            print("\n--- Library Analysis Report ---")
            print("REPORT UNAVAILABLE: No data loaded.")
            return
        
        print("\n" + "="*70)
        print("Library Data Analysis Report - Comprehensive Summary")
        print("="*70)
        
        print("\nData Overview")
        total_transactions = len(self.transactions_df)
        total_unique_books = self.transactions_df['Book_Title'].nunique()
        total_unique_members = self.transactions_df['User_ID'].nunique()

        print(f"* Total Transactions Processed: **{total_transactions}**")
        print(f"* Total Unique Books: **{total_unique_books}**")
        print(f"* Total Unique Users: **{total_unique_members}**")

        print("\nKey Library Usage Statistics")
        stats = self.statistics
        
        if 'most_borrowed_book' in stats:
            print(f"1. **Most Borrowed Book:** '{stats['most_borrowed_book']}' (Borrowed **{stats['most_borrowed_count']}** times)")
        if 'busiest_day_date' in stats:
            print(f"2. **Busiest Day:** **{stats['busiest_day_date']}** (Total Transactions: **{stats['busiest_day_count']}**)")     
        
        print("\nBorrowing Duration Statistics (in Days)")
        duration_stats = self.statistics.get('duration_stats')
        if duration_stats:
            print(f"| Metric | Value (Days) |")
            print(f"| :--- | :--- |")
            print(f"| **Average Duration** | **{duration_stats['mean']}** |")
            print(f"| Median Duration | {duration_stats['median']} |")
            print(f"| Std. Deviation | {duration_stats['std_dev']} |")
            print(f"| Min / Max Duration | {duration_stats['min']} / {duration_stats['max']} |")  

        print("\nTop Aggregated Metrics")

        print("Top 5 Borrowed Books")
        top_books_df = self.statistics.get('total_borrowings_per_book', pd.Series()).head(5)
        print(top_books_df.to_frame('Borrow Count').to_markdown(numalign="left", stralign="left"))

        print("\nBorrowings by Genre")
        genre_df = self.statistics.get('borrowings_by_genre', pd.Series())
        print(genre_df.to_frame('Borrow Count').to_markdown(numalign="left", stralign="left"))

        print("\n" + "="*70)
        print("Analysis Complete. The graphical trends are also displayed.")
        print("="*70)

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

        print("\nGenerating Visualizations...")
        
        df = self.transactions_df.copy()

        fig, axes = plt.subplots(2, 2, figsize=(18, 14))
        plt.suptitle('Library Transaction Trends Analysis', fontsize=20, y=1.02)
        
        top_5_books = self.statistics['total_borrowings_per_book'].head(5)
        sns.barplot(x=top_5_books.values, y=top_5_books.index, ax=axes[0, 0], palette="viridis")
        axes[0, 0].set_title('A. Top 5 Most Borrowed Books', fontsize=14)
        axes[0, 0].set_xlabel('Number of Borrowings')
        axes[0, 0].set_ylabel('Book Title')
        
        monthly_trends = self.statistics['borrowings_by_month']
        monthly_trends.index = monthly_trends.index.strftime('%Y-%m') 
        
        sns.lineplot(x=monthly_trends.index, y=monthly_trends.values, marker='o', ax=axes[0, 1], color='darkorange')
        axes[0, 1].set_title('B. Monthly Borrowing Trend (Jan-Mar 2025)', fontsize=14)
        axes[0, 1].set_xlabel('Month (Year-Month)')
        axes[0, 1].set_ylabel('Total Borrowings')
        axes[0, 1].tick_params(axis='x', rotation=45)

        genre_counts = self.statistics['borrowings_by_genre']
        threshold = 0.10 * genre_counts.sum()
        small_genres = genre_counts[genre_counts < threshold]
        
        if len(small_genres) > 0:
            main_genres = genre_counts[genre_counts >= threshold]
            main_genres['Other'] = small_genres.sum()
        else:
            main_genres = genre_counts
            
        axes[1, 0].pie(main_genres, labels=main_genres.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'}, pctdistance=0.85, textprops={'fontsize': 10})
        axes[1, 0].set_title('C. Borrowing Distribution by Genre', fontsize=14)
        axes[1, 0].axis('equal') 
        
        df['Day_of_Week'] = df['Date'].dt.day_name()
        df['Hour_Group'] = df['Date'].dt.hour // 3 * 3 
        
        heatmap_data = df.groupby(['Day_of_Week', 'Hour_Group']).size().unstack(fill_value=0)
        
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        time_blocks = sorted(df['Hour_Group'].unique())

        heatmap_data = heatmap_data.reindex(index=day_order, columns=time_blocks, fill_value=0).astype(int)
        
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap="YlGnBu", cbar_kws={'label': 'Total Borrowings'}, ax=axes[1, 1], linewidths=.5, linecolor='lightgray')
        axes[1, 1].set_title('D. Borrowing Activity by Day and Time (3-hour blocks)', fontsize=14)
        axes[1, 1].set_xlabel('Time Block (Hour Start)')
        axes[1, 1].set_ylabel('Day of Week')

        plt.tight_layout(rect=[0, 0, 1, 0.98])
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
        dashboard.load_data()
        
    elif choice==2:
        dashboard.calculate_statistics()
        
    elif choice==3:
        dashboard.filter_transactions()
        
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
    
  