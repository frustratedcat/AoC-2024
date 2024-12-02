from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.profile = FirefoxProfile('/home/jared/.mozilla/firefox/oh2nm0of.default-release')

driver = webdriver.Firefox(options=options)
driver.get('https://adventofcode.com/2024/day/2/input')

list_of_nums = str(driver.find_element(By.XPATH, '//pre').text)

split_list = list_of_nums.split('\n')
list_of_lists = []

for i in range(0, len(split_list)):
    list_of_lists.append(list(split_list[i]))

split_join = []

for i in range(0, len(list_of_lists)):
    res = ''.join(list_of_lists[i])
    split_join.append(res.split())


for i in range(len(split_join)):
    for j in range(len(split_join[i])):
        split_join[i][j] = int(split_join[i][j])

evaluate = 0

for i in range(len(split_join)):
    ascending = all(j < k for j, k in zip(split_join[i], split_join[i][1:]))
    diff_ascending = all((k - j) < 4 for j, k in zip(split_join[i], split_join[i][1:]))
    descending = all(j > k for j, k in zip(split_join[i], split_join[i][1:]))
    diff_descending = all((j - k) < 4 for j, k in zip(split_join[i], split_join[i][1:]))
    if ascending == True and diff_ascending == True:
        evaluate += 1
    elif descending == True and diff_descending == True:
        evaluate += 1

print(evaluate)

driver.quit()
