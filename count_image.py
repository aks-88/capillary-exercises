import requests
from bs4 import BeautifulSoup
from time import sleep
import json
from random import choice
base_url = "https://unsplash.com/s/photos/blog"

print ("Running code")

def main():
    print ("count_image")
    response=requests.get(f"{base_url}")
    soup = BeautifulSoup(response.text, "html.parser")
    images= soup.find_all('img')
    print(f"Total image tag is: {len(images)}")



if __name__ == '__main__':
    main()
