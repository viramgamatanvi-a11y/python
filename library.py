

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class FitnessDashboard:
    def _init_(self, file_name="gym_members_exercise_tracking_synthetic_data.csv"):
        self.file_name = file_name
        try:
            self.records = pd.read_csv(file_name)
        except FileNotFoundError:
            self.records = pd.DataFrame(columns=["Date", "Workout", "Time (Minutes)", "Calories"])
            self.records.to_csv(file_name, index=False)

    def add_entry(self, workout, time_spent, calories_burned):
        if time_spent <= 0 or calories_burned <= 0:
            print(" Time and calories must be greater than zero!")
            return

        log_row = {
            "Date": datetime.today().strftime("%Y-%m-%d"),
            "Workout": workout,
            "Time (Minutes)": time_spent,
            "Calories": calories_burned
        }

        self.records = pd.concat([self.records, pd.DataFrame([log_row])], ignore_index=True)
        self.records.to_csv(self.file_name, index=False)
        print(f"Added: {workout} - {time_spent} mins, {calories_burned} cal")

    def show_summary(self):
        if self.records.empty:
            print(" No records to display.")
            return

        total_calories = self.records["Calories"].sum()
        avg_time = self.records["Time (Minutes)"].mean()
        workout_count = self.records["Workout"].value_counts()

        print("\nProgress Report:")
        print(f"Total Calories Burned: {total_calories}")
        print(f"Average Session Time: {avg_time:.2f} mins")
        print("\nWorkout Frequency:\n", workout_count)

    def get_filtered_logs(self, workout=None, from_date=None, to_date=None):
        logs = self.records.copy()

        if workout:
            logs = logs[logs["Workout"].str.lower() == workout.lower()]
        if from_date:
            logs = logs[logs["Date"] >= from_date]
        if to_date:
            logs = logs[logs["Date"] <= to_date]

        return logs

    def plot_statistics(self):
        if self.records.empty:
            print(" No workout data to display.")
            return

       
        self.records["Date"] = pd.to_datetime(self.records["Date"], errors='coerce')
        self.records = self.records.sort_values("Date")

        plt.figure(figsize=(12, 8))

        # Bar Chart
        plt.subplot(2, 2, 1)
        sns.barplot(x="Workout", y="Time (Minutes)", data=self.records, estimator=sum, ci=None, palette="Set2")
        plt.title("Total Time per Workout")
        plt.xlabel("Workout Type")
        plt.ylabel("Total Minutes")

        # Line Chart 
        plt.subplot(2, 2, 2)
        daily_calories = self.records.groupby("Date")["Calories"].sum()
        plt.plot(daily_calories.index, daily_calories.values, marker="o", color="orange", linewidth=2)
        plt.title("Calories Burned Over Time")
        plt.xlabel("Date")
        plt.ylabel("Calories Burned")
        plt.grid(True)

        # Pie Chart
        plt.subplot(2, 2, 3)
        workout_counts = self.records["Workout"].value_counts()
        plt.pie(workout_counts.values, labels=workout_counts.index, autopct="%1.1f%%",
                startangle=90, colors=sns.color_palette("Set3"))
        plt.title("Workout Type Distribution")

        #Heatmap
        plt.subplot(2, 2, 4)
        corr = self.records[["Time (Minutes)", "Calories"]].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Time vs Calories Correlation")

        plt.tight_layout()
        plt.show()


if _name_ == "_main_":
    tracker = FitnessDashboard()

    while True:
        print("\n----- Health Tracking Menu -----")
        print("1. Add Workout")
        print("2. View Report")
        print("3. Search Logs")
        print("4. Show Graphs")
        print("5. Quit")

        option = input("Enter option: ")

        if option == "1":
            w = input("Enter workout type (Running, Yoga, Cycling, etc.): ")
            try:
                t = int(input("Enter duration (minutes): "))
                c = int(input("Enter calories burned: "))
                tracker.add_entry(w, t, c)
            except ValueError:
                print(" Enter valid numbers for time and calories.")

        elif option == "2":
            tracker.show_summary()

        elif option == "3":
            w = input("Filter by workout (or press Enter to skip): ")
            f_date = input("Start date (YYYY-MM-DD) or Enter: ")
            t_date = input("End date (YYYY-MM-DD) or Enter: ")
            results = tracker.get_filtered_logs(w if w else None,
                                                f_date if f_date else None,
                                                t_date if t_date else None)
            print("\nFiltered Logs:\n", results)

        elif option == "4":
            tracker.plot_statistics()

        elif option == "5":
            print(" Exiting dashboard. Goodbye!")
            break

        else:
            print(" Invalid option. Try again.")