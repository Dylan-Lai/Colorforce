from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize  Chrome driver
driver = webdriver.Chrome()
driver.get("https://ssb.cc.binghamton.edu:8484/StudentRegistrationSsb/ssb/term/termSelection?mode=search")

# term dropdown click
term_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "s2id_txt_term"))  # Clickable term dropdown
)
term_dropdown.click()

# dropdown options load
term_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "select2-results"))
)


time.sleep(2)

# click desired term 
try:
    term_option_elements = term_options.find_elements(By.TAG_NAME, "li")

    for option in term_option_elements:
        if option.text == 'Fall 2024':
            option.click()
            break
    else:
        print("Desired term option not found.")

    # click continue to submit option
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']"))
    )
    continue_button.click()

    # attribute dropdown 
    attribute_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "s2id_txt_attribute"))  
    )
    attribute_dropdown.click()

  
    attribute_options = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "select2-results"))
    )


    time.sleep(2)

    
    attribute_option_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "li"))
    )

    # debugging - print all available options 
    print("Available attribute options:")
    for option in attribute_option_elements:
        print(option.text)  # print option

    # click desired course attribute 
    for option in attribute_option_elements:
        if option.text == 'A - Aesthetic Perspective':
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(option))  
            driver.execute_script("arguments[0].click();", option) 
            break
    else:
        print("Desired attribute option not found.")

except Exception as e:
    print("Error:", e)


time.sleep(10)  

# close browser 
driver.quit()
