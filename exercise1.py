temperature_in_celcius = float(input("What is temperature right now in celcius? "))
temperature_in_faranheit = (temperature_in_celcius * 9/5)+32
temperature_in_kelvin = temperature_in_celcius + 273.15
print(f"Right now, the temperature is {temperature_in_celcius:.2f} celcius, {temperature_in_faranheit:.2f} faranheit, {temperature_in_kelvin:.2f} kelvin")