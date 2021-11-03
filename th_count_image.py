import requests
from bs4 import BeautifulSoup
from time import sleep
import timeit
import threading
from concurrent.futures import ThreadPoolExecutor

base_urls = ["https://unsplash.com/s/photos/blog","https://unsplash.com/s/photos/blog", "https://unsplash.com/s/photos/blog", "https://unsplash.com/s/photos/blog", "https://unsplash.com/s/photos/blog", "https://unsplash.com/s/photos/blog", "https://unsplash.com/s/photos/blog", "https://unsplash.com/s/photos/blog", "https://unsplash.com/s/photos/blog", "https://unsplash.com/s/photos/blog","https://unsplash.com/s/photos/blog", "https://unsplash.com/s/photos/blog","https://unsplash.com/s/photos/blog","https://unsplash.com/s/photos/blog"]

print ("Running code")


def image_count(url):
    response=requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    images= soup.find_all('img')
    print(f"{url} : Total image tag is: {len(images)}")

def main():
    with ThreadPoolExecutor(50) as executor:
        for url in base_urls:
            future= executor.submit(image_count,url)  
    
    
         
    future.result()



if __name__ == '__main__':
    
    time_taken= timeit.timeit(main, number=1)
    print(f"thread time taken {time_taken}s")
