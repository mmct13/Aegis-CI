import pytest
from scripts.dlp_check import luhn_check

class TestDLP:
    def test_luhn_check_valid(self):
        # Valid test cases (Test numbers from online generators)
        assert luhn_check("453201511283036") == True
        assert luhn_check("49927398716") == True
    
    def test_luhn_check_invalid(self):
        # Invalid test cases
        assert luhn_check("453201511283037") == False
        assert luhn_check("1234") == False

    def test_luhn_check_with_strings(self):
        # Should handle strings, though the function expects cleaned input in usage
        # The function internal logic converts to int immediately
        assert luhn_check("49927398716") == True
