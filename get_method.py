import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://masp-dev1.smartcom.software/#/login?redirect=%2Fmain%2F")
time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
#button_1 = driver.find_element_by_xpath('//button[@class="login_button_microsoft"]')
#button_1.Click()

time.sleep(5)

text_input_login = driver.find_element_by_name("loginfmt")
text_input_login.send_keys("ivan.obraztsov@smartcom.software")

time.sleep(3)

button_next = driver.find_element_by_id("idSIButton9")
button_next.click()

time.sleep(5)

button_password = driver.find_element_by_id("i0118")
button_password.send_keys("iyYAzcF4e")



button_exit = driver.find_element_by_id("idSIButton9")
button_exit.click()

time.sleep(5)

button_no = driver.find_element_by_id("idSIButton9")
button_no.click()

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе

time.sleep(10)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
