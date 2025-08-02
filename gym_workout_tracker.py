# Write a program to help you track your workout routines, sets, reps, and weights. It lets you add exercises, 
# record your progress, and review past workouts. Perfect for gym users who want to log their progress.
class Exercise():
    def __init__(self, name):
        self.name = name
        self.workouts = []

    def add_session(self, sets, reps, weight):
        self.workouts.append({
            'sets': sets,
            'reps': reps,
            'weight': weight
        })

    def show_progress(self):
        if not self.workouts:
            print(f"No workouts logged for {self.name}.")
            return
        print(f"Progress for {self.name}:")
        for i, workout in enumerate(self.workouts, start=1):
            print(f"  Session {i}: {workout['sets']} sets, {workout['reps']} reps, {workout['weight']} kg")

    def __str__(self):
        return self.name
    
class GymTracker:
    def __init__(self):
        self.exercises = {}

    def add_exercise(self, name):
        if name in self.exercises:
            print(f"Exercise '{name}' already exists.")
        else:
            self.exercises[name] = Exercise(name)
            print(f"Exercise '{name}' added successfully.")
    
    def log_workout(self, name, sets, reps, weight):
        if name in self.exercises:
            self.exercises[name].add_session(sets, reps, weight)
            print(f"Workout logged for '{name}': {sets} sets, {reps} reps, {weight} kg.")
        else:
            print(f"Exercise '{name}' not found. Please add it first.")     
        
    def view_progress(self):
        if not self.exercises:
            print("No exercises logged yet.")
        else:
            for exercise in self.exercises.values():
                exercise.show_progress()

tracker = GymTracker()
while True:
    print("\nGym Tracker Options:")
    print("1. Add Exercise")
    print("2. Log workout")
    print("3. View progress")
    print("4. Exit")

    choice = input("Choice an option: ")

    if choice == "1":
        name = input("Enter exercise name: ")
        tracker.add_exercise(name)

    elif choice == "2":
        name = input("Enter exercise name: ").strip().capitalize()
        sets = int(input("Enter number of sets: "))
        reps = int(input("Enter number of reps: "))
        weight = float(input("Enter weight used (in kg): "))
        tracker.log_workout(name, sets, reps, weight)

    elif choice == "3":
        tracker.view_progress()
    
    elif choice == "4":
        print("Exiting the tracker. Keep up the good work!")
        break
    else:
        print("Invalid choice. Please try again.")