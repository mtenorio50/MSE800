import pandas as pd
import math


class DataProcess:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    # Read the file based on its extension
    def read_file(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        elif self.file_path.endswith('.txt'):
            with open(self.file_path, 'r') as file:
                self.data = file.read()
        else:
            raise ValueError("Unsupported file format")


class Calculator:
    def __init__(self):
        pass

    def get_user_input(self):
        self.radius = float(input("Enter the radius of the circle: "))
        self.angle = float(input("Enter the angle in degrees: "))

    def calculate_area_of_circle(self):
        area = math.pi * (self.radius ** 2)
        return area

    def calculate_sine(self):
        sine_value = math.sin(math.radians(self.angle))
        return sine_value

    def calculate_cosine(self):
        cosine_value = math.cos(math.radians(self.angle))
        return cosine_value


def main():
    # Example usage
    file_path = 'D:\\YooBee\\HelloWorld\\MSE800\\Week4\\sample_text.txt'
    data_processor = DataProcess(file_path)

    try:
        data_processor.read_file()
        print("Data read successfully.")
        print(data_processor.data)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

    calc = Calculator()
    calc.get_user_input()

    area = calc.calculate_area_of_circle()
    sine_value = calc.calculate_sine()
    cosine_value = calc.calculate_cosine()

    print(f"Area of the circle: {area:.2f}")
    print(f"Sine of the angle: {sine_value:.2f}")
    print(f"Cosine of the angle: {cosine_value:.2f}")


if __name__ == "__main__":
    main()
