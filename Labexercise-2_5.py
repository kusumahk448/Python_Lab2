from datetime import datetime, timedelta
import random

# Generate dummy weather data for demonstration
def generate_weather_data(start_date: datetime, end_date: datetime) -> list:
    data = []
    current_date = start_date
    while current_date <= end_date:
        entry = {
            'date': current_date.strftime('%Y-%m-%d'),
            'max_temp': round(random.uniform(10.0, 35.0), 1),  # Random max temp between 10°C and 35°C
            'min_temp': round(random.uniform(0.0, 25.0), 1),   # Random min temp between 0°C and 25°C
            'humidity': random.randint(30, 100)                  # Random humidity between 30% and 100%
        }
        data.append(entry)
        current_date += timedelta(days=1)
    return data

# Function to find highest and lowest temperatures
def find_temp_extremes(weather_data: list) -> tuple:
    max_temp = max(entry['max_temp'] for entry in weather_data)
    min_temp = min(entry['min_temp'] for entry in weather_data)
    return max_temp, min_temp

# Function to determine number of days with temperatures above 30°C
def count_hot_days(weather_data: list) -> int:
    return sum(1 for entry in weather_data if entry['max_temp'] > 30)

# Function to compute average humidity
def average_humidity(weather_data: list) -> float:
    total_humidity = sum(entry['humidity'] for entry in weather_data)
    return total_humidity / len(weather_data)

def display_menu():
    print("\n--- Weather Data Analysis Menu ---")
    print("1. Find highest and lowest temperatures")
    print("2. Count the number of days with temperatures above 30°C")
    print("3. Compute the average humidity")
    print("4. Exit")

def main():
    # Define the date range
    start_date = datetime(2023, 8, 1)
    end_date = datetime(2024, 7, 10)
    
    # Generate weather data
    weather_data = generate_weather_data(start_date, end_date)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            highest_temp, lowest_temp = find_temp_extremes(weather_data)
            print(f"Highest Temperature Recorded: {highest_temp}°C")
            print(f"Lowest Temperature Recorded: {lowest_temp}°C")
        
        elif choice == '2':
            hot_days_count = count_hot_days(weather_data)
            print(f"Number of Days with Temperature Above 30°C: {hot_days_count}")
        
        elif choice == '3':
            avg_humidity = average_humidity(weather_data)
            print(f"Average Humidity Over the Period: {avg_humidity:.2f}%")
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
