import requests
import os
import random
import json

#import access key and secret key variables for unsplash api from app.json file
# if local vazriables are used comment out the below code
with open('app.json') as f:
    data = json.load(f)
    ACCESS_KEY = data['unsplash']['accessKey']
    SECRET_KEY = data['unsplash']['secretKey']

# use access key and secret key stored locally
ACCESS_KEY = "your_access_key"
SECRET_KEY = "your_secret_key"

#Create a folder
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("Folder created successfully")
    else:
        print("Folder already exists")

def download_image(image_url, save_path, author=None):
    response = requests.get(image_url, headers={"Authorization": f"Client-ID {ACCESS_KEY}"})
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully and saved as {save_path}")
        return True
    else:
        print(f"Failed to download the image from {image_url}")
        return False

# Function to save author details in a text file
def save_author_details(folder_name, image_filename, author):
    file_path = os.path.join(folder_name, 'author_details.txt')
    with open(file_path, 'a') as file:
        file.write(f"{image_filename}: {author}\n")
    print(f"Author details saved in {file_path}")

while True:
    search_prompt = input("Enter the search prompt: ")
    folder_name = search_prompt.replace(" ", "_").lower()[0:10]
    create_folder(folder_name)
    image_count = random.randint(5, 10)
    image_api_url = f"https://api.unsplash.com/search/photos?query={search_prompt}&per_page={image_count}"
    response = requests.get(image_api_url, headers={"Authorization": f"Client-ID {ACCESS_KEY}"})
    if response.status_code == 200:
        images_data = response.json()["results"]
        for i, image_data in enumerate(images_data):
            image_url = image_data["urls"]["regular"]
            image_filename = f"{i+1}.jpg"
            image_save_path = os.path.join(folder_name, image_filename)
            author = image_data["user"]["name"]
            if download_image(image_url, image_save_path, author):
                save_author_details(folder_name, image_filename, author)
    else:
        print("Failed to fetch images from the Unsplash API.")
    user_choice = input("Do you want to search for another prompt? (y/n): ")
    if user_choice.lower() != 'y':
        break
