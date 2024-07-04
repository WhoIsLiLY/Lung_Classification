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


# Initialize empty lists for storing test data and labels
test_data = []
test_labels = []

# Load test data
test_dir = os.path.join(dataset_dir, "test")
for class_name in os.listdir(test_dir):
    class_dir = os.path.join(test_dir, class_name)
    for image_name in os.listdir(class_dir):
        image_path = os.path.join(class_dir, image_name)
        print(image_path)
        image = cv2.imread(image_path)
        image = cv2.resize(image, (64, 64), interpolation=cv2.INTER_AREA)
        test_data.append(image.flatten())
        test_labels.append(class_name)

# Convert the lists to numpy arrays
test_data = np.array(test_data)
test_labels = np.array(test_labels)

# Misalkan train_data dan train_labels adalah data pelatihan dan label yang sudah ada
# label_encoder digunakan untuk meng-encode label jika belum dilakukan
label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)

# Membagi dataset menggunakan Stratified Shuffle Split
sss = StratifiedShuffleSplit(n_splits=6, test_size=0.2, train_size=0.8, random_state=42)
for train_index, test_index in sss.split(train_data, train_labels_encoded):
    X_train, X_test = train_data[train_index], train_data[test_index]
    y_train, y_test = train_labels_encoded[train_index], train_labels_encoded[test_index]

# Inisialisasi KNN classifier
svm_classifier = svm.SVC(
    C=1.0,
    kernel="poly",
    gamma="auto",
    cache_size=500,
    degree=5,
    probability=True
)

# Melatih classifier
svm_classifier.fit(X_train, y_train)

model_and_encoder = {'model': svm_classifier, 'label_encoder': label_encoder}

try:
    # Save the trained model to a file
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trained_svm_model.pkl')
    print("success")
    joblib.dump(model_and_encoder, model_path)

    print(f"Model saved to {model_path}")
except Exception as e:
    print(e)