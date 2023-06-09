"""
AJ Clemendor ML - Seating

Devd as a gift for Mrs. Donaldson

2023
"""
import math

import numpy as np
import itertools
import random
import matplotlib.pyplot as plt
from ml_helpers import create_compatibility_model
from RetriveSheetInfo import RetrieveSheetInfo


class SeatStudents:

    def __init__(self, student_data):

        # Personal note why do my main classes always include the word "logic" in quotes?
        """
        Create student seating "Logic"
        :param student_data -> Should be in google form:
        """
        self.student_data = student_data
        self.num_students = len(student_data)
        self.compatibility_models = {}

    def preprocess_data(self):
        # create labels for pairs
        X = []
        y = []

        for pair in itertools.combinations(self.student_data, 2):
            features = self.extract_features(pair)
            label = self.create_label(pair)
            X.append(features)
            y.append(label)

        X = np.array(X)
        y = np.array(y)

        return X, y

    def extract_features(self, pair):
        # gut features
        features = []

        # gpa diff
        grade_diff = abs(pair[0]['current_grade'] - pair[1]['current_grade'])
        features.append(grade_diff)

        # concept gap
        difficult_concepts_similarity = len(set(pair[0]['difficult_concepts']) & set(pair[1]['difficult_concepts']))
        features.append(difficult_concepts_similarity)

        # strong concept gap
        best_concepts_similarity = len(set(pair[0]['best_concepts']) & set(pair[1]['best_concepts']))
        features.append(best_concepts_similarity)

        # working in groups pref
        group_work_preference_similarity = int(pair[0]['group_work_preference'] == pair[1]['group_work_preference'])
        features.append(group_work_preference_similarity)

        # sit close?
        glasses_similarity = int(pair[0]['glasses_or_need_close'] == pair[1]['glasses_or_need_close'])
        features.append(glasses_similarity)

        return features

    def create_label(self, pair):
        """
        Takes a pair of students and checks if they can sit near each other or if it will be a
        "Problem"

        :param pair:
        :return:
        """
        if set(pair[0]['prefer_not_to_sit_with']) & set(pair[1]['prefer_not_to_sit_with']):
            return 0
        else:
            return 1

    def visualize_seating_arrangement(self, seating_arrangement, num_rows, num_cols):
        # Calculate size of each cell
        cell_size = 10
        padding = 2
        total_width = num_cols * (cell_size + padding) + padding
        total_height = num_rows * (cell_size + padding) + padding

        # Initialize seating grid
        seating_grid = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]

        # Populate seating grid with student names
        for i, student in enumerate(seating_arrangement):
            row = i // num_cols
            col = i % num_cols
            seating_grid[row][col] = student['name']

        # Print seating arrangement
        print('+' + '-' * total_width + '+')
        for row in seating_grid:
            print('|', end='')
            for name in row:
                print(f'{name:^{cell_size}}|', end='')
            print('\n+' + '-' * total_width + '+')

    def optimize_seating_arrangement(self, iterations=1, num_trials=1):
        best_seating_arrangement = None
        best_score = -1

        for _ in range(iterations):
            trial_seating_arrangements = [self.generate_seating_arrangement() for _ in range(num_trials)]
            trial_scores = [sum(self.personalized_compatibility_score(student_id, seatmate_id)
                                for student_id, seatmate_id in zip(arrangement, arrangement[1:] + [arrangement[0]]))
                            for arrangement in trial_seating_arrangements]

            max_index = np.argmax(trial_scores)
            if trial_scores[max_index] > best_score:
                best_score = trial_scores[max_index]
                best_seating_arrangement = trial_seating_arrangements[max_index]

        return [self.student_data[student_id]['name'] for student_id in best_seating_arrangement]

    def personalized_compatibility_score(self, student_id, other_student_id):
        pair_features = self.extract_features((self.student_data[student_id], self.student_data[other_student_id]))
        model = self.compatibility_models[student_id]
        score = model.predict(np.array([pair_features]))[0][0]
        return score



    def train_personalized_compatibility_models(self, epochs=100, batch_size=32):
        self.compatibility_models = {}

        for student_id, student_info in enumerate(self.student_data):
            X, y = self.generate_personalized_training_data(student_id)
            model = create_compatibility_model()
            model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=0)
            self.compatibility_models[student_id] = model

    def generate_personalized_training_data(self, student_id):
        student_ids = list(range(self.num_students))
        student_ids.remove(student_id)

        X = []
        y = []

        for other_student_id in student_ids:
            pair_features = self.extract_features((self.student_data[student_id],
                                                   self.student_data[other_student_id]))
            X.append(pair_features)
            compatibility_label = self.create_label((self.student_data[student_id],
                                                     self.student_data[other_student_id]))
            y.append(compatibility_label)

        return np.array(X), np.array(y)

    def generate_seating_arrangement(self):
        arrangement = list(range(self.num_students))
        random.shuffle(arrangement)
        return arrangement


if __name__ == "__main__":
    sheet_info = RetrieveSheetInfo()
    student_data = sheet_info.get_student_data()
    seat_students = SeatStudents(student_data)

    # what you may want to tweak, lower epochs quicker runtime
    seat_students.train_personalized_compatibility_models(epochs=5, batch_size=32)

    optimal_seating_arrangement = seat_students.optimize_seating_arrangement(iterations=5, num_trials=1)
    print("Optimal seating arrangement:", optimal_seating_arrangement)

    seat_students.visualize_seating_arrangement(optimal_seating_arrangement)
    print("Done")