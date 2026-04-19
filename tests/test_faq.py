import allure
import pytest
from pages.home_page import HomePage
from data import FAQ_DATA


@allure.feature("FAQ")
class TestFAQ:
    
    @allure.title("Проверка ответов на вопросы в разделе 'Вопросы о важном'")
    @pytest.mark.parametrize("question_index, expected_answer", FAQ_DATA)
    def test_faq_answer(self, driver, question_index, expected_answer):
        home_page = HomePage(driver)
        home_page.click_question(question_index)
        
        actual_answer = home_page.get_answer_text(question_index)
        
        with allure.step("Проверить, что текст ответа соответствует ожидаемому"):
            assert expected_answer in actual_answer, \
                f"Ожидалось: {expected_answer}\nПолучено: {actual_answer}"