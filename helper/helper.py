import json
import bs4
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def extract_user_profile_data_from_soup(soup):
    try:
        result_list = []
        li_elements = soup.select('._acay li')
        for child in li_elements:
            result_dict = {}
            img = child.find(class_="xnz67gz")
            element = child.find(class_="x9f619 x1lliihq x6ikm8r x10wlt62 x1n2onr6 x2b8uid xlyipyv xuxw1ft x1yf5rgg xhikscq xg83lxy x1h0ha7o")

            if isinstance(img, bs4.element.Tag):
                img_src = img.find('img')['src']
                result_dict['img_src'] = img_src

            if isinstance(element, bs4.element.Tag):
                result_dict['name'] = element.text.strip()
                result_dict['insta_url'] = f"https://www.instagram.com/{element.text.strip()}"

            result_list.append(result_dict)

        json_result = json.dumps(result_list, indent=4, default=str)
        return json_result
    except Exception as e:
        return "Something Went Wrong"
        



def all_user_profile_images(users_story_data,driver):
    try: 
        
        parsed_data = json.loads(users_story_data)
        all_user_profile_story_data = []
        for user in parsed_data:
            if "insta_url" in user:
                result_list = []
                driver = driver.get(user['insta_url'])
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                li_elements = soup.find_all(class_="xnz67gz x14yjl9h xudhj91 x18nykt9 xww2gxu x1lliihq x6ikm8r x10wlt62 x1n2onr6")
                for child in li_elements:
                        if isinstance(child, bs4.element.Tag):
                            img_src = child.find('img')['src']
                            result_dict['img_src'] = img_src.replace('amp;','')
                            result_list.append(result_dict)
            all_user_profile_story_data.append(result_list)
            time.sleep(5)
        return all_user_profile_story_data
    except Exception as e: 
        return "Something went wrong"



def take_screenshot(driver):
    li_elements = driver.find_elements(By.CSS_SELECTOR,'._acay li')
    print(len(li_elements))
    for child in li_elements:
        print(child.text)
        try:
            element = child.find(class_="x9f619 x1lliihq x6ikm8r x10wlt62 x1n2onr6 x2b8uid xlyipyv xuxw1ft x1yf5rgg xhikscq xg83lxy x1h0ha7o").click()
            if isinstance(element, bs4.element.Tag):
                element.screenshot('1.png')
        except Exception as e: 
            print('e',e)
    return "All profile screenshot taken"


