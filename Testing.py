import requests
from selenium import webdriver
import docker
client = docker.from_env()
chrome_path = "C:/Users/Shahar Reuven/Documents/שחר/Job/DevOps Expert/Lesson 4 - Testing/chromedriver.exe"
my_driver = webdriver.Chrome(executable_path=chrome_path)


# checks whether the app is up and running
def code_200_check(flask_url):
    response = requests.get(flask_url)
    try:
        response.status_code == 200
    except BaseException as e:
        print(e.args)


# checks if the container ids matches
def container_id_check(flask_url):
    my_driver.get(flask_url)
    running_cont = client.containers.list(filters={'name': "my-container"})
    expected = str(running_cont[0].id[:12])
    actual = my_driver.find_element_by_xpath("/html/body/b[1]").text
    assert expected == actual


code_200_check("http://localhost:9090")
container_id_check("http://localhost:9090")
