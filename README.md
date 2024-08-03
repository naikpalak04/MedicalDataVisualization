## Introduction

The goal of this project is to develop an automated pipeline that fetches medical data from Snowflake, processes it using Python, and visualizes it using Tableau. This helps healthcare professionals and researchers to easily interpret complex medical data.


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/
    ```

2. Change to the project directory:

    ```bash
    cd medical-data-visualization
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update the Snowflake connection details in `scripts/snowflake_connection.py`.

2. Run the data transformation script to fetch and process the data:

    ```bash
    python scripts/data_transformation.py
    ```

3. Use the Tableau integration script to visualize the processed data:

    ```bash
    python scripts/tableau_integration.py
    ```

4. Alternatively, you can explore the data using the provided Jupyter notebook:

    ```bash
    jupyter notebook notebooks/data_analysis.ipynb
    ```