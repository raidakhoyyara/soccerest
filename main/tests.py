from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from main.models import Product

class SoccerestFunctionalTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.quit()

    def setUp(self):
        # Buat user untuk testing
        self.test_user = User.objects.create_user(
            username="testadmin",
            password="testpassword"
        )

    def tearDown(self):
        # Reset state browser
        self.browser.delete_all_cookies()
        self.browser.execute_script("window.localStorage.clear();")
        self.browser.execute_script("window.sessionStorage.clear();")
        self.browser.get("about:blank")

    def login_user(self):
        """Helper login"""
        self.browser.get(f"{self.live_server_url}/login/")
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("testadmin")
        password_input.send_keys("testpassword")
        password_input.submit()

    def test_login_page(self):
        self.login_user()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Soccerest")
        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(),'Logout')]")
        self.assertTrue(logout_button.is_displayed())

    def test_register_page(self):
        self.browser.get(f"{self.live_server_url}/register/")
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Register")

        # isi form register
        username_input = self.browser.find_element(By.NAME, "username")
        password1_input = self.browser.find_element(By.NAME, "password1")
        password2_input = self.browser.find_element(By.NAME, "password2")

        username_input.send_keys("newuser")
        password1_input.send_keys("complexpass123")
        password2_input.send_keys("complexpass123")
        password2_input.submit()

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))

    def test_create_product(self):
        self.login_user()
        add_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Add Product')]")
        add_button.click()

        # isi form produk
        name_input = self.browser.find_element(By.NAME, "name")
        description_input = self.browser.find_element(By.NAME, "description")
        price_input = self.browser.find_element(By.NAME, "price")
        category_select = self.browser.find_element(By.NAME, "category")
        thumbnail_input = self.browser.find_element(By.NAME, "thumbnail")

        name_input.send_keys("Test Product")
        description_input.send_keys("Deskripsi produk testing selenium")
        price_input.send_keys("150000")
        thumbnail_input.send_keys("https://example.com/image.jpg")

        select = Select(category_select)
        select.select_by_value("jersey")  # contoh kategori

        name_input.submit()

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Soccerest"))
        self.assertIn("Test Product", self.browser.page_source)

    def test_product_detail(self):
        self.login_user()
        # bikin produk langsung lewat model
        product = Product.objects.create(
            name="Detail Test Product",
            description="Deskripsi detail produk",
            price=200000,
            category="shoes",
            user=self.test_user
        )
        self.browser.get(f"{self.live_server_url}/product/{product.id}/")
        self.assertIn("Detail Test Product", self.browser.page_source)
        self.assertIn("Deskripsi detail produk", self.browser.page_source)

    def test_logout(self):
        self.login_user()
        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(),'Logout')]")
        logout_button.click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Login")

    def test_filter_main_page(self):
        # bikin produk test
        Product.objects.create(
            name="My Test Product",
            description="Produk saya",
            price=100000,
            category="jersey",
            user=self.test_user
        )
        Product.objects.create(
            name="Other User Product",
            description="Produk lain",
            price=120000,
            category="shoes",
            user=self.test_user
        )
        self.login_user()

        # cek filter All
        all_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'All Product')]")
        all_button.click()
        self.assertIn("My Test Product", self.browser.page_source)
        self.assertIn("Other User Product", self.browser.page_source)

        # cek filter My
        my_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'My Product')]")
        my_button.click()
        self.assertIn("My Test Product", self.browser.page_source)

