from selenium import webdriver
class Test_Chrome():
    def launch_Chrome(self):
        # instantiate Chrome browser
        driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\romana\\1.Running Test On Browser\\Drivers\\chromedriver_103.0.exe")

Chrome_obj= Test_Chrome()
Chrome_obj.launch_Chrome()
