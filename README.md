# Major1-Crop_Recommendation_System
## Overview

This project aims to develop a **Crop Recommendation System** tailored for Indian farmers. The system leverages machine learning models to analyze soil and environmental conditions, helping farmers make informed decisions about the best crops to grow in their fields.

## Features

- **Data-Driven Insights:** The system uses real-world data to recommend the most suitable crops based on soil composition, weather conditions, and other environmental factors.
- **User-Friendly Interface:** Easy to use for farmers with minimal technical knowledge.
- **Localized Recommendations:** The system is specifically designed to cater to the diverse agricultural landscapes across India.

## Files in the Repository

- **`app.py`**: The main application file that powers the Crop Recommendation System.
- **`crop_model.jpynb.ipynb`**: A Jupyter Notebook containing the machine learning model used to make crop recommendations.
- **`Crop_Recommendation.csv`**: The dataset used for training and testing the machine learning model.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Jupyter Notebook
- Required Python libraries: `pandas`, `numpy`, `scikit-learn`, `flask`, etc.

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/crop-recommendation-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd crop-recommendation-system
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Using Jupyter Notebook:**

   - Open the `crop_model.jpynb.ipynb` file in Jupyter Notebook.
   - Run the cells to load the data, train the model, and make predictions.

2. **Running the Flask Application:**

   - Execute the `app.py` file to start the web application:

     ```bash
     python app.py
     ```

   - The application will be available at `http://localhost:5000`, where you can input data and receive crop recommendations.

### Usage

- **Farmers** can input soil and environmental data into the system to receive recommendations on which crops to plant.
- **Agricultural Experts** can use this tool to analyze large datasets and provide consultation to farmers.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- **Indian Farmers**: The backbone of our project, providing the inspiration to create this system.
- **Open Source Libraries**: Tools like `pandas`, `scikit-learn`, and `Flask` have been instrumental in the development of this project.

---

You can customize the sections as needed, especially the links, and add any additional details specific to your project.