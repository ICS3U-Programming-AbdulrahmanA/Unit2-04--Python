#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/1/2025
# Program to calculate the area and circumference of a circle using math.pi
import math


def main():
    # Get radius from user
    radius = float(input("Enter the radius of the circle (in cm): "))

    # Calculate area and circumference
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius

    # Display results
    print(f"Area of the circle: {area:.2f} cm^2")
    print(f"Circumference of the circle: {circumference:.2f} cm")


if __name__ == "__main__":
    main()
