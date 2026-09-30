# fitness tracker - main.py
import json
import os
from datetime import datetime

DATA_FILE = "fitness_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def calculate_bmi(weight, height):
    # height in cm
    h_m = height / 100
    bmi = weight / (h_m ** 2)
    return round(bmi, 2)

def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def add_workout():
    print("\n--- Add Today's Workout ---")
    workout_type = input("Workout type (e.g., Running, Gym, Yoga): ")
    duration = input("Duration in minutes: ")
    calories = input("Calories burned: ")
    weight = float(input("Your weight (kg): "))
    height = float(input("Your height (cm): "))

    bmi = calculate_bmi(weight, height)
    status = get_bmi_status(bmi)

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "workout": workout_type,
        "duration_min": duration,
        "calories": calories,
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "status": status
    }
    
    data = load_data()
    data.append(entry)
    save_data(data)
    print(f"\n✅ Saved! Your BMI: {bmi} ({status})")

def view_history():
    data = load_data()
    if not data:
        print("\nNo records yet.")
        return
    
    print("\n--- Workout History ---")
    for i, d in enumerate(data, 1):
        print(f"{i}. {d['date']} | {d['workout']} | {d['duration_min']}min | {d['calories']} cal | BMI: {d['bmi']} ({d['status']})")

def main():
    while True:
        print("\n===== FITNESS TRACKER =====")
        print("1. Add Workout")
        print("2. View History")
        print("3. Exit")
        choice = input("Choose (1-3): ")

        if choice == "1":
            add_workout()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Stay fit! Bye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
