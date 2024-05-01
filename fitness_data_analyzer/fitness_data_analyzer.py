def calculate_bmi(person_weight, person_height):
    """
    Calculates the Body Mass Index (BMI).
    `person_weight` parameter takes weight in kilograms,
    `person_height` parameter takes height in meters.
    BMI is calculated as follows:
    BMI = (person_weight / (person_height ** 2))
    """

    calculated_bmi = person_weight / (person_height ** 2)
    return calculated_bmi


def calculate_burned_calories(exercise_duration):
    """
    Calculates the estimated number of burned calories during the exercise.
    exercise_duration takes the duration of the exercise in minutes,
    burned_calories_per_minute is the average rate of calories burned per minute of exercise,
    total_calories_burned is calculated as multiply exercise_duration by average rate of calories burned per minute
    """

    burned_calories_per_minute = 7
    total_calories_burned = exercise_duration * burned_calories_per_minute
    return total_calories_burned


def filter_overweight_people(people_data_list):
    """
    Filter the overweight people based on BMI.
    `people_data_list` parameter takes a list of dictionaries containing information about each person
    including their weight and height. The function returns a filtered list of dictionaries with overweight people
    """

    overweight_people_list = []
    for current_person in people_data_list:
        current_bmi = calculate_bmi(current_person['weight'], current_person['height'])
        if current_bmi >= 25:
            overweight_people_list.append(current_person)
        return overweight_people_list


# Main program
people_data = []

while True:
    name = input("Enter person`s name ").strip()
    if not name:
        break

    try:
        weight = float(input("Enter person`s weight in kilograms: "))
        height = float(input("Enter person`s height in meters: "))
        duration = float(input("Enter exercise duration in minutes: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    person = {"name": name, "weight": weight, "height": height, "duration": duration}
    people_data.append(person)

print("\nFitness Analysis")
for person in people_data:
    bmi = calculate_bmi(person["weight"], person["height"])
    calories_burned = calculate_burned_calories(person["duration"])
    person["bmi"] = bmi
    person["calories_burned"] = calories_burned
    print(f"{person["name"]}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

overweight_people = filter_overweight_people(people_data)
print("\nOverweight People:")
for person in overweight_people:
    print(f"{person['name']}: BMI = {person['bmi']:.2f}")


