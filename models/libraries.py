import os
import cv2
import numpy as np
import joblib
from sklearn.neighbors import KNeighborsClassifier #Metode KNN (K-Nearest Neighbors)
from sklearn import svm #Metode SVM (Support Vector Machine)
from sklearn.ensemble import RandomForestClassifier #Metode Random Forest
from sklearn.tree import DecisionTreeClassifier #Metode Decision Tree
from sklearn.naive_bayes import GaussianNB #Metode Naive Bayes
from sklearn.linear_model import LogisticRegression #Metode Logistic Regression
from xgboost import XGBClassifier #Metode Gradient Boosting
from sklearn.preprocessing import LabelEncoder #Metode Gradient Boosting
from sklearn.ensemble import AdaBoostClassifier #Metode Ada Boost
from sklearn.neural_network import MLPClassifier #Metode Neural Network
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedShuffleSplit