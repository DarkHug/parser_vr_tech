import logging
import re
import os

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)

load_dotenv()


def parse(url: str) -> dict:
    chrome_options = Options()
    service = Service(os.getenv("CHROMEDRIVER_PATH"))
    chrome_options.binary_location = os.getenv("CHROME_PATH")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    product_data = {}

    try:
        card_name = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1.item__heading"))
        )
        product_data["name"] = card_name.text
        logger.info("Название: %s", card_name.text)

        price = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.item__price-once"))
        )
        product_data["price"] = price.text
        logger.info("Цена: %s", price.text)

        rating_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.item__rating span"))
        )
        rating_class = rating_element.get_attribute("class")  # например "rating _49"
        match = re.search(r'_(\d+)', rating_class)
        if match:
            rating = float(match.group(1)) / 10
            product_data["rating"] = rating
            logger.info("Рейтинг: %s", rating)
        else:
            product_data["rating"] = None
            logger.info("Рейтинг не найден")

        reviews_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.item__rating-link span"))
        )
        reviews_text = reviews_element.text
        reviews_number = re.search(r'(\d+)', reviews_text)
        if reviews_number:
            product_data["reviews"] = int(reviews_number.group(1))
            logger.info("Количество отзывов: %s", reviews_number.group(1))
        else:
            product_data["reviews"] = 0
            logger.info("Отзывы не найдены")

        category_elements = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.breadcrumbs__item"))
        )

        if len(category_elements) >= 3:
            category_text = category_elements[2].text.strip()
            product_data["category"] = category_text
            logger.info("Категория: %s", category_text)
        else:
            product_data["category"] = None
            logger.info("Категория не найдена")

    except Exception as e:
        logger.exception("Ошибка при парсинге: %s", e)

    finally:
        driver.quit()

    return product_data
