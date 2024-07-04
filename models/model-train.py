from libraries import *

# Set the path to the dataset directory
parent_dir = os.path.dirname(os.path.abspath(__file__))
dataset_dir = parent_dir + "\\preprocess_result\\"

# Initialize empty lists for storing training data and labels
train_data = []
train_labels = []

# Load training data
train_dir = os.path.join(dataset_dir, 'train')
for class_name in os.listdir(train_dir):
    class_dir = os.path.join(train_dir, class_name)
    for image_name in os.listdir(class_dir):
        image_path = os.path.join(class_dir, image_name)
        image = cv2.imread(image_path)
        image = cv2.resize(image, (64,64), interpolation=cv2.INTER_AREA)
        train_data.append(image.flatten())
        train_labels.append(class_name)
        #print(image.shape)

# Convert the lists to numpy arrays
train_data = np.array(train_data)
train_labels = np.array(train_labels)

# Initialize the SVM classifier
svm_classifier = svm.SVC(
    C=1.0,
    kernel="poly",
    gamma="auto",
    cache_size=500,
    degree=5,
    probability=True
)
svm_classifier.fit(train_data, train_labels)  # Train the classifier

model_and_encoder = {'model': svm_classifier, 'label_encoder': None}

try:
    # Save the trained model to a file
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trained_svm_model.pkl')
    print("success")
    joblib.dump(model_and_encoder, model_path)

    print(f"Model saved to {model_path}")
except Exception as e:
    print(e)
"""
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

def process_and_save_images(input_dir, output_dir):
    for class_name in os.listdir(input_dir):
        class_dir = os.path.join(input_dir, class_name)
        output_class_dir = os.path.join(output_dir, class_name)
        os.makedirs(output_class_dir, exist_ok=True)

        for image_name in os.listdir(class_dir):
            image_path = os.path.join(class_dir, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Apply preprocessing
            processed_image = preprocess_image(image)

            # Save processed image
            output_image_path = os.path.join(output_class_dir, image_name)
            cv2.imwrite(output_image_path, processed_image)
            print(f"Saved preprocessed image to {output_image_path}")

# Paths to dataset directories
train_dir = os.path.join(dataset_dir, "train")
test_dir = os.path.join(dataset_dir, "test")

# Output directory for preprocessed images
os.makedirs(parent_dir, exist_ok=True)

# Process and save train images
process_and_save_images(train_dir, os.path.join(parent_dir, "train"))

# Process and save test images
process_and_save_images(test_dir, os.path.join(parent_dir, "test"))

print("Preprocessing and saving completed.")
"""