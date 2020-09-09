import math
from selenium import webdriver
import time

# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

try:
    input_1 = browser.find_element_by_css_selector('.btn')
    input_1.click()
    input_2 = browser.switch_to.alert
    input_2.accept()
    x_elem = browser.find_element_by_id("input_value").text
    x = x_elem

    def calc():
        return str(math.log(abs(12*math.sin(int(x)))))


    y = calc()
    func_number = browser.find_element_by_id('answer').send_keys(y)
    submit_final = browser.find_element_by_xpath('//button[@type="submit"]').click()



    time.sleep(6)
finally:
    time.sleep(2)
    browser.quit()


    #http://suninjuly.github.io/alert_redirect.html?






#     input_first_name = browser.find_element_by_css_selector('[name=firstname]')
#     input_first_name.send_keys('Aslan')
#     input_last_name = browser.find_element_by_css_selector('[name=lastname]')
#     input_last_name.send_keys('Usoyan')
#     input_email = browser.find_element_by_css_selector('[name=email]')
#     input_email.send_keys('gaga@yahoo.com')
#
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, 'get_method.py')
#     file_submit = browser.find_element_by_id('file')
#     file_submit.send_keys(file_path)
#     input_button = browser.find_element_by_css_selector('.btn.btn-primary')
#     input_button.click()
#
# finally:
#     time.sleep(5)
#     browser.quit()
