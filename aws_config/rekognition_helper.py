import boto3
import os

# Initialize AWS Rekognition client
rekognition = boto3.client(
    "rekognition",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION", "us-east-1")
)

def analyze_image(image_path):
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()

    response = rekognition.detect_labels(
        Image={"Bytes": img_bytes},
        MaxLabels=10,
        MinConfidence=70
    )

    labels = []
    for label in response["Labels"]:
        labels.append({
            "Name": label["Name"],
            "Confidence": round(label["Confidence"], 2)
        })

    return labels
