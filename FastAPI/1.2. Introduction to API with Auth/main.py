import argparse
import requests
import cv2
import fal_api
import plant_api

def main():
    # if len(sys.argv) > 1:
    #     input_string = ' '.join(sys.argv[1:])
    #     print("Input flower name:", input_string)
    # else:
    #     print("Please provide a string as input.")
    parser = argparse.ArgumentParser()
    parser.add_argument('--greeting', default='Hello My friend Your Fav Plants name is')
    parser.add_argument('--plantName', required=True, type=str)
    arguments = parser.parse_args()
    print('{}: {} \t input type:{}'.format(arguments.greeting, arguments.plantName, type(arguments.plantName)))
    plant_name = arguments.plantName

    prompt = f"put {plant_name} in the center of the image with a white background"
    url = fal_api.fal(prompt)
    response = requests.get(url)
    plant_file_address = "./res/plant_pic.jpg"

    if response.status_code == 200:
        with open(plant_file_address, 'wb') as f:
            f.write(response.content)
        print("Image downloaded as:", plant_name)
    else:
        print("Failed_Status code:", response.status_code)

    img = cv2.imread(plant_name)
    cv2.imshow("drawn plant", img)
    cv2.waitKey(0)
    plant_file_2_name = plant_api.plant(plant_file_address)
    print(f"your plant name: {plant_file_2_name}")

if __name__ == "__main__":
    main()