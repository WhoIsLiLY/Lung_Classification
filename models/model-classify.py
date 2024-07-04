from libraries import *

def preprocess_image(image):
    #image

    # Apply histogram equalization
    # image_eq = cv2.equalizeHist(image)

    # Apply median filtering
    # image_median = cv2.medianBlur(image, 3)

    # # Apply Laplacian filter for edge enhancement
    laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
    enhanced_img = cv2.convertScaleAbs(image - laplacian)

    return enhanced_img

# Load the trained SVM model
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trained_svm_model.pkl')
model_and_encoder = joblib.load(model_path)

svm_classifier = model_and_encoder['model']
#if 
label_encoder = model_and_encoder['label_encoder']

# Load and preprocess the single image you want to classify
image_path = os.path.dirname(os.path.abspath(__file__)) + "\\predict_image\\"
result_path = os.path.dirname(os.path.abspath(__file__)) + "\\preprocessed_image\\"

# List all files in the image directory
files = os.listdir(image_path)
image_path_name = os.path.join(image_path, files[0])

image = cv2.imread(image_path_name)
image = preprocess_image(image)

cv2.imwrite(result_path+files[0], image)

# Perform any necessary preprocessing on the image here
image = cv2.resize(image, (64, 64), interpolation=cv2.INTER_AREA)

# Convert the image to a feature vector
image_flat = image.flatten()

# Classify the image using the trained SVM classifier
predicted_class = svm_classifier.predict([image_flat])

# Get the probability of the prediction
predicted_prob = svm_classifier.predict_proba([image_flat])

# Map the predicted class to its probability
predicted_class_label = predicted_class[0]  # This is the predicted class label
class_labels = svm_classifier.classes_  # This gives the array of class labels
predicted_class_index = list(class_labels).index(predicted_class_label)  # Find the index of the predicted class label
predicted_class_probability = predicted_prob[0][predicted_class_index]  # Fetch the probability using the index

# Print the predicted class and its probability
if label_encoder is None:
    print(predicted_class)
    print(predicted_class_probability * 100)
    print("-")
else:
    print(label_encoder.inverse_transform(predicted_class))
    print(predicted_class_probability * 100)
    print("Stratified Hold Out")

