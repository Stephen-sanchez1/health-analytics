import pandas as pd
import numpy as np

# Variables
blood_sugar_today = 165  # blood sugar level in mg/dL
blood_sugar_past_week = [150, 140, 138, 155, 160, 170, 162]
time_of_measurement = "2 hours after meal"  
sugar_data = {
    "morning": 130,
    "pre_meal": 110,
    "post_meal": 165,
}

# Function to analyze blood sugar levels
def blood_sugar_analysis(level):
    if level < 70:
        return "Your blood sugar is low. Consider having a snack."
    elif level <= 180:
        return "Your blood sugar is normal."
    else:
        return "Your blood sugar is high. Drink water and monitor."

# Analyzing blood sugar level
sugar_feedback = blood_sugar_analysis(blood_sugar_today)

# Print statements
print("Blood sugar level today:", blood_sugar_today, "mg/dL")
print("Time of measurement:", time_of_measurement)
print("Average blood sugar level over the past week:", round(sum(blood_sugar_past_week) / len(blood_sugar_past_week), 2), "mg/dL")
print("Sugar data for today:", sugar_data)
print("Blood Sugar Analysis:", sugar_feedback)

