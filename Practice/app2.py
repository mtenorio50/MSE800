class bmi():
    def __init__(self, mass, height):
        self.mass = mass
        self.height = height

    def calculate(self):
        return (self.mass/(self.height**2))


def main():
    try:
        mass_input = float(input("Enter mass in kg: "))
        height_input = float(input("Enter height in meters: "))
        bmi_total = bmi(mass_input, height_input)
        print(f"BMI is: {bmi_total.calculate(): .2f}")
    except ValueError:
        print("Enter valid number!")


if __name__ == "__main__":
    main()
