class Food:
    def __init__(self, weight: float, energy_add: int, happiness_add: int, cost: int):
        self.weight = weight # in kg
        self.energy_add = energy_add
        self.happiness_add = happiness_add
        self.cost = cost

class Student:
    def __init__(self, student_number: int, name: str, weight: float):
        self.student_number = student_number
        self.name = name
        self.weight = weight  # in kg

    def eat(self, food: Food):
        # print(f"{self.name} ate {food}.")
        self.weight += float(food.weight)

    def exercise(self, exercise: str):
        # print(f"{self.name} did {exercise}.")
        self.weight -= float(0.50)

    def get_weight_in_grams(self):
        return float(self.weight * (10**3))

class Employee:
    salary = 0 
    rate = 300 
    def work(self):
        self.salary += self.rate

class EEE111Student(Employee, Student ):
    energy_level = 50
    happiness_level = 50

    def code_python(self):
        self.energy_level -= 10
        self.happiness_level += 10
        

    def eat(self, food: Food):
        self.happiness_level += food.happiness_add
        self.energy_level += food.energy_add
        Student.eat(self, food)
        self.salary -= food.cost 

    def work(self):
        self.energy_level -= 10
        Employee.work(self)

    def exercise(self, food: str):
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
    food_choices = {
        "papaya": Food(weight=0.10, energy_add=10, happiness_add=5, cost=30),
        "corn": Food(weight=0.20, energy_add=5, happiness_add=6, cost=20),
        "rice": Food(weight=0.20, energy_add=5, happiness_add=5, cost=20),
        "adobo": Food(weight=0.30, energy_add=20, happiness_add=10, cost=40),
        "sinigang": Food(weight=0.40, energy_add=20, happiness_add=13, cost=50),
        "juice": Food(weight=0.50, energy_add=10, happiness_add=17, cost=20),
    }
    num_students = int(input("Enter the number of students: "))

    students = []
    for idx in range(num_students):
        # TODO: create new_student here
        # print(idx)
        student_number = idx + 1
        name = "Student" + str(student_number)
        weight = 50 + 0.5 * (student_number-1)
        new_student = EEE111Student(student_number, name, weight)
        students.append(new_student)

    set_meals = {
    0: ["rice", "adobo", "juice"],
    1: ["rice", "sinigang", "juice"],
    2: ["rice", "sinigang", "juice", "corn"],
    3: ["rice", "adobo", "juice", "papaya"],
    4: ["rice", "adobo", "juice", "papaya", "corn"],
    }
    weights, energies, happiness, salaries = 0, 0, 0, 0
    for idx, student in enumerate(students):
        student.work()
        meal = set_meals[(idx % 5)]
        for food in meal:
            student.eat(food_choices[food])

        if (idx+1) % 2 == 0:
            student.code_python()
        elif (idx+1) % 2 != 0:
            student.exercise("run")
        if (idx+1) % 13 != 0:
            student.eat(food_choices["juice"])

        weights += float(student.get_weight_in_grams())
        energies += float(student.energy_level)
        happiness += float(student.happiness_level)
        salaries += float(student.salary)

    avg_weight = float(weights / num_students)
    avg_energy= float(energies/ num_students)
    avg_happiness = float(happiness/ num_students)
    avg_salary= float(salaries/ num_students)

    print(f"Average weight of all students is {avg_weight} g")
    print(f"Average energy of all students is {avg_energy}%")
    print(f"Average happiness of all students is {avg_happiness}%")
    print(f"Average remaining salary of all students is PHP{avg_salary}")

