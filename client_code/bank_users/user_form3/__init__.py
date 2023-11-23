from ._anvil_designer import user_form3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from . import user_module
from ..main_form import main_form_module

class user_form3(user_form3Template):
  def __init__(self,**properties):
    self.init_components(**properties)
    self.email = main_form_module.email
    email=self.email
    self.name = user_module.get_name(email)
    self.user_id =  user_module.find_user_id(email)
    
    self.email = email
    self.user_name_lable.text = self.name
    if main_form_module.alert_mes(main_form_module.flag):
      print("user login")
    else:
      print("user login")

  
  def logout_user_form_link_click(self, **event_args):
     alert("logout sucessfully")
     anvil.users.logout()
     open_form('bank_users.main_form')
    

  
  # this function is use for new borrower signup and check the user already  signup or not
  def borrower_user_form_link_click(self, **event_args):
    userid = self.user_id
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin',user_id=userid)
   


  #--this metod is for lendor--#

  def lendor_user_form_link_click(self, **event_args):
    userid = self.user_id
    open_form('lendor_registration_form.Lender_reg_form_1',user_id=userid)

  #--------------------------------------------------------------------#
  
  def view_profile_user_home_click(self, **event_args):
    name = self.name
    email = self.email
    user_id = self.user_id
    alert(f"View profile:\nName = {name}\nEmail = {email}\nUser Id = {user_id}")