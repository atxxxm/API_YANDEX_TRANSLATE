from playwright.sync_api import sync_playwright
from time import sleep

def API_YANDEX_TRANSLATE(text, from_la, to_la):
    
    url = f"https://translate.yandex.ru/?source_lang={from_la}&target_lang={to_la}&text="
    translate = "#fakeArea"
    swap = "#langsPanel > div.wnJW7LPN_ZsOMBoXFamJ.J1LTehOMOcJzZSeWwLEY > div > div > button.gTx50DUfJa1q57Z9sbM6.t3nFXmxYr19rwmJaBoHg.yZ0odbAnIl__RMrmbWuA.SNvWOiTv0bJTav0uo4Y6.nit1qvNY5o0LAHqo2TZ2.hf9lG6bClwoi5q7Cs1uQ"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url + text)
        swap_btn = page.locator(swap)
        sleep(0.2)
        swap_btn.click()
        translate_text = page.locator(translate).inner_text()
        browser.close()
        return translate_text
        
        
    
 
