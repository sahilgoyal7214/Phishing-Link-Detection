# URL Analysis & Prediction Project

This project provides a framework for extracting features from URLs and using trained TensorFlow models to predict outcomes based on those features. 

## Overview

The project is designed to:
- **Extract URL Features:** The `url_feature.py` file defines functions to extract multiple features from a given URL—such as domain age, page rank (via an API), hyperlink counts, and more. These features serve as inputs for machine learning models .
- **Make Predictions:** Using the extracted features, the `inferences.py` file loads two different trained models (a standard model and a reinforcement learning-based model) and performs predictions on an input URL citeturn0file0.
- **Model Training:** `train.ipynb` Notebook for model training, experimentation, and analysis. This notebook includes code for preparing data, training the TensorFlow models, and evaluating their performance. 

## Features

- **Robust Feature Extraction:**  
  The extraction process gathers 19 different features from a URL such as:
  - Google index status
  - Page rank (via OpenPageRank API)
  - URL structure details (e.g., count of "www", digits ratio, slashes, etc.)
  - Domain-specific features (e.g., domain age, whether the domain is in the title, etc.)
  
- **Dual Model Prediction:**  
  The inferences script demonstrates how to:
  - Load a reinforcement learning model (`dqn_model.h5`).
  - Load a standard best model (`best_model.keras`).
  - Use both models to predict outputs based on extracted URL features.
  
- **API Integration:**  
  The project interfaces with external APIs (such as openpagerank.com and payapi.io) to fetch dynamic information like page rank and domain age.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sahilgoyal7214/Phishing-Link-Detection.git
   cd Phishing-Link-Detection
   ```

2. **Set Up a Virtual Environment (Optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   Install the required packages using pip. The project depends on libraries such as TensorFlow, NumPy, requests, BeautifulSoup4, and tldextract.
   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain API Keys:**
   - **OpenPageRank API Key:** Replace the placeholder key in `inferences.py` with your actual API key or adjust as needed.
   - **Additional API Setup:** If needed, review the functions in `url_feature.py` for any other external API endpoints and configure accordingly.

## Usage

### Running Inference

You can perform predictions on a given URL by running the inference script. For example, use the following command in your terminal:

```bash
python inferences.py <url>
```

- **Parameters:**
  - `<url>`: The URL you wish to analyze.
  - The script will automatically load both the reinforcement learning model and the standard model and output their respective predictions.

### Training the Model

- Open the `train.ipynb` notebook in Jupyter Notebook or JupyterLab.
- Follow the steps in the notebook to train a model using your dataset.
- The notebook includes code for data preprocessing, model training, evaluation, and saving the final model artifacts.

## File Structure

- **inferences.py**  
  Contains functions to load models, extract URL features, and perform predictions. The main script accepts a URL as an argument, performs feature extraction using `extract_features_from_url`, and outputs prediction results citeturn0file0.

- **url_feature.py**  
  Defines various helper functions used for feature extraction from URLs. This module handles tasks like:
  - Calculating ratios (e.g., digits in URL, hyperlinks ratios).
  - External API calls to fetch page rank and domain age.
  - Parsing and analyzing URL structure citeturn0file1.

- **train.ipynb**  
  A Jupyter Notebook that includes the steps required to train and evaluate your prediction models. (Ensure you have all the necessary data and dependencies installed to run this notebook.)

## Customization

- **API Keys & Endpoints:**  
  Edit the API keys and endpoints in `url_feature.py` and `inferences.py` according to your requirements.
  
- **Model Files:**  
  Ensure that `dqn_model.h5` and `best_model.keras` are correctly placed in the working directory when performing inferences.

- **Additional Features:**  
  Feel free to extend the feature extraction functions in `url_feature.py` or modify the prediction logic in `inferences.py` to cater to additional use cases.

