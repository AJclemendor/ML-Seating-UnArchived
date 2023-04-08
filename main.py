"""
AJ Clemendor ML - Seating

Devd as a gift for Mrs. Donaldson

2023
"""



from RetriveSheetInfo import RetrieveSheetInfo
from SeatStudents import SeatStudents

def main():

    ROWS = int(input("Enter Rows"))
    COLS = int(input("Enter Cols"))

    # Instantiate classes // get data
    retriever = RetrieveSheetInfo()
    student_data = retriever.student_data

    # instantiate seatstudents
    seater = SeatStudents(student_data)

    # fun ml preprocessing into a more "usable" form
    X, y = seater.preprocess_data()

    # train the compatibility model using the preprocessed data
    seater.train_personalized_compatibility_models(epochs=5, batch_size=32)

    # Optimize the seating arrangement using the trained compatibility model
    best_seating_arrangement = seater.optimize_seating_arrangement(iterations=10, num_trials=10)


    # Print the best seating arrangement as a tic-tac-toe grid
    print("Best seating arrangement:")
    num_rows = ROWS
    num_cols = COLS
    for i in range(num_rows):
        for j in range(num_cols):
            student_index = i * num_cols + j
            if student_index < len(best_seating_arrangement):
                student = best_seating_arrangement[student_index]
                print(student.ljust(20), end="")
            else:
                print("".ljust(20), end="")
        print("\n")


if __name__ == "__main__":
    main()
