from django.test import TestCase

# Create your tests here.

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#class LoginTestCase(TestCase):
 #   def setUp(self):
  #      self.driver = webdriver.Chrome()
   #     self.driver.implicitly_wait(10)

    #def tearDown(self):
     #   self.driver.quit()

    #def test_login(self):
     #   self.driver.get('http://127.0.0.1:8000/login.html')

      #  username_input = self.driver.find_element(By.NAME, 'username')
       # password_input = self.driver.find_element(By.NAME, 'password')

     #   # Use XPath to locate the login button
      #  login_button_xpath = '//button[@type="submit"]'
        
       # # Wait for the button to be visible
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_button_xpath)))
        
        ## Find the login button using XPath
        #login_button = self.driver.find_element(By.XPATH, login_button_xpath)

        #username_input.send_keys('abhi')
        #password_input.send_keys('abhi')
        #login_button.click()

        ## Wait for the page to load after login (replace this with appropriate page load condition)
        #WebDriverWait(self.driver, 10).until(EC.url_to_be('http://127.0.0.1:8000/admindashboard.html'))

        ## Perform assertions to verify successful login
        # #expected_content = 'Text or Element on Successful Login Page'
        # #assert expected_content in self.driver.page_source, f"Expected content '{expected_content}' not found after login"

#from django.test import TestCase
from django.forms import ValidationError
from .forms import LeaveApplicationForm
from datetime import datetime, timedelta

class LeaveApplicationFormTest(TestCase):
    def test_valid_leave_application_form(self):
        # Test the form with valid data
        form_data = {
            'start_date': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'),
            'end_date': (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d'),
            'reason': 'Vacation',
        }
        form = LeaveApplicationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_leave_application_form(self):
        # Test the form with invalid data (end_date before start_date)
        form_data = {
            'start_date': (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d'),
            'end_date': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'),
            'reason': 'Vacation',
        }
        form = LeaveApplicationForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Check if the error is present in __all__ instead of a specific field
        self.assertIn('__all__', form.errors)
        self.assertEqual(form.errors['__all__'], ['End date must be equal to or after the start date.'])

    def test_date_range_constraints(self):
        # Test that the date range constraints are applied
        form = LeaveApplicationForm()
        start_date_widget = form.fields['start_date'].widget
        end_date_widget = form.fields['end_date'].widget

        # Check if 'min' and 'max' attributes are set correctly
        self.assertIn('min', start_date_widget.attrs)
        self.assertIn('max', start_date_widget.attrs)
        self.assertIn('min', end_date_widget.attrs)
        self.assertIn('max', end_date_widget.attrs)

        # You can add more specific checks based on your date range constraints

    # Add more test cases as needed based on your form's behavior

from django.test import TestCase
from django.urls import reverse
from .models import Orders, WorkerProfile, OrderWorkerAssignment, District
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class ProcessAssignmentTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

        # Create a district
        self.district = District.objects.create(district_id=2, district_name='Thiruvananthapuram')  # Updated field name

        # Create an order
        self.order = Orders.objects.create(
            user=self.user,
            district=self.district,
            # Add other required fields
        )

        # Create a worker
        self.worker = WorkerProfile.objects.create(
            user=self.user,
            district=self.district,
            # Add other required fields
        )

    def test_process_assignment_view(self):
        url = reverse('process_assignment', args=[self.order.id])
        data = {'selected_workers': [self.worker.worker_id]}  # Use the correct field name for the worker's primary key
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Add more assertions as needed

    # Add more test cases as needed


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from watersystemapp.models import Payment, OrderWorkerAssignment

class PaymentHistoryTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create an OrderWorkerAssignment for testing
        self.order_assignment = OrderWorkerAssignment.objects.create(
            order=order_id,  # Replace with an actual Order instance
            worker=worker_id  # Replace with an actual Worker instance
        )

        # Create a payment for the user
        self.payment = Payment.objects.create(
            order_assignment=self.order_assignment,
            user=self.user,
            price=50.00,
            payment_status='Completed'
        )

    def test_payment_history_view(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        # Access the payment history view
        url = reverse('payment_history')  # Replace with your actual URL name for payment_history
        response = self.client.get(url)

        # Check if the view returns a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check if the payment details are present in the context
        self.assertIn('payment_details', response.context)
        
        # Check if the payment for the user is in the payment details
        self.assertIn(self.payment, response.context['payment_details'])

    