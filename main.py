import data
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time





# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.CSS_SELECTOR, ".button.round")
    option_comfort_rate = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_number_button = (By.CSS_SELECTOR, ".np-button")
    phone_number_field = (By.ID, "phone")
    next_button = (By.CSS_SELECTOR, ".button.full")
    sms_code_field = (By.ID, "code")
    sms_confirmation_button = (By.XPATH, "//div[@class='buttons']/button[text()='Confirmar']")
    pay_method_button = (By.CSS_SELECTOR, ".pp-button")
    add_card_button = (By.CSS_SELECTOR, ".pp-plus-container")
    card_number_field= (By.ID, "number")
    code_number_field = (By.NAME, "code")
    add_button = (By.XPATH, "//button[@class='button full' and text()='Agregar']")
    added_card_field = (By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']" )
    pay_method_close_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    message_to_driver_field = (By.ID, "comment")
    blanket_and_handkerchief_switch = (By.CLASS_NAME, 'switch')
    blanket_and_handkerchief_input = (By.CLASS_NAME, 'switch-input')
    ice_cream_counter_plus = (By.CLASS_NAME, 'counter-plus')
    request_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
    countdown_modal = (By.XPATH, "//div[contains(@class, 'order-header-time')]")
    trip_details_modal = (By.CLASS_NAME, "order-details")
    driver_name = (By.XPATH, '//div[@class="order-btn-group"][1]/div[2]')



    def __init__(self, driver):
        self.driver = driver


    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def set_from(self, from_address):
        WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)


    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_request_taxi(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.order_taxi_button)
        )

    def click_on_order_taxi_button(self):
        self.get_request_taxi().click()

    def get_option_comfort_rate(self):
        return self.driver.find_element(*self.option_comfort_rate)

    def click_on_comfort_rate(self):
        self.get_option_comfort_rate().click()

    def get_phone_number_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.phone_number_button)
        )

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.visibility_of_element_located(self.phone_number_field)
        )

    def set_phone_number(self):
        self.get_phone_number_field().send_keys(data.phone_number)

    def get_next_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.next_button)
        )

    def click_on_next_button(self):
        self.get_next_button().click()

    def get_sms_code_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.sms_code_field)
        )

    def set_sms_code(self):
        code = retrieve_phone_code(self.driver)
        self.get_sms_code_field().send_keys(code)

    def get_confirmation_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.sms_confirmation_button)
        )

    def click_on_sms_confirmation_button(self):
        self.get_confirmation_button().click()

    def get_pay_method_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.pay_method_button)
        )

    def click_on_payment_method_button(self):
        self.get_pay_method_button().click()

    def get_add_card_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.add_card_button)
        )

    def click_on_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.card_number_field)
        )

    def set_card_number(self):
        self.get_card_number_field().send_keys(data.card_number)

    def get_code_number_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.code_number_field)
        )

    def set_code_field(self):
        self.get_code_number_field().send_keys(data.card_code)

    def get_add_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.add_button)
        )

    def click_on_add_button(self):
        self.get_add_button().click()

    def get_added_card_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.added_card_field)
        )

    def get_pay_method_close_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.pay_method_close_button)
        )

    def click_on_close_button(self):
        self.get_pay_method_close_button().click()

    def get_message_to_driver_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.message_to_driver_field)
        )

    def set_message_to_driver(self):
        self.get_message_to_driver_field().send_keys(data.message_for_driver)


    def get_blanket_and_handkerchief(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.blanket_and_handkerchief_switch)
        )

    def set_blanket_and_handkerchief_switch(self):
        self.get_blanket_and_handkerchief().click()


    def get_blanket_and_handkerchief_input(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.blanket_and_handkerchief_input)
        )

    def click_on_blanket_and_handkerchief_input(self):
        self.get_blanket_and_handkerchief_input().click()

    def get_ice_cream_counter_plus(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.ice_cream_counter_plus)
        )

    def click_ice_cream_counter_plus(self):
        self.get_ice_cream_counter_plus().click()

    def get_counter_value(self):                                                                 #Obtenemos el valor inicial del contador
        counter_element = self.driver.find_element(By.CLASS_NAME, "counter-value")
        return int(counter_element.text)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def wait_countdown_modal_close(self):
        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located(UrbanRoutesPage.countdown_modal)
        )

    def get_driver_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.driver_name)
        )



class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_order_taxi_button()
        routes_page.click_on_comfort_rate()

        comfort_rate = routes_page.get_option_comfort_rate().text
        comfort_text = "Comfort"
        assert comfort_text in comfort_rate

    def test_enter_phone_number(self):
        self.test_select_comfort_rate()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_phone_number_button()
        routes_page.set_phone_number()

        assert data.phone_number == routes_page.get_phone_number_field().get_property("value")

        routes_page.click_on_next_button()
        routes_page.set_sms_code()
        routes_page.click_on_sms_confirmation_button()

        assert routes_page.get_phone_number_button().text == data.phone_number

    def test_enter_payment_method(self):
        self.test_enter_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_payment_method_button()
        routes_page.click_on_add_card_button()
        routes_page.set_card_number()
        routes_page.get_card_number_field().send_keys(Keys.TAB)
        routes_page.set_code_field()
        routes_page.get_code_number_field().send_keys(Keys.TAB)
        routes_page.click_on_add_button()
        assert routes_page.get_added_card_field().text == 'Tarjeta'
        routes_page.click_on_close_button()

    def test_enter_message_to_driver(self):
        self.test_enter_payment_method()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_message_to_driver_field().send_keys(Keys.TAB)
        routes_page.set_message_to_driver()
        assert data.message_for_driver == routes_page.get_message_to_driver_field().get_attribute("value")

    def test_select_blanket_and_handkerchief(self):
        self.test_enter_message_to_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_blanket_and_handkerchief_switch()
        assert routes_page.get_blanket_and_handkerchief_input().get_property('checked')                #Confirma que el switch esta activado

    def test_add_ice_cream(self):
        self.test_select_blanket_and_handkerchief()
        routes_page = UrbanRoutesPage(self.driver)
        initial_value = routes_page.get_counter_value()
        routes_page.click_ice_cream_counter_plus()
        new_value = routes_page.get_counter_value()
        assert new_value == initial_value + 1, f"Error: Se esperaba {initial_value + 1}, resultado {new_value}"      #Se confirma que el contador aumento en 1

    def test_request_taxi_button(self):
        self.test_add_ice_cream()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_request_taxi_button()

    def test_trip_details_modal_after_countdown(self):
        self.test_request_taxi_button()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_countdown_modal_close()
        driver_name = routes_page.get_driver_name().text
        assert driver_name != "", f"El nombre del conductor no debería estar vacío, resutado: '{driver_name}'"



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
























