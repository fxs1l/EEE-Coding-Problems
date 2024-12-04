class Food:
    def __init__(self, weight: float, energy_add: int, happiness_add: int):
        self.weight = weight # in kg
        self.energy_add = energy_add
        self.happiness_add = happiness_add

class Student:
    def __init__(self, student_number: int, name: str, weight: float):
        self.student_number = student_number
        self.name = name
        self.weight = weight  # in kg

    def eat(self, food: Food):
        # TODO: insert appropriate code here
        # print(f"{self.name} ate {food}.")
        self.weight += float(food.weight)

    def exercise(self, exercise: str):
        # TODO: insert appropriate code here
        # print(f"{self.name} did {exercise}.")
        self.weight -= float(0.50)

    def get_weight_in_grams(self):
        # TODO: insert appropriate code here
        # TODO: once done, remove line of code below
        return float(self.weight * (10**3))


class EEE111Student(Student):
    energy_level = 50
    happiness_level = 50

    def code_python(self):
        # TODO: insert appropriate code here
        # TODO: once done, remove line of code below
        self.energy_level -= 10
        self.happiness_level += 10

    def eat(self, food: Food):
        # TODO: insert appropriate code here
        # TODO: once done, remove line of code below
        self.happiness_level += food.happiness_add
        self.energy_level += food.energy_add
        Student.eat(self, food)

    def exercise(self, food: str):
        # TODO: insert appropriate code here
        # TODO: once done, remove line of code below
        self.happiness_level +=10
        self.energy_level -= 10
        Student.exercise(self, food)

    def display_state(self):
        print(
            f"Displaying stats for {self.name}, student number: {self.student_number}."
        )
        print(
            f"Energy level: {self.energy_level}, happiness level: {self.happiness_level}, weight: {self.weight}"
        )

if __name__ == "__main__":
    num_students = int(input("Enter the number of students: "))

    students = []
    for idx in range(num_students):
        # TODO: create new_student here
        student_number = idx + 1
        name = "Student" + str(student_number)
        weight = 50 + 0.5 * (student_number-1)
        new_student = EEE111Student(student_number, name, weight)
        students.append(new_student)

    food_choices = {
        "papaya": Food(weight=0.10, energy_add=10, happiness_add=5),
        "corn": Food(weight=0.20, energy_add=5, happiness_add=6),
    }
    # Students tasks
    weight, energy, happiness = 0, 0, 0
    for student in students:
        student_number = student.student_number
        if student_number % 2 == 0:
            student.eat(food_choices["corn"])
            student.code_python()
        if student_number % 2 != 0:
            student.eat(food_choices["papaya"])
            student.exercise("run") 
        if student_number % 7 == 0:
            student.eat(food_choices["papaya"])
            student.eat(food_choices["corn"])
        if student_number % 5 == 0:
            student.code_python()
            student.exercise("run") 

        weight += float(student.get_weight_in_grams())
        energy += float(student.energy_level)
        happiness += float(student.happiness_level)

    avg_weight = float(weight / num_students)
    avg_energy = float(energy / num_students)
    avg_happiness = float(happiness/ num_students)
    print(f"Average weight of all students is {avg_weight} g")
    print(f"Average energy of all students is {avg_energy}%")
    print(f"Average happiness of all students is {avg_happiness}%")
