import requests

image_data = open("./pics/car.jpg","rb").read()

response = requests.post("https://yolo-yrh27rcwya-el.a.run.app/v1/vision/detection",files={"image":image_data}).json()

print(response)