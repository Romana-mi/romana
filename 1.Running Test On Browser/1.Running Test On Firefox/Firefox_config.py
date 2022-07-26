from selenium import webdriver
class Test_Firefox():
    def launch_firefox(self):
        # instantiate firefox browser
        driver = webdriver.Firefox(executable_path="C:\\Users\\USER\\PycharmProjects\\romana\\1.Running Test On Browser\\Drivers\\geckodriver_0.31.0.exe")
        driver.get("https://google.com")
        driver.quit()
firefox_obj= Test_Firefox()
firefox_obj.launch_firefox()
