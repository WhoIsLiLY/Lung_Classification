# Lung Disease Classification using SVM (Flask App)

This project is a Flask-based web application designed to classify lung conditions from chest X-ray images. It uses a Support Vector Machine (SVM) model trained to distinguish between **COVID-19**, **pneumonia**, and **normal lungs**, achieving a classification accuracy of **96%** with specific preprocessing techniques.

## Features
- **Disease Classification**: The app predicts whether an input chest X-ray image shows signs of COVID-19, pneumonia, or a normal lung.
- **Trained Model**: The SVM model was trained on a dataset obtained from Kaggle, with robust preprocessing to improve classification accuracy.
- **High Accuracy**: The model achieves up to **96% accuracy** on the test set.
- **Web-Based Interface**: Users can upload chest X-ray images through a simple web interface built with Flask, and instantly receive classification results.

## Preprocessing Methods
The following preprocessing steps are applied to the input X-ray images to ensure optimal classification accuracy:
- **Median Blur**: Reduces noise in the images without blurring important edges, making it ideal for medical images like X-rays.
- **Histogram Equalization**: Enhances the contrast of the X-ray images, making lung features more distinguishable.
- **Laplacian Filter**: Sharpens the edges in the image, which helps the SVM model recognize important features such as lung structures more clearly.

These preprocessing steps significantly improve the model's performance, particularly the Laplacian filter, which gave the highest accuracy when used in combination with SVM.

## Model Details
- **Algorithm**: The classification model is based on **Support Vector Machine (SVM)** with a **polynomial kernel**.
- **Evaluation**: The dataset was split using **Stratified Hold-Out** validation to ensure an even distribution of classes (COVID-19, pneumonia, normal lungs) in both the training and test sets.
- **Accuracy**: The model achieved an accuracy of **96%** on the test set when using Laplacian-filtered images, outperforming other preprocessing combinations.
- **Comparison with Other Models**: Several other machine learning models, including **K-Nearest Neighbors (KNN)**, **Decision Trees**, and **Naive Bayes**, were tested but did not reach the same accuracy as the SVM model.

## Dataset
- **Source**: The dataset used for training and testing was obtained from Kaggle.
- **Classes**: The dataset contains chest X-ray images classified into three categories:
  - **COVID-19**
  - **Pneumonia**
  - **Normal lungs**
- **Partition**: The dataset consists of 317 images (111 COVID-19, 70 pneumonia, 70 normal) in the training set and 66 images (26 COVID-19, 20 pneumonia, 20 normal) in the test set.

## Setup Instructions

To run this project locally, follow these steps:

### Prerequisites
- Python 3.x
- Flask
- Numpy
- OpenCV
- Scikit-learn
- Xgboost

### Installation
1. Clone this repository:
   ```bash
   git clone [<repository-url>](https://github.com/WhoIsLiLY/Lung_Classification.git)
   cd lung-classification
   ```
## Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
## Install the required packages using pip install

## Run the Flask application:
```bash
python app.py
```

## USAGE
Once the application is running, open a browser and navigate to http://localhost:5000. You will be prompted to upload a chest X-ray image. After uploading, the app will classify the image as either normal, COVID-19, or pneumonia based on the trained SVM model.

## Model Training
If you wish to retrain the model, use the train_model.py script. This script preprocesses the dataset, extracts features, and trains the SVM model using the selected kernel.

## Results
The application’s model achieves:
- Accuracy: 96%
- Precision: 95%
- Recall: 96%
- F1 Score: 96%
These metrics demonstrate the robustness of the model and its effectiveness in classifying lung conditions based on X-ray images.

## Journal Reference
For a detailed explanation of the methodology, model training, and evaluation metrics, please refer to the attached journal paper [https://drive.google.com/drive/folders/1oJAwGifq8GWF10dVG0fq0dRhqkLDZOtF].

## License
This project is licensed under the MIT License. See the LICENSE file for details.
