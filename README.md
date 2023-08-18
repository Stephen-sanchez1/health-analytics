# health-analytics
>This is a primer assignment for HHA 504/507

## Variables

1. `blood_sugar_today`: The current blood sugar level in mg/dL.
2. `blood_sugar_past_week`: A list containing blood sugar levels over the past week.
3. `time_of_measurement`: When the blood sugar was measured.
4. `sugar_data`: A dictionary containing blood sugar measurements at different times. 

## Function: blood_sugar_analysis(level)

This function takes a blood sugar level and returns a recommendation for the patient based on the level

- If the blood sugar level is less than 70, the function recommends having a snack to raise the blood sugar.
- If the blood sugar level is between 70 and 180 (inclusive), it indicates that the blood sugar is normal.
- If the blood sugar level is higher than 180, the function recommends drinking water and monitoring the situation.

### Expected Output

```python
Blood sugar level today: 165 mg/dL
Time of measurement: 2 hours after meal
Average blood sugar level over the past week: 153.57 mg/dL
Sugar data for today: {'morning': 130, 'pre_meal': 110, 'post_meal': 165}
Blood Sugar Analysis: Your blood sugar is normal.