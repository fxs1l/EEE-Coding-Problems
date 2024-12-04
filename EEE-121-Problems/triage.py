class Patient:
    def __init__(self, name, priority):
        """Initialization of the Patient object

        Args:
            name (string): The name of the patient, consists of alphabetical characters only.
            priority (int): The integer priority of the patient, from 1 to 4.
        """
        self.name = name
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        """Initialize the priority queue. It is up to you what kind of data structure you will use."""
        # Part A. Implement initialization of your priority queue
        self.queue = []
    def insert(self, patient):
        """Insert a new patient in the priority queue
            
        Args:
            patient (Patient): Inserts a new Patient object, defined above,
        """
        # print(f"Inserting {patient.name} to queue")
        if len(self.queue) == 0:
            # print(f"\tFirst in line")
            self.queue.append(patient)
        else:
            for i in range(len(self.queue)):
                curr_patient = self.queue[i]
                if patient.priority >= curr_patient.priority:
                    # Patient has less than or equal priority than the index")
                    if i+1 == len(self.queue):
                        # print(f"\t\t We are at the last so adding {patient.name} to the last")
                        self.queue.insert(i+1,patient)
                        # print(f"\t\t Queue now looks like this")
                        # self.print_queue()
                    continue
                else:
                    # Patient has more priority than the index, so inserting here")
                    self.queue.insert(i, patient)
                    # print(f"\t\t Queue now looks like this")
                    # self.print_queue()
                    break
            
            
        # Part B. Implement code for insertion

    def pop_highest_priority(self):
        """A combination of get highest priority and delete highest priority. This should return the next person in line if they exist otherwise, this should return an empty string ("").

        Returns:
            string: Return either a patient name or an empty string ("").
        """
        # Part C. Implement popping of the highest priority
        if len(self.queue) == 0:
            return ""
        else:
            patient = self.queue.pop(0)
            return patient.name

    def print_queue(self):
        """Print out the remainining patients in queue in order. Print out one patient name per line"""
        # Part D. Implement printing of the priority queue order
        for q in self.queue:
            print(q.name)


#### DO NOT MODIFY THE MAIN FUNCTION ####
if __name__ == "__main__":
    n = int(input())

    pq = PriorityQueue()

    print("Patients served:")
    for i in range(n):
        line = input()
        if line.isnumeric():
            patients_to_be_served = int(line)
            for i in range(patients_to_be_served):
                patient_name = pq.pop_highest_priority()
                if (
                    patient_name != ""
                ):  # If returned element is an empty string, then there are no more people in line so do not print
                    print(patient_name)
        else:
            name, priority = line.split(",")
            p = Patient(name, int(priority))
            pq.insert(p)

    print("Remaining:")
    pq.print_queue()
