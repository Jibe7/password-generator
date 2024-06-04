""" Tests for the GUI password generator application.

Current limitation : it won't pass all the tests systematically (especially when the password size is not too big) as currently the code for the app does not guaranty that a set of character is chosen even when selected. EG : the user check all the checkbox, but it does not guarantee that there will be any digits in the password; imagine if the random function choose only lower cases letter despite it being able to pull digits... Future fix to do but not necessary either, the app works well enough for my use. Improvement would be to be able to choose from each of the category of characters how much we want in our password.

"""


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest
from password_generator import passGen
import string



def includesCharacterFrom(password, alphabet):
    for chr in password:
        if chr in alphabet:
            return True
    return False

def notIncludesCharacterFrom(password, alphabet):
    for chr in password:
        if chr in alphabet:
            return False
    return True

def countCharacterFrom(password, alphabet):
    cnt = 0
    for chr in password:
        if chr in alphabet:
            cnt += 1
    return cnt


PassWordGenerator = passGen.PasswordGenerator()

@pytest.mark.default_config 
@pytest.mark.characters_customization # relates to the choice of checkboxes for character customization
def test_default_config(default_size = 15, default_characters = string.ascii_lowercase):
    """ Tests that by default, the password generated are 15 characters long and only contains lowercase characters.
    
    """


    PassWordGenerator.basicPassGen()
    new_pass = PassWordGenerator.password 
    assert countCharacterFrom(new_pass, default_characters) == default_size

@pytest.mark.no_checkbox_checked
@pytest.mark.characters_customization
def test_no_alphabet(default_answer =  "Please choose at least one type of characters for the password."):
    """ Tests that when all checkbox are unselected the user receives a given message to select at least one.
    
    """
    PassWordGenerator.lowerCasesCheckBox.checkBox.deselect()
    PassWordGenerator.upperCasesCheckBox.checkBox.deselect()
    PassWordGenerator.digitsCheckBox.checkBox.deselect()
    PassWordGenerator.punctuationCheckBox.checkBox.deselect()

    PassWordGenerator.basicPassGen()
    new_pass = PassWordGenerator.password 

    assert new_pass == default_answer

@pytest.mark.characters_customization
def test_digits(pass_size = 15):
    PassWordGenerator.lowerCasesCheckBox.checkBox.deselect()
    PassWordGenerator.upperCasesCheckBox.checkBox.deselect()
    PassWordGenerator.punctuationCheckBox.checkBox.deselect()
    PassWordGenerator.digitsCheckBox.checkBox.select()

    PassWordGenerator.basicPassGen(pass_size)
    new_pass = PassWordGenerator.password 

    assert len(new_pass) == pass_size

    assert countCharacterFrom(new_pass, string.digits) == pass_size

@pytest.mark.characters_customization
def test_lower_digits(pass_size = 30):
    PassWordGenerator.lowerCasesCheckBox.checkBox.select()
    PassWordGenerator.upperCasesCheckBox.checkBox.deselect()
    PassWordGenerator.digitsCheckBox.checkBox.select()
    PassWordGenerator.punctuationCheckBox.checkBox.deselect()

    PassWordGenerator.basicPassGen(pass_size)
    new_pass = PassWordGenerator.password 

    assert len(new_pass) == pass_size

    assert includesCharacterFrom(new_pass, string.ascii_lowercase)
    assert includesCharacterFrom(new_pass, string.digits)
    assert notIncludesCharacterFrom(new_pass, string.ascii_uppercase)
    assert notIncludesCharacterFrom(new_pass, string.punctuation)

@pytest.mark.characters_customization
def test_lower_upper_digits(pass_size = 30):
    PassWordGenerator.lowerCasesCheckBox.checkBox.select()
    PassWordGenerator.upperCasesCheckBox.checkBox.select()
    PassWordGenerator.digitsCheckBox.checkBox.select()
    PassWordGenerator.punctuationCheckBox.checkBox.deselect()

    PassWordGenerator.basicPassGen(pass_size)
    new_pass = PassWordGenerator.password 

    assert len(new_pass) == pass_size

    assert includesCharacterFrom(new_pass, string.ascii_lowercase)
    assert includesCharacterFrom(new_pass, string.digits)
    assert includesCharacterFrom(new_pass, string.ascii_uppercase)
    assert notIncludesCharacterFrom(new_pass, string.punctuation)

@pytest.mark.characters_customization
def test_lower_upper_digits_punctuation(pass_size = 45):
    PassWordGenerator.lowerCasesCheckBox.checkBox.select()
    PassWordGenerator.upperCasesCheckBox.checkBox.select()
    PassWordGenerator.digitsCheckBox.checkBox.select()
    PassWordGenerator.punctuationCheckBox.checkBox.select()

    PassWordGenerator.basicPassGen(pass_size)
    new_pass = PassWordGenerator.password 

    assert len(new_pass) == pass_size

    assert includesCharacterFrom(new_pass, string.ascii_lowercase)
    assert includesCharacterFrom(new_pass, string.digits)
    assert includesCharacterFrom(new_pass, string.ascii_uppercase)
    assert includesCharacterFrom(new_pass, string.punctuation)

@pytest.mark.skip(reason="Not implemented. Currently if the user input is a negative number, it will be converted to positive. It should return a message asking him to enter a positive number.")
@pytest.mark.wrong_input
def test_negative_input(negative_size = - 15, negative_msg = "You should enter a positive integer."):
    PassWordGenerator.lowerCasesCheckBox.checkBox.select()
    PassWordGenerator.upperCasesCheckBox.checkBox.deselect()
    PassWordGenerator.digitsCheckBox.checkBox.deselect()
    PassWordGenerator.punctuationCheckBox.checkBox.deselect()

    PassWordGenerator.basicPassGen(negative_size)
    new_pass = PassWordGenerator.password 

    assert new_pass == negative_msg

@pytest.mark.skip(reason="Not implemented. Currently, if the user input is a text it will have the default behavior with a size of 15 and only lowercase characters. It should return a message asking him to enter a number.")
@pytest.mark.wrong_input
def test_string_input(string_size = "Lorem ipsum", string_error_msg = "You should enter a number and not a string."):
    PassWordGenerator.lowerCasesCheckBox.checkBox.select()
    PassWordGenerator.upperCasesCheckBox.checkBox.deselect()
    PassWordGenerator.digitsCheckBox.checkBox.deselect()
    PassWordGenerator.punctuationCheckBox.checkBox.deselect()

    PassWordGenerator.basicPassGen(string_size)
    new_pass = PassWordGenerator.password 

    assert new_pass == string_error_msg

@pytest.mark.xfail # when we expect a test to fail
@pytest.mark.wrong_input
def test_zero_input(zero_size = 0, string_error_msg = "You should enter a positive number that is not zero."):
    if not any([PassWordGenerator.lowerCasesCheckBox.checkBox.get(), PassWordGenerator.upperCasesCheckBox.checkBox.get(),
    PassWordGenerator.digitsCheckBox.checkBox.get(),
    PassWordGenerator.punctuationCheckBox.checkBox.get()]):
        PassWordGenerator.lowerCasesCheckBox.checkBox.select()

    PassWordGenerator.basicPassGen(zero_size)
    new_pass = PassWordGenerator.password 

    assert new_pass == string_error_msg

