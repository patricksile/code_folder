# Problem: Calculate BMI (8kyu)
"""
Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

if bmi <= 18.5 return "Underwei
ght"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""
# My Solution:

def bmi(weight, height):
    your_bmi = weight / (height ** 2)
    if your_bmi <= 18.5:
        return "Underweight"
    elif your_bmi <= 25.0:
        return "Normal"
    elif your_bmi <= 30.0:
        return "Overweight"
    elif your_bmi > 30:
        return "Obese"
