device_status = "active"
temperature = 38  # Current temperature in Celsius

if device_status == "active":
    if temperature < 40:
        print("Heating up")
    elif 20 <= temperature <= 25:
        print("Maintaining temperature")
    else:
        print("Cooling down")
else:
    print("Device is inactive. No action taken.")