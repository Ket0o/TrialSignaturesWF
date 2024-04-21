import os
import pickle
import cv2
import numpy as np
from skimage.feature import local_binary_pattern, hog
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.svm import SVC

class Signature_Authenticate:

    def __init__(self):
        super().__init__()
        current_directory = os.path.dirname(__file__)
        pca_path = os.path.join(current_directory, '..', '..', 'models', 'authenticate', 'trained_pca.pkl')
        classifier_path = os.path.join(current_directory, '..', '..', 'models', 'authenticate', 'signature_classifier.pkl')
        self.pca, self.classifier = self.load_model(pca_path, classifier_path)


    def load_signatures(self,directory):
        """Load signatures and differentiate between originals and forgeries."""
        originals = 'path_to_original.png'  # Путь к оригинальной подписи
        forgeries = 'path_to_test_signature.png'
        return originals, forgeries


    def preprocess_image(self,image_path):
        """Convert image to binary, remove noise, and resize."""
        try:
            image = Image.open(image_path).convert('L').resize((128, 128))
            image_np = np.array(image)
            _, binary_image = cv2.threshold(image_np, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            kernel = np.ones((2, 2), np.uint8)
            return cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")
            return None


    def extract_features(self,image):
        """Extract HOG and LBP features from an image."""
        if image is None:
            return None
        try:
            hog_features = hog(image, orientations=8, pixels_per_cell=(16, 16),
                               cells_per_block=(2, 2), block_norm='L2-Hys', visualize=False, feature_vector=True)
            lbp = local_binary_pattern(image, P=8, R=1, method="uniform")
            lbp_hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, 11), range=(0, 10))
            lbp_hist = lbp_hist.astype("float") / (lbp_hist.sum() + 1e-6)
            return np.hstack([hog_features, lbp_hist])
        except Exception as e:
            print(f"Feature extraction error: {e}")
            return None


    def load_model(self,pca_path, classifier_path):
        """ Load the PCA and classifier models from files. """
        with open(pca_path, 'rb') as f:
            pca = pickle.load(f)
        with open(classifier_path, 'rb') as f:
            classifier = pickle.load(f)
        return pca, classifier


    def preprocess_and_extract_features(self,image_path):
        """ Preprocess the image and extract features. """
        processed_image = self.preprocess_image(image_path)
        if processed_image is None:
            return None
        features = self.extract_features(processed_image)
        return features


    def authenticate_signature(self,original_sig_path, test_sig_path,  threshold=0.5):
        """
        Authenticate a signature by comparing the original with a test signature.
        """
        original_features = self.preprocess_and_extract_features(original_sig_path)
        test_features = self.preprocess_and_extract_features(test_sig_path)

        if original_features is None or test_features is None:
            print("Error in processing images.")
            return False

        # Applying PCA
        original_features_pca = self.pca.transform([original_features])
        test_features_pca = self.pca.transform([test_features])

        # Generating a feature vector for comparison
        comparison_vector = np.abs(original_features_pca - test_features_pca).flatten()

        # Predicting using the classifier
        prediction = self.classifier.predict([comparison_vector])[0]
        return prediction >= threshold

