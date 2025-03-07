import os
import torch
from torchvision import models, transforms
from PIL import Image
from sklearn.cluster import KMeans
import shutil


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


def main():
    image_folder = "H:\\kurnik\\b\\"
    output_folder = "H:\\kurnik\\out\\"
    num_clusters = 4  # Number of clusters

    # Load and preprocess images
    image_tensors, image_paths = load_and_preprocess_images(image_folder)

    # Load pre-trained model without the final classification layer
    model = models.resnet50(pretrained=True)
    model = torch.nn.Sequential(*(list(model.children())[:-1]))
    model.eval()

    # Extract features
    features = extract_features(image_tensors, model)

    # Cluster images
    clusters = cluster_images(features, num_clusters)

    # Copy images into cluster directories
    copy_images_to_clusters(image_paths, clusters, output_folder)


if __name__ == "__main__":
    main()
