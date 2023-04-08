2222# Machine Learning Seating Arrangement

This project aims to optimize the seating arrangement of students in a classroom using machine learning. It takes into account student preferences, academic performance, and other relevant features to generate a personalized seating arrangement that maximizes overall compatibility.


P.S. 

may want to tweak epoch count lower // group students instead of training a nn for each. Can take a long time to run depending on # of students. 
Stronger vs Weaker for speed vs complexity of chart


I also feel this could be done in 20 lines using GPT-4 API - May build just for fun

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/AJclemendor/ML-Seating.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up a Google Sheets API key and place the creds.json file in the project directory. For more information on how to set up Google Sheets API, please refer to this [guide](https://developers.google.com/sheets/api/guides/concepts).

4. Update the Google Sheet name in the RetrieveSheetInfo.py file with your own Google Sheet.

## Usage

After the installation, run the main.py script:

```bash
python main.py
```

This script will retrieve student data from the specified Google Sheet, preprocess the data, train personalized compatibility models, optimize the seating arrangement, and print the best seating arrangement.

You can also visualize the seating arrangement by running the SeatStudents.py script:

```bash
python SeatStudents.py
```

This will generate and display a visual representation of the optimal seating arrangement.

## Features

- Retrieves student data from a Google Sheet
- Preprocesses data to create feature vectors and labels for each pair of students
- Trains personalized compatibility models for each student
- Optimizes the seating arrangement using the trained compatibility models
- Visualizes the best seating arrangement

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b your-feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin your-feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.
