from pathlib import Path

def upload(username, current_url, mp4_path, txt_path, driver, wait, EC, By, generate_ai_content, time):
    try:
        time.sleep(10)
        driver.get(current_url)
        file_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file'][name='Filedata']"))
            )

        # Set the file path to the input element
        base_dir = Path(__file__).resolve().parent
        hiii_folder = base_dir / 'hiii' / f"{username}"
        file_path = hiii_folder / mp4_path  # Replace with your file path
        print(file_path)
        
        file_input.send_keys(str(file_path))
        print("File uploaded successfully")
        time.sleep(2)
        text_path = hiii_folder /  txt_path
        with open(text_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
        title = generate_ai_content(text_content + "       :make the above under 100 characters and return only the answer so that i can directly copy paste to be written")
        print("title generated ")
        textbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Add a title that describes your video (type @ to mention a channel)']")))
        textbox.clear()  # This may not work as expected for content-editable elements
        # Send text to the content-editable div
        textbox.send_keys(title)
        time.sleep(3)
        print("title sent")
        next_button = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button.ytcp-button-shape-impl[aria-label='Next']"
        )))
        print("next clicked")

        # Click the button
        next_button.click()
        time.sleep(2)
        next_button2 = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button.ytcp-button-shape-impl[aria-label='Next']"
        )))

        # Click the button
        next_button2.click()
        time.sleep(2)
        next_button3 = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button.ytcp-button-shape-impl[aria-label='Next']"
        )))

        # Click the button
        next_button3.click()
        time.sleep(2)

        private_radio_button = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "tp-yt-paper-radio-button#private-radio-button"
        )))

        # Click the radio button
        private_radio_button.click()
        time.sleep(1)
        save_button = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button.ytcp-button-shape-impl[aria-label='Save']"
        )))

        # Click the button
        save_button.click()
        time.sleep(2)
    except Exception as e:
        print(f"error occured while uploading {e}")

