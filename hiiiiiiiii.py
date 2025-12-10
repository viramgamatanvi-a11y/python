import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta

# Set plotting style for better visualization
sns.set_style("whitegrid")

class LibraryDashboard:
    """
    A comprehensive class for Library Management data analysis, 
    incorporating OOP, Pandas/NumPy computations, and Matplotlib/Seaborn visualization.
    """
    def __init__(self):
        self.transactions_df = pd.DataFrame()
        self.statistics = {}

    # =========================================================================
    # 1. LOAD AND CLEAN DATA (Pandas: Missing/Duplicate Handling)
    # =========================================================================
    def load_data(self, file_path):
        """
        Load, validate, and clean the dataset, handling missing/duplicate data entries.
        """
        print(f"Loading data from: {file_path}...")
        try:
            df = pd.read_csv(file_path)

            required_cols = ['transaction_type', 'transaction_date', 'title', 'return_date', 'member_id', 'genre', 'user_type']
            if not all(col in df.columns for col in required_cols):
                print(f"❌ Data validation failed: Missing required columns. Required: {required_cols}")
                return False

            # Convert date columns to datetime objects
            df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
            df['return_date'] = pd.to_datetime(df['return_date'], errors='coerce')
            
            # --- Handling Missing/Duplicate Data ---
            # 1. Drop duplicates
            initial_count = len(df)
            df.drop_duplicates(inplace=True)
            print(f"ℹ️ Removed {initial_count - len(df)} duplicate rows.")

            # 2. Handle missing essential dates
            df.dropna(subset=['transaction_date'], inplace=True)
            
            # 3. Fill missing categorical data
            df['genre'].fillna('Unknown', inplace=True)
            df['user_type'].fillna('General', inplace=True)
            
            self.transactions_df = df
            print("✅ Data loaded, cleaned (duplicates/missing), and validated successfully.")
            return True

        except FileNotFoundError:
            print(f"❌ Error: File not found at {file_path}")
            return False
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            return False

    # =========================================================================
    # 2. CALCULATE STATISTICS (NumPy: Duration Stats, Pandas: Aggregation)
    # =========================================================================
    def calculate_statistics(self):
        """
        Calculate key metrics: most borrowed book, busiest day, borrowing duration stats.
        Includes all requirements from point 1 and 3.
        """
        if self.transactions_df.empty:
            print("⚠️ Cannot calculate statistics: Data not loaded or is empty.")
            return

        df = self.transactions_df.copy()
        
        # --- 1. Basic Metrics (Most Borrowed Book, Busiest Day) ---
        borrow_df = df[df['transaction_type'] == 'Borrow']
        if not borrow_df.empty:
            self.statistics['most_borrowed_book'] = borrow_df['title'].value_counts().idxmax()
            self.statistics['most_borrowed_count'] = borrow_df['title'].value_counts().max()
        
        df['date_only'] = df['transaction_date'].dt.date
        if not df.empty:
            self.statistics['busiest_day_date'] = df['date_only'].value_counts().idxmax()
            self.statistics['busiest_day_count'] = df['date_only'].value_counts().max()
            
        # --- 2. Borrowing Duration Statistics (NumPy) ---
        completed_loans = df[
            (df['transaction_type'] == 'Borrow') & 
            (df['return_date'].notna())
        ].copy()
        
        if not completed_loans.empty:
            completed_loans['borrow_duration'] = (completed_loans['return_date'] - completed_loans['transaction_date']).dt.days
            duration_array = completed_loans['borrow_duration'].values.astype(float)
            
            self.statistics['duration_stats'] = {
                'count': int(len(duration_array)),
                'mean': np.mean(duration_array).round(2),
                'median': np.median(duration_array).round(2),
                'std_dev': np.std(duration_array).round(2),
                'min': np.min(duration_array).round(2),
                'max': np.max(duration_array).round(2)
            }
            self.statistics['avg_borrowing_time'] = self.statistics['duration_stats']['mean'] # For compatibility with old method name

        # --- 3. Aggregation (Grouping by Genre and User Type - Pandas) ---
        
        # Grouping: Total Borrowings Per Book
        self.statistics['total_borrowings_per_book'] = borrow_df.groupby('title').size().sort_values(ascending=False)
        
        # Grouping: Total Borrowings Per User Type
        self.statistics['borrowings_by_user_type'] = borrow_df.groupby('user_type').size().sort_values(ascending=False)
        
        print("✅ Comprehensive statistics and aggregations calculated.")


    def filter_transactions(self, condition):
        """
        Filter transactions based on a user-defined pandas query string.
        """
        if self.transactions_df.empty:
            print("⚠️ Cannot filter transactions: Data not loaded or is empty.")
            return pd.DataFrame()

        try:
            filtered_df = self.transactions_df.query(condition, engine='python')
            print(f"✅ Filter successful. Found {len(filtered_df)} transactions.")
            return filtered_df
        except Exception as e:
            print(f"❌ Error during filtering with condition '{condition}': {e}")
            return pd.DataFrame()

    # =========================================================================
    # 3. VISUALIZATION (Matplotlib & Seaborn - High Weightage)
    # =========================================================================
    def generate_visualizations(self):
        """
        Create and display insightful visualizations using Matplotlib and Seaborn.
        """
        if self.transactions_df.empty:
            print("⚠️ Cannot generate visualizations: Data not loaded.")
            return

        print("\n🎨 Generating Visualizations...")
        
        # Filter for 'Borrow' transactions as most visualizations focus on borrowing activity
        borrow_df = self.transactions_df[self.transactions_df['transaction_type'] == 'Borrow'].copy()
        if borrow_df.empty:
            print("⚠️ No borrow transactions found to visualize.")
            return

        # --- Setup Matplotlib Figure ---
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))
        plt.suptitle('Library Transaction Trends Analysis', fontsize=20, y=1.02)
        
        # ----------------------------------------
        # A. Bar Chart: Top 5 Most Borrowed Books
        # ----------------------------------------
        top_5_books = self.statistics['total_borrowings_per_book'].head(5)
        sns.barplot(x=top_5_books.values, y=top_5_books.index, ax=axes[0, 0], palette="viridis")
        axes[0, 0].set_title('Top 5 Most Borrowed Books', fontsize=14)
        axes[0, 0].set_xlabel('Number of Borrowings')
        axes[0, 0].set_ylabel('Book Title')
        
        # ----------------------------------------
        # B. Line Chart: Borrowing Trends Over Months
        # ----------------------------------------
        monthly_trends = borrow_df.set_index('transaction_date').resample('M').size()
        monthly_trends.index = monthly_trends.index.strftime('%Y-%m') # Format for x-axis
        
        sns.lineplot(x=monthly_trends.index, y=monthly_trends.values, marker='o', ax=axes[0, 1], color='darkorange')
        axes[0, 1].set_title('Monthly Borrowing Trend', fontsize=14)
        axes[0, 1].set_xlabel('Month (Year-Month)')
        axes[0, 1].set_ylabel('Total Borrowings')
        axes[0, 1].tick_params(axis='x', rotation=45)

        # ----------------------------------------
        # C. Pie Chart: Distribution of Books Borrowed by Genre
        # ----------------------------------------
        genre_counts = borrow_df['genre'].value_counts()
        axes[1, 0].pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'}, pctdistance=0.85, textprops={'fontsize': 10})
        axes[1, 0].set_title('Borrowing Distribution by Genre', fontsize=14)
        axes[1, 0].axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
        
        # ----------------------------------------
        # D. Heatmap: Borrowing Activity by Day and Time
        # ----------------------------------------
        borrow_df['day_of_week'] = borrow_df['transaction_date'].dt.day_name()
        borrow_df['hour_group'] = borrow_df['transaction_date'].dt.hour // 3 * 3 # Group hours into 3-hour bins (0-2, 3-5, etc.)
        
        # Create a pivot table for the heatmap
        heatmap_data = borrow_df.groupby(['day_of_week', 'hour_group']).size().unstack(fill_value=0)
        
        # Reorder days for sensible display
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        heatmap_data = heatmap_data.reindex(day_order, axis=0)

        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap="YlGnBu", cbar_kws={'label': 'Total Borrowings'}, ax=axes[1, 1], linewidths=.5, linecolor='lightgray')
        axes[1, 1].set_title('Borrowing Activity by Day and Time', fontsize=14)
        axes[1, 1].set_xlabel('Time Block (Hour)')
        axes[1, 1].set_ylabel('Day of Week')

        plt.tight_layout(rect=[0, 0, 1, 0.98])
        plt.show()


    # =========================================================================
    # 4. GENERATE REPORT (Summary)
    # =========================================================================
    def generate_report(self):
        """
        Generate a summary report of the analysis.
        """
        # Ensure stats are calculated before generating the report
        self.calculate_statistics() 

        if self.transactions_df.empty:
            print("\n--- 📝 Library Analysis Report ---")
            print("❌ REPORT UNAVAILABLE: No data loaded.")
            return

        print("\n" + "="*60)
        print("📝 Library Data Analysis Report - Comprehensive Summary")
        print("="*60)
        
        # --- Data Overview ---
        print("\n## 📊 Data Overview & Cleaning")
        total_transactions = len(self.transactions_df)
        total_unique_books = self.transactions_df['title'].nunique()
        total_unique_members = self.transactions_df['member_id'].nunique()
        
        print(f"* Total Transactions Processed: **{total_transactions}**")
        print(f"* Total Unique Books: **{total_unique_books}**")
        print(f"* Total Unique Members: **{total_unique_members}**")

        # --- Key Statistics ---
        print("\n## 📈 Key Library Usage Statistics")
        stats = self.statistics
        
        if 'most_borrowed_book' in stats:
            print(f"1. **Most Borrowed Book:** '{stats['most_borrowed_book']}' (Borrowed **{stats['most_borrowed_count']}** times)")
        if 'busiest_day_date' in stats:
            print(f"2. **Busiest Day:** **{stats['busiest_day_date']}** (Total Transactions: **{stats['busiest_day_count']}**)")

        # --- Borrowing Duration Statistics (NumPy) ---
        print("\n## ⏳ Borrowing Duration Statistics (NumPy)")
        duration_stats = self.statistics.get('duration_stats')
        if duration_stats:
            print(f"| Metric | Value (Days) |")
            print(f"| :--- | :--- |")
            print(f"| **Average Duration** | **{duration_stats['mean']}** |")
            print(f"| Median Duration | {duration_stats['median']} |")
            print(f"| Std. Deviation | {duration_stats['std_dev']} |")
            print(f"| Total Completed Loans | {duration_stats['count']} |")
        else:
            print("No completed loans to show duration statistics.")
            
        # --- Aggregated Metrics (Pandas GroupBy) ---
        print("\n## 📚 Aggregated Group Metrics (Pandas)")

        print("### Top 3 Borrowings by User Type")
        user_type_df = self.statistics.get('borrowings_by_user_type', pd.Series()).head(3)
        print(user_type_df.to_markdown(numalign="left", stralign="left", headers=["User Type", "Borrow Count"]))

        print("\n### Top 3 Borrowed Genres")
        genre_df = self.transactions_df[self.transactions_df['transaction_type'] == 'Borrow']['genre'].value_counts().head(3)
        print(genre_df.to_frame('Borrow Count').to_markdown(numalign="left", stralign="left"))


        print("\n" + "="*60)
        print("🎉 Analysis Complete. Check the generated charts for visual trends.")
        print("="*60)


# --- Example Execution ---
if __name__ == "__main__":
    
    # ⚠️ IMPORTANT: Ensure the 'library_transactions.csv' file exists 
    # with the data structure provided above.
    
    FILE_PATH = 'library_transactions.csv'
    dashboard = LibraryDashboard()

    if dashboard.load_data(FILE_PATH):
        
        # Calculate all statistics and aggregations first
        dashboard.calculate_statistics()
        
        # Demonstrate filtering
        print("\n" + "-"*50)
        print("Filter Demonstration: Transactions for 'Student' user type")
        student_filter = dashboard.filter_transactions('user_type == "Student"')
        print(student_filter[['transaction_date', 'title', 'user_type']].head(3).to_markdown(index=False))
        print("-"*50)

        # Generate the full summary report (text output)
        dashboard.generate_report()
        
        # Generate and display all visualizations (graphical output)
        dashboard.generate_visualizations()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        





import pandas as pd
from datetime import timedelta

class LibraryDashboard:
    """
    A class to manage and analyze library transaction data.
    """
    def __init__(self):
        # Initialize an empty DataFrame to hold the transaction data
        self.transactions_df = pd.DataFrame()
        self.statistics = {}

    def load_data(self, file_path):
        """
        Load and Validate the dataset using Pandas.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            bool: True if data is loaded successfully and is valid, False otherwise.
        """
        print(f"Loading data from: {file_path}...")
        try:
            # 1. Load the dataset
            df = pd.read_csv(file_path)

            # 2. Basic Validation: Check for required columns
            required_cols = ['transaction_type', 'transaction_date', 'title', 'return_date']
            if not all(col in df.columns for col in required_cols):
                print(f"❌ Data validation failed: Missing required columns. Required: {required_cols}")
                return False

            # 3. Data Type Conversion and Cleaning
            # Convert date columns to datetime objects
            df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
            df['return_date'] = pd.to_datetime(df['return_date'], errors='coerce')

            # Filter out rows where transaction_date conversion failed
            df.dropna(subset=['transaction_date'], inplace=True)
            
            # Store the cleaned DataFrame
            self.transactions_df = df
            print("✅ Data loaded and validated successfully.")
            return True

        except FileNotFoundError:
            print(f"❌ Error: File not found at {file_path}")
            return False
        except pd.errors.EmptyDataError:
            print("❌ Error: The file is empty.")
            return False
        except Exception as e:
            print(f"❌ An unexpected error occurred during data loading: {e}")
            return False

    def calculate_statistics(self):
        """
        Calculate metrics like the most borrowed book, average borrowing time, and the busiest day.
        """
        if self.transactions_df.empty:
            print("⚠️ Cannot calculate statistics: Data not loaded or is empty.")
            return

        print("\nCalculating Library Statistics...")
        df = self.transactions_df.copy()
        
        # --- 1. Most Borrowed Book ---
        # Filter for 'Borrow' transactions and count unique titles
        borrow_df = df[df['transaction_type'] == 'Borrow']
        most_borrowed = borrow_df['title'].value_counts().idxmax()
        most_borrowed_count = borrow_df['title'].value_counts().max()

        # --- 2. Average Borrowing Time ---
        # Filter for 'Borrow' transactions that have a return date (i.e., completed loans)
        completed_loans = df[(df['transaction_type'] == 'Borrow') & (df['return_date'].notna())]
        
        if not completed_loans.empty:
            # Calculate the time difference (Borrowing Time) in days
            completed_loans['borrow_duration'] = (completed_loans['return_date'] - completed_loans['transaction_date']).dt.days
            average_borrow_time = completed_loans['borrow_duration'].mean()
        else:
            average_borrow_time = 0

        # --- 3. Busiest Day ---
        # Count transactions per day (date part only)
        df['date_only'] = df['transaction_date'].dt.date
        busiest_day_date = df['date_only'].value_counts().idxmax()
        busiest_day_count = df['date_only'].value_counts().max()
        
        # Store results
        self.statistics = {
            'most_borrowed_book': most_borrowed,
            'most_borrowed_count': most_borrowed_count,
            'average_borrow_time_days': round(average_borrow_time, 2),
            'busiest_day_date': busiest_day_date,
            'busiest_day_count': busiest_day_count
        }
        print("✅ Statistics calculated.")

    def filter_transactions(self, condition):
        """
        Filter transactions based on user-defined criteria.

        Args:
            condition (str): A pandas query string (e.g., 'genre == "Fiction"' or 
                             'transaction_date > "2023-10-15"').

        Returns:
            pd.DataFrame: A DataFrame containing the filtered transactions.
        """
        if self.transactions_df.empty:
            print("⚠️ Cannot filter transactions: Data not loaded or is empty.")
            return pd.DataFrame()

        print(f"\nFiltering transactions with condition: '{condition}'")
        try:
            # Use the .query() method for string-based filtering
            filtered_df = self.transactions_df.query(condition, engine='python')
            print(f"✅ Filter successful. Found {len(filtered_df)} transactions.")
            return filtered_df
        except Exception as e:
            print(f"❌ Error during filtering with condition '{condition}': {e}")
            return pd.DataFrame()

    def generate_report(self):
        """
        Generate a summary report of the analysis.
        """
        if not self.statistics:
            self.calculate_statistics() # Recalculate if not done

        if self.transactions_df.empty:
            print("\n--- 📝 Library Analysis Report ---")
            print("❌ REPORT UNAVAILABLE: No data loaded.")
            return

        print("\n--- 📝 Library Analysis Report ---")
        
        # --- Data Summary ---
        print("\n## Data Overview")
        total_transactions = len(self.transactions_df)
        total_unique_books = self.transactions_df['title'].nunique()
        total_unique_members = self.transactions_df['member_id'].nunique()
        
        print(f"* Total Transactions Processed: **{total_transactions}**")
        print(f"* Total Unique Books in Dataset: **{total_unique_books}**")
        print(f"* Total Unique Members in Dataset: **{total_unique_members}**")
        
        # --- Key Statistics ---
        print("\n## Key Usage Statistics")
        stats = self.statistics
        if stats:
            print(f"1. **Most Borrowed Book:** '{stats['most_borrowed_book']}' (Borrowed **{stats['most_borrowed_count']}** times)")
            print(f"2. **Average Borrowing Time:** **{stats['average_borrow_time_days']}** days")
            print(f"3. **Busiest Day:** **{stats['busiest_day_date']}** (Total Transactions: **{stats['busiest_day_count']}**)")
        else:
            print("⚠️ Statistics were not calculated.")

        # --- Genre Distribution ---
        print("\n## Genre Distribution (Top 3)")
        if 'genre' in self.transactions_df.columns:
            genre_counts = self.transactions_df['genre'].value_counts().head(3)
            print(genre_counts.to_string())
        else:
            print("Genre data not available in the dataset.")
        
        print("\n--- End of Report ---")

# --- Example Usage ---
if __name__ == "__main__":
    
    # NOTE: Ensure you have created the 'library_transactions.csv' file 
    # based on the sample structure provided above.
    
    dashboard = LibraryDashboard()
    file_path = 'library_transactions.csv'

    # 1. Load Data
    if dashboard.load_data(file_path):
        
        # 2. Calculate Statistics
        dashboard.calculate_statistics()
        
        # 3. Filter Transactions (Example 1: By Genre)
        fiction_transactions = dashboard.filter_transactions('genre == "Fiction"')
        if not fiction_transactions.empty:
            print("\n--- 📚 Fiction Transactions Sample (First 3) ---")
            print(fiction_transactions.head(3).to_markdown(index=False))

        # 4. Filter Transactions (Example 2: By Date Range)
        recent_transactions = dashboard.filter_transactions('transaction_date >= "2023-10-20"')
        if not recent_transactions.empty:
            print("\n--- 📅 Transactions since 2023-10-20 Sample (First 3) ---")
            print(recent_transactions.head(3).to_markdown(index=False))

        # 5. Generate Report
        dashboard.generate_report()
        
        
        
        







































import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# सेटिंग्स: बेहतर विज़ुअलाइज़ेशन के लिए
sns.set_style("whitegrid")

# आपके द्वारा प्रदान किया गया डेटा
csv_data = """Transaction ID,Date (YYYY-MM-DD),User ID,Book Title,Genre,Borrowing Duration (Days)
T001,2025-03-01,U156,AI Fundamentals,Technology,8
T002,2025-01-21,U126,Database SQL,Mystery,24
T003,2025-03-09,U105,Love Stories,Romance,8
T004,2025-03-21,U171,Data Science Intro,Technology,30
T005,2025-03-18,U160,Crime Thriller,Fiction,30
T006,2025-02-08,U167,Python Basics,History,10
T007,2025-02-26,U180,Ancient Civilizations,Technology,13
T008,2025-03-04,U166,Machine Learning Guide,Science,24
T009,2025-01-27,U133,Modern Tech,Mystery,21
T010,2025-02-24,U180,Robotics,Fiction,8
T011,2025-03-31,U124,Robotics,Technology,20
T012,2025-02-03,U131,Python Basics,Mystery,29
T013,2025-03-02,U193,Modern Tech,History,25
T014,2025-01-04,U119,World History,Fiction,9
T015,2025-01-06,U126,AI Fundamentals,History,5
T016,2025-02-04,U129,Love Stories,History,24
T017,2025-03-03,U147,Mystery Case,Romance,7
T018,2025-03-25,U134,Crime Thriller,Romance,5
T019,2025-01-08,U109,Data Science Intro,Science,13
T020,2025-03-09,U126,Mystery Case,Fiction,7
T021,2025-02-06,U194,Robotics,Mystery,17
T022,2025-02-13,U156,World History,Romance,21
T023,2025-02-18,U105,Love Stories,Technology,6
T024,2025-02-24,U107,Data Science Intro,Mystery,16
T025,2025-01-23,U159,AI Fundamentals,Science,20
T026,2025-01-06,U147,Love Stories,Romance,27
T027,2025-02-15,U134,Algorithm Design,History,26
T028,2025-01-08,U140,Space Science,History,16
T029,2025-03-10,U139,AI Fundamentals,Science,13
T030,2025-01-13,U193,Mystery Case,Science,14
T031,2025-02-21,U198,Robotics,Technology,16
T032,2025-03-08,U164,Python Basics,History,23
T033,2025-03-12,U123,Ancient Civilizations,Romance,11
T034,2025-01-05,U118,Modern Tech,Fiction,17
T035,2025-02-25,U144,Data Science Intro,Fiction,29
T036,2025-01-21,U136,Python Basics,Technology,29
T037,2025-03-17,U102,Machine Learning Guide,Fiction,20
T038,2025-02-17,U116,Space Science,Mystery,17
T039,2025-03-09,U125,AI Fundamentals,Romance,15
T040,2025-02-17,U172,Mystery Case,Science,11
T041,2025-03-15,U137,Data Science Intro,Technology,12
T042,2025-03-16,U116,Love Stories,Science,8
T043,2025-03-28,U147,Love Stories,Romance,13
T044,2025-01-21,U186,Crime Thriller,Mystery,11
T045,2025-03-21,U182,Space Science,Mystery,29
T046,2025-01-02,U105,AI Fundamentals,Technology,20
T047,2025-01-27,U116,Python Basics,History,11
T048,2025-02-01,U138,Robotics,History,21
T049,2025-03-13,U155,Mystery Case,Fiction,11
T050,2025-01-01,U190,Crime Thriller,Science,7
T051,2025-01-15,U175,Space Science,Mystery,29
T052,2025-03-14,U105,Mystery Case,Science,30
T053,2025-03-08,U180,Database SQL,Science,18
T054,2025-02-15,U182,Machine Learning Guide,Mystery,7
T055,2025-03-01,U124,Database SQL,Romance,28
T056,2025-02-24,U183,Algorithm Design,Science,23
T057,2025-01-05,U187,Space Science,History,27
T058,2025-03-24,U197,Crime Thriller,Fiction,11
T059,2025-02-11,U186,Deep Learning,Fiction,18
T060,2025-03-18,U167,Deep Learning,History,8
T061,2025-03-02,U125,Mystery Case,History,9
T062,2025-03-11,U134,Robotics,History,8
T063,2025-01-24,U110,Mystery Case,Romance,11
T064,2025-03-07,U171,Python Basics,Mystery,5
T065,2025-01-21,U100,AI Fundamentals,History,17
T066,2025-02-22,U185,World History,Science,10
T067,2025-02-25,U136,Robotics,Science,20
T068,2025-01-24,U158,Space Science,Technology,20
T069,2025-02-27,U129,Space Science,History,5
T070,2025-01-14,U135,Deep Learning,Fiction,30
T071,2025-03-24,U106,Crime Thriller,Romance,18
T072,2025-03-18,U191,Mystery Case,Fiction,12
T073,2025-03-22,U154,Python Basics,Fiction,14
T074,2025-03-30,U176,Deep Learning,Mystery,8
T075,2025-02-09,U185,World History,History,28
T076,2025-01-06,U114,Deep Learning,Technology,21
T077,2025-02-21,U143,Crime Thriller,History,25
T078,2025-03-05,U105,Ancient Civilizations,History,8
T079,2025-03-04,U105,Algorithm Design,Technology,16
T080,2025-02-10,U144,Love Stories,Fiction,21
T081,2025-01-15,U141,Modern Tech,Technology,6
T082,2025-02-17,U127,Robotics,Science,30
T083,2025-03-19,U127,Algorithm Design,Romance,11
T084,2025-02-12,U127,Mystery Case,Technology,14
T085,2025-02-25,U117,Data Science Intro,History,17
T086,2025-01-24,U185,Python Basics,Technology,29
T087,2025-03-10,U142,Crime Thriller,History,29
T088,2025-02-09,U132,Machine Learning Guide,Science,10
T089,2025-03-17,U198,Crime Thriller,Technology,22
T090,2025-02-22,U172,Machine Learning Guide,Science,19
T091,2025-02-12,U185,Love Stories,History,11
T092,2025-02-19,U145,Deep Learning,Fiction,21
T093,2025-01-08,U158,Mystery Case,Mystery,23
T094,2025-02-22,U103,Machine Learning Guide,Technology,26
T095,2025-03-19,U138,Deep Learning,Technology,17
T096,2025-01-31,U188,Deep Learning,Technology,27
T097,2025-03-04,U136,Robotics,Romance,22
T098,2025-02-13,U143,AI Fundamentals,Mystery,11
T099,2025-03-27,U189,AI Fundamentals,Mystery,20
T100,2025-03-20,U164,Deep Learning,Romance,22
T101,2025-02-07,U116,Algorithm Design,Science,5
T102,2025-03-22,U115,Crime Thriller,Mystery,10
T103,2025-02-18,U163,Data Science Intro,Mystery,14
T104,2025-03-28,U180,Crime Thriller,Science,26
T105,2025-03-25,U176,Ancient Civilizations,Romance,13
T106,2025-02-01,U133,AI Fundamentals,Science,18
T107,2025-02-21,U171,Robotics,Science,17
T108,2025-03-12,U123,World History,Mystery,5
T109,2025-03-22,U177,Algorithm Design,History,13
T110,2025-01-01,U133,Python Basics,Technology,30
T111,2025-02-18,U176,AI Fundamentals,Technology,20
T112,2025-03-04,U182,AI Fundamentals,History,11
T113,2025-03-25,U156,Database SQL,Technology,14
T114,2025-03-29,U139,Machine Learning Guide,Science,12
T115,2025-03-10,U135,Space Science,Science,20
T116,2025-01-25,U184,Mystery Case,Fiction,21
T117,2025-03-22,U160,Python Basics,Fiction,17
T118,2025-02-19,U190,Database SQL,Romance,6
T119,2025-03-16,U149,Ancient Civilizations,Fiction,19
T120,2025-01-27,U194,Robotics,Romance,20
T121,2025-03-19,U134,Space Science,History,18
T122,2025-01-23,U162,Database SQL,Science,6
T123,2025-01-15,U136,Algorithm Design,Technology,5
T124,2025-03-23,U180,Python Basics,Fiction,5
T125,2025-02-21,U177,Data Science Intro,Science,11
T126,2025-03-15,U115,Machine Learning Guide,Technology,16
T127,2025-03-15,U122,Crime Thriller,History,28
T128,2025-03-01,U118,Deep Learning,Technology,8
T129,2025-03-30,U170,Ancient Civilizations,History,14
T130,2025-01-10,U105,Data Science Intro,Fiction,30
T131,2025-01-15,U195,Crime Thriller,Mystery,14
T132,2025-01-20,U151,Data Science Intro,History,21
T133,2025-01-27,U133,Algorithm Design,Fiction,6
T134,2025-03-05,U104,Database SQL,Technology,12
T135,2025-03-08,U198,World History,Mystery,18
T136,2025-03-27,U166,Crime Thriller,Romance,29
T137,2025-02-10,U171,Database SQL,Romance,25
T138,2025-01-06,U170,Robotics,Fiction,30
T139,2025-03-27,U148,Mystery Case,Science,16
T140,2025-01-17,U169,Love Stories,Fiction,23
T141,2025-02-09,U108,Mystery Case,Fiction,9
T142,2025-03-08,U187,Modern Tech,Technology,5
T143,2025-02-13,U181,Love Stories,Fiction,10
T144,2025-01-19,U168,Robotics,History,10
T145,2025-01-24,U168,Deep Learning,Fiction,25
T146,2025-01-25,U165,Machine Learning Guide,Science,11
T147,2025-01-02,U133,Machine Learning Guide,Mystery,20
T148,2025-02-21,U111,Love Stories,Fiction,12
T149,2025-03-05,U141,Deep Learning,Science,10
T150,2025-01-24,U139,Ancient Civilizations,Fiction,13"""


class LibraryDashboard:
    """
    पुस्तकालय लेनदेन डेटा का विश्लेषण, सांख्यिकी और विज़ुअलाइज़ेशन के लिए क्लास।
    """
    def __init__(self):
        self.transactions_df = pd.DataFrame()
        self.statistics = {}

    def load_data(self, data_source):
        """डेटा को लोड, साफ और वैलिडेट करता है।"""
        print(f"Loading data...")
        try:
            # StringIO का उपयोग करके सीधे स्ट्रिंग से डेटा लोड करें
            df = pd.read_csv(StringIO(data_source))
            
            # कॉलम का नामकरण सरल करें
            df.columns = ['Transaction_ID', 'Date', 'User_ID', 'Book_Title', 'Genre', 'Duration_Days']
            
            # डेटा वैलिडेशन और सफाई
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            
            initial_count = len(df)
            df.drop_duplicates(inplace=True)
            print(f"ℹ️ Removed {initial_count - len(df)} duplicate rows.")

            # महत्वपूर्ण कॉलम में missing values (NaN) वाली rows को हटा दें
            df.dropna(subset=['Date', 'Book_Title', 'Duration_Days'], inplace=True)
            
            # Duration को integer में बदलें (यह मानते हुए कि कोई missing value नहीं है)
            df['Duration_Days'] = df['Duration_Days'].astype(int)
            
            self.transactions_df = df
            print(f"✅ Data loaded, cleaned, and validated successfully. Total transactions: {len(df)}")
            return True

        except Exception as e:
            print(f"❌ An unexpected error occurred during data loading: {e}")
            return False

    def calculate_statistics(self):
        """NumPy और Pandas का उपयोग करके प्रमुख मेट्रिक्स की गणना करता है।"""
        if self.transactions_df.empty:
            print("⚠️ Cannot calculate statistics: Data not loaded or is empty.")
            return

        df = self.transactions_df.copy()
        
        # 1. सबसे ज्यादा Borrow की गई किताब
        most_borrowed = df['Book_Title'].value_counts().idxmax()
        most_borrowed_count = df['Book_Title'].value_counts().max()
        self.statistics['most_borrowed_book'] = most_borrowed
        self.statistics['most_borrowed_count'] = int(most_borrowed_count)
        
        # 2. सबसे व्यस्त दिन (Busiest Day)
        df['Date_Only'] = df['Date'].dt.date
        busiest_day = df['Date_Only'].value_counts().idxmax()
        busiest_day_count = df['Date_Only'].value_counts().max()
        self.statistics['busiest_day_date'] = str(busiest_day)
        self.statistics['busiest_day_count'] = int(busiest_day_count)
        
        # 3. Borrowing Duration Statistics (NumPy)
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
        
        # 4. Aggregations (Pandas GroupBy)
        self.statistics['total_borrowings_per_book'] = df.groupby('Book_Title').size().sort_values(ascending=False)
        self.statistics['borrowings_by_genre'] = df.groupby('Genre').size().sort_values(ascending=False)
        self.statistics['borrowings_by_month'] = df.set_index('Date').resample('M').size()
        
        print("✅ Comprehensive statistics and aggregations calculated.")


    def filter_transactions(self, condition):
        """यूजर-डिफाइंड criteria के आधार पर transactions को फ़िल्टर करता है।"""
        if self.transactions_df.empty:
            print("⚠️ Cannot filter transactions: Data not loaded or is empty.")
            return pd.DataFrame()

        try:
            # Pandas query() का उपयोग करके फ़िल्टर करें
            filtered_df = self.transactions_df.query(condition, engine='python')
            print(f"✅ Filter successful with condition '{condition}'. Found {len(filtered_df)} transactions.")
            return filtered_df
        except Exception as e:
            print(f"❌ Error during filtering with condition '{condition}': {e}")
            return pd.DataFrame()

    def generate_visualizations(self):
        """Matplotlib और Seaborn का उपयोग करके विज़ुअलाइज़ेशन उत्पन्न करता है।"""
        if self.transactions_df.empty:
            print("⚠️ Cannot generate visualizations: Data not loaded.")
            return

        print("\n🎨 Generating Visualizations...")
        
        df = self.transactions_df.copy()

        fig, axes = plt.subplots(2, 2, figsize=(18, 14))
        plt.suptitle('Library Transaction Trends Analysis', fontsize=20, y=1.02)
        
        # A. Bar Chart: Top 5 Most Borrowed Books
        top_5_books = self.statistics['total_borrowings_per_book'].head(5)
        sns.barplot(x=top_5_books.values, y=top_5_books.index, ax=axes[0, 0], palette="viridis")
        axes[0, 0].set_title('A. Top 5 Most Borrowed Books', fontsize=14)
        axes[0, 0].set_xlabel('Number of Borrowings')
        axes[0, 0].set_ylabel('Book Title')
        
        # B. Line Chart: Borrowing Trends Over Months
        monthly_trends = self.statistics['borrowings_by_month']
        monthly_trends.index = monthly_trends.index.strftime('%Y-%m') 
        
        sns.lineplot(x=monthly_trends.index, y=monthly_trends.values, marker='o', ax=axes[0, 1], color='darkorange')
        axes[0, 1].set_title('B. Monthly Borrowing Trend (Jan-Mar 2025)', fontsize=14)
        axes[0, 1].set_xlabel('Month (Year-Month)')
        axes[0, 1].set_ylabel('Total Borrowings')
        axes[0, 1].tick_params(axis='x', rotation=45)

        # C. Pie Chart: Distribution of Books Borrowed by Genre
        genre_counts = self.statistics['borrowings_by_genre']
        # 10% से कम हिस्सेदारी वाले छोटे genres को 'Other' में समूहबद्ध करें
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
        
        # D. Heatmap: Borrowing Activity by Day and Time
        df['Day_of_Week'] = df['Date'].dt.day_name()
        # 3 घंटे के ब्लॉक में समय को समूहित करें
        df['Hour_Group'] = df['Date'].dt.hour // 3 * 3 
        
        # दिनों और घंटों के आधार पर counts की गणना करें
        heatmap_data = df.groupby(['Day_of_Week', 'Hour_Group']).size().unstack(fill_value=0)
        
        # दिनों और घंटों को क्रम में सेट करें
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        time_blocks = sorted(df['Hour_Group'].unique())

        heatmap_data = heatmap_data.reindex(index=day_order, columns=time_blocks, fill_value=0).astype(int)
        
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap="YlGnBu", cbar_kws={'label': 'Total Borrowings'}, ax=axes[1, 1], linewidths=.5, linecolor='lightgray')
        axes[1, 1].set_title('D. Borrowing Activity by Day and Time (3-hour blocks)', fontsize=14)
        axes[1, 1].set_xlabel('Time Block (Hour Start)')
        axes[1, 1].set_ylabel('Day of Week')

        plt.tight_layout(rect=[0, 0, 1, 0.98])
        plt.show() # ग्राफ को डिस्प्ले करें


    def generate_report(self):
        """सभी विश्लेषण का एक सारांश रिपोर्ट उत्पन्न करता है।"""
        self.calculate_statistics() 

        if self.transactions_df.empty:
            print("\n--- 📝 Library Analysis Report ---")
            print("❌ REPORT UNAVAILABLE: No data loaded.")
            return

        print("\n" + "="*70)
        print("📝 Library Data Analysis Report - Comprehensive Summary")
        print("="*70)
        
        # --- Data Overview ---
        print("\n## 📊 Data Overview")
        total_transactions = len(self.transactions_df)
        total_unique_books = self.transactions_df['Book_Title'].nunique()
        total_unique_members = self.transactions_df['User_ID'].nunique()
        
        print(f"* Total Transactions Processed: **{total_transactions}**")
        print(f"* Total Unique Books: **{total_unique_books}**")
        print(f"* Total Unique Users: **{total_unique_members}**")

        # --- Key Statistics ---
        print("\n## 📈 Key Library Usage Statistics")
        stats = self.statistics
        
        if 'most_borrowed_book' in stats:
            print(f"1. **Most Borrowed Book:** '{stats['most_borrowed_book']}' (Borrowed **{stats['most_borrowed_count']}** times)")
        if 'busiest_day_date' in stats:
            print(f"2. **Busiest Day:** **{stats['busiest_day_date']}** (Total Transactions: **{stats['busiest_day_count']}**)")

        # --- Borrowing Duration Statistics (NumPy) ---
        print("\n## ⏳ Borrowing Duration Statistics (in Days)")
        duration_stats = self.statistics.get('duration_stats')
        if duration_stats:
            print(f"| Metric | Value (Days) |")
            print(f"| :--- | :--- |")
            print(f"| **Average Duration** | **{duration_stats['mean']}** |")
            print(f"| Median Duration | {duration_stats['median']} |")
            print(f"| Std. Deviation | {duration_stats['std_dev']} |")
            print(f"| Min / Max Duration | {duration_stats['min']} / {duration_stats['max']} |")
            
        # --- Aggregated Metrics (Pandas GroupBy) ---
        print("\n## 📚 Top Aggregated Metrics")

        print("### Top 5 Borrowed Books")
        top_books_df = self.statistics.get('total_borrowings_per_book', pd.Series()).head(5)
        print(top_books_df.to_frame('Borrow Count').to_markdown(numalign="left", stralign="left"))

        print("\n### Borrowings by Genre")
        genre_df = self.statistics.get('borrowings_by_genre', pd.Series())
        print(genre_df.to_frame('Borrow Count').to_markdown(numalign="left", stralign="left"))

        print("\n" + "="*70)
        print("🎉 Analysis Complete. The graphical trends are also displayed.")
        print("="*70)


# --- Example Execution ---
dashboard = LibraryDashboard()

# 1. डेटा लोड करें (यह फ़ंक्शन स्ट्रिंग डेटा को स्वीकार करता है)
if dashboard.load_data(csv_data):
    
    # 2. रिपोर्ट और मुख्य सांख्यिकी उत्पन्न करें
    dashboard.generate_report()
    
    # 3. फ़िल्टरिंग का उदाहरण दिखाएं
    print("\n" + "-"*50)
    print("Filter Demonstration: Transactions with 'Technology' Genre and Duration > 15 days")
    # 'Genre == "Technology" and Duration_Days > 15'
    filtered_data = dashboard.filter_transactions('Genre == "Technology" and Duration_Days > 15')
    print(filtered_data[['Date', 'Book_Title', 'Genre', 'Duration_Days']].head().to_string(index=False))
    print("-"*50)
    
    # 4. विज़ुअलाइज़ेशन उत्पन्न करें
    dashboard.generate_visualizations()