from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "http://73.48.250.41:60001/view2.html"
    cookies = [{'domain': '73.48.250.41', 'expiry': 1578833783, 'httpOnly': False, 'name': 'lxc_save', 'path': '/',
          'secure': False, 'value': 'admin%2C'},
         {'domain': '73.48.250.41', 'httpOnly': False, 'name': 'dvr_sensorcnt', 'path': '/', 'secure': False,
          'value': '4'},
         {'domain': '73.48.250.41', 'httpOnly': False, 'name': 'dvr_clientport', 'path': '/', 'secure': False,
          'value': '60001'},
         {'domain': '73.48.250.41', 'httpOnly': False, 'name': 'dvr_camcnt', 'path': '/', 'secure': False,
          'value': '8'},
               {'domain': '73.48.250.41', 'httpOnly': False, 'name': 'dvr_usr', 'path': '/', 'secure': False,
                'value': '8'},
               {'domain': '73.48.250.41', 'httpOnly': False, 'name': 'dvr_pwd', 'path': '/', 'secure': False,
                'value': '8'}
               ]
    # url_test = "http://31.168.242.85:60001/"
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)
    # WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td[2]/input')))
    # elem = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td[2]/input")
    # elem.click()
    # WebDriverWait(driver, 15)
    # print(driver.get_cookies())
