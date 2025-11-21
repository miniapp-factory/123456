def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def main() -> None:
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose conversion (1 or 2): ").strip()
    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
