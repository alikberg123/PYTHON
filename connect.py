from datetime import date, datetime
import requests
import time
from config import wsite


status = True
url = wsite
while status:
    requests.get(url)
    if requests.get(url).status_code == 200:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Done " + url + "\n")
        with open("sucess.txt", "a") as file:
            file.write(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Done " + url + "\n"
            )
    else:
        quit()        
    if __name__ == "__main__":
        print("main")