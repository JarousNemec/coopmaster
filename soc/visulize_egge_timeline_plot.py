import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

image_folder = "d:\\kurnik\\b\\"

import os
import torch
from torchvision import models, transforms
from PIL import Image
from sklearn.cluster import KMeans
import shutil
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

def load_and_preprocess_images(image_folder):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Resize images to 224x224 required by pre-trained models
        transforms.ToTensor(),  # Convert images to tensor
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize
    ])

    image_tensors = []
    image_paths = []

    for image_name in os.listdir(image_folder):
        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, image_name)
            image = Image.open(image_path).convert('RGB')
            image_tensor = transform(image)
            image_tensors.append(image_tensor)
            image_paths.append(image_path)

    return image_tensors, image_paths


def extract_features(image_tensors, model):
    with torch.no_grad():
        images_batch = torch.stack(image_tensors)
        features = model(images_batch)
    return features.squeeze()


def cluster_images(features, num_clusters=2):
    features_np = features.view(features.shape[0], -1).numpy()
    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(features_np)
    return clusters


def copy_images_to_clusters(image_paths, clusters, output_folder):
    clustered_image_paths = {i: [] for i in range(max(clusters) + 1)}
    for img_path, cluster_id in zip(image_paths, clusters):
        clustered_image_paths[cluster_id].append(img_path)

    for cluster_id, images in clustered_image_paths.items():
        cluster_folder = os.path.join(output_folder, f"cluster_{cluster_id}")
        os.makedirs(cluster_folder, exist_ok=True)
        for img_path in images:
            shutil.copy(img_path, cluster_folder)
            print(f"Copied {img_path} to {cluster_folder}")

def plot_feature_vectors(features, clusters):
    # Reduce the dimensionality of the features to 2D using PCA
    pca = PCA(n_components=2)
    features_2d = pca.fit_transform(features)

    # Plot each cluster with a different color
    unique_clusters = np.unique(clusters)
    plt.figure(figsize=(10, 7))

    for cluster_id in unique_clusters:
        indices = clusters == cluster_id
        plt.scatter(features_2d[indices, 0], features_2d[indices, 1], label=f'Chicken {cluster_id}')

    plt.title('Vizualizace vektorů')
    # plt.xlabel('PCA Component 1')
    # plt.ylabel('PCA Component 2')
    plt.legend()
    plt.show()

def main():
    output_folder = "d:\\kurnik\\out\\"
    num_clusters = 4  # Number of clusters

    # Load and preprocess images
    image_tensors, image_paths = load_and_preprocess_images(image_folder)

    # Load pre-trained model without the final classification layer
    model = models.resnet50(pretrained=True)
    model = torch.nn.Sequential(*(list(model.children())[:-1]))
    model.eval()

    # Extract features
    features = extract_features(image_tensors, model)

    # Convert features to a NumPy array
    features_np = features.view(features.shape[0], -1).numpy()

    # Cluster images
    clusters = cluster_images(features, num_clusters)

    # Visualize feature vectors as points
    plot_feature_vectors(features_np, clusters)

    # Copy images into cluster directories
    copy_images_to_clusters(image_paths, clusters, output_folder)

if __name__ == "__main__":
    main()

