from selenium.webdriver.common.action_chains import ActionChains

import warnings
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from genai_module import generate_ai_content 
from upload_file import upload
from file_array import make_map
# from genai_module import generate_ai_content 
# from upload_file import upload
# from file_array import make_map



# Setup WebDriver with options
def Y_uploader_run(username):
    
    options = uc.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    options.headless = True  # Run in headless mode for Docker
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Specify the path to the Chrome binary
    options.binary_location = "/usr/bin/google-chrome"

    # Start the WebDriver
    driver = uc.Chrome(options=options)

    try:
        # Navigate to the target page
        

        driver.get("https://www.youtube.com")

        # # Wait for the "Sign in" button to be clickable
        wait = WebDriverWait(driver, 20)
        sign_in_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[aria-label='Sign in'][href*='ServiceLogin']")
        ))
        sign_in_button.click()
        print("sign in clicked")
                next_button_ini = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button'))
        )

        # Scroll to the element
        driver.execute_script("arguments[0].scrollIntoView();", next_button_ini)
        # Optional: Print computed style for debugging

        # Wait briefly before attempting to click
        time.sleep(1)

        # Check visibility and click
        if next_button_ini.is_displayed():
            next_button_ini.click()
        else:
            print("Element is not visible, attempting to click with ActionChains.")
            actions = ActionChains(driver)
            actions.move_to_element(next_button_ini).click().perform()

        time.sleep(5)  # Wait to observe the result



        pass_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        # Type the email address
        time.sleep(2)
        pass_input.send_keys("important4u")  # Replace with your email
        time.sleep(5)
        # Locate and click the "Next" button
        next_button_ini2 = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button'))
        )

        # Scroll to the element
        driver.execute_script("arguments[0].scrollIntoView();", next_button_ini2)
        # Optional: Print computed style for debugging

        # Wait briefly before attempting to click
        time.sleep(1)

        # Check visibility and click
        if next_button_ini2.is_displayed():
            next_button_ini2.click()
        else:
            print("Element is not visible, attempting to click with ActionChains.")
            actions = ActionChains(driver)
            actions.move_to_element(next_button_ini2).click().perform()

        time.sleep(5)  # Wait to observe the result


        
        create_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Create']"))
        )
        create_button.click()
        print("craete clicked")

        upload_video_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/upload']"))
        )
        upload_video_link.click()
        print("upload button clicked")

        current_url = driver.current_url
        time.sleep(10)
        folder_map=make_map(username)
        print(folder_map)
        for mp4_file, txt_file in folder_map.items():
            print("upload called")
            upload(username, current_url, mp4_file, txt_file, driver, wait, EC, By, generate_ai_content, time)
            time.sleep(5)
        #     # print(mp4_file)
        # print(folder_map)
        
        time.sleep(5)

    except Exception as e:
        print(f"Error ooccered {e}")

    # try:
    #     driver.quit()
    # except Exception as e:
    #     warnings.warn(f"Warning during driver quit: {e}")

