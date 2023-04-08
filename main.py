"""
AJ Clemendor ML - Seating

Devd as a gift for Mrs. Donaldson

2023
"""



from RetriveSheetInfo import RetrieveSheetInfo
from SeatStudents import SeatStudents

def main():
    # Instantiate classes // get data
    retriever = RetrieveSheetInfo()
    student_data = retriever.student_data

    # instantiate seatstudents
    seater = SeatStudents(student_data)

    # fun ml preprocessing into a more "usable" form
    X, y = seater.preprocess_data()

    # train the compatibility model using the preprocessed data
    seater.train_personalized_compatibility_models(epochs=100, batch_size=32)

    # Optimize the seating arrangement using the trained compatibility model
    best_seating_arrangement = seater.optimize_seating_arrangement(iterations=1000, num_trials=10)

    # Print the best seating arrangement -> TODO Change this imp in a visual update
    print("Best seating arrangement:")
    for student in best_seating_arrangement:
        print(student)


if __name__ == "__main__":
    main()
