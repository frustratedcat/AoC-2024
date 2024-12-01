from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.profile = FirefoxProfile('/home/jared/.mozilla/firefox/oh2nm0of.default-release')

driver = webdriver.Firefox(options=options)
driver.get('https://adventofcode.com/2024/day/1/input')

list_of_nums = str(driver.find_element(By.XPATH, '//pre').text)

split_list = list_of_nums.split()

list_1 = []
list_2 = []
list_3 = []
final_result = 0

for i in range(0, len(split_list)):
    if i == 0 or i % 2 == 0:
        list_1.append(int(split_list[i]))
    else:
        list_2.append(int(split_list[i]))

sorted_list_1 = sorted(list_1)
sorted_list_2 = sorted(list_2)

for j in range(0, len(list_1)):
    list_3.append(abs(sorted_list_1[j] - sorted_list_2[j]))

for k in range(0, len(list_3)):
    final_result += list_3[k]

print(final_result)

