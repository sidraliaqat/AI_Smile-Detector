import random
# Define sample space and weighted probabilities for each weather condition
sample_space = ["Sunny", "Cloudy", "Haze", "Rain", "Mostly Cloudy"]
probabilities = [0.4, 0.2, 0.1, 0.2, 0.1]  # Adjust these values to represent likely weather probabilities
# Number of days to forecast
days = 7
# Forecast function that uses weighted probabilities
def forecast_weather(days, sample_space, probabilities):
    forecast = []
    for _ in range(days):
        day_weather = random.choices(sample_space, probabilities)[0]
        forecast.append(day_weather)
    return forecast
# Probability calculation for each weather type
def probability_event(forecast, sample_space):
    probabilities = {}
    for weather_type in sample_space:
        probabilities[weather_type] = forecast.count(weather_type) / len(forecast)
    return probabilities

# Display the detailed forecast and probability summary for each weather type
def display_forecast_summary(forecast, sample_space):
    print("Weather Forecast for the Next 7 Days:")
    for i, weather in enumerate(forecast, 1):
        print(f"Day {i}: {weather}")
    
    # Calculate and print probabilities for each weather type
    weather_probabilities = probability_event(forecast, sample_space)
    print("\nSummary of Probabilities for Each Weather Type:")
    for weather_type, prob in weather_probabilities.items():
        print(f"{weather_type}: {prob:.2f}")

# Run the forecast simulation and display results
forecasted_weather = forecast_weather(days, sample_space, probabilities)
display_forecast_summary(forecasted_weather, sample_space)  # Pass sample_space here