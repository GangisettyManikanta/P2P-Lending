from ._anvil_designer import application_trackerTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class application_tracker(application_trackerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    current_user=get_current_user_id()
    # Any code you write here will run before the form opens.
    self.repeating_panel_1=tables.app_tables.loan_details.search()
    loan_exists = anvil.server.call('check_loan_existence', user_id)
    if loan_exists:
      print("Loan already exists for this user.")
    else:
      print("No existing loan for this user.")
  def home_borrower_registration_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form')
