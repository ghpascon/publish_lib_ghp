"""Tests for the greeting module."""

import pytest
from src.publish_lib_ghp import Greeting


class TestGreeting:
    """Test class for Greeting functionality."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.greeting = Greeting()
    
    def test_say_hello_basic(self):
        """Test basic hello functionality."""
        result = self.greeting.say_hello("World")
        assert result == "Hello, World!"
    
    def test_say_hello_with_different_names(self):
        """Test hello with different names."""
        test_cases = [
            ("Alice", "Hello, Alice!"),
            ("Bob", "Hello, Bob!"),
            ("Gabriel", "Hello, Gabriel!"),
            ("Maria José", "Hello, Maria José!"),
        ]
        
        for name, expected in test_cases:
            result = self.greeting.say_hello(name)
            assert result == expected
    
    def test_say_hello_empty_name(self):
        """Test hello with empty name raises ValueError."""
        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            self.greeting.say_hello("")
    
    def test_say_hello_none_name(self):
        """Test hello with None name raises ValueError."""
        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            self.greeting.say_hello(None)
    
    def test_say_hello_non_string_name(self):
        """Test hello with non-string name raises ValueError."""
        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            self.greeting.say_hello(123)
    
    def test_say_goodbye_basic(self):
        """Test basic goodbye functionality."""
        result = self.greeting.say_goodbye("World")
        assert result == "Goodbye, World!"
    
    def test_say_goodbye_with_different_names(self):
        """Test goodbye with different names."""
        test_cases = [
            ("Alice", "Goodbye, Alice!"),
            ("Bob", "Goodbye, Bob!"),
            ("Gabriel", "Goodbye, Gabriel!"),
        ]
        
        for name, expected in test_cases:
            result = self.greeting.say_goodbye(name)
            assert result == expected
    
    def test_say_goodbye_validation(self):
        """Test goodbye input validation."""
        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            self.greeting.say_goodbye("")
            
        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            self.greeting.say_goodbye(None)
    
    def test_get_greeting_with_time_morning(self):
        """Test morning greeting."""
        result = self.greeting.get_greeting_with_time("Alice", "morning")
        assert result == "Good morning, Alice!"
    
    def test_get_greeting_with_time_afternoon(self):
        """Test afternoon greeting."""
        result = self.greeting.get_greeting_with_time("Bob", "afternoon")
        assert result == "Good afternoon, Bob!"
    
    def test_get_greeting_with_time_evening(self):
        """Test evening greeting."""
        result = self.greeting.get_greeting_with_time("Charlie", "evening")
        assert result == "Good evening, Charlie!"
    
    def test_get_greeting_with_time_case_insensitive(self):
        """Test time-specific greeting is case insensitive."""
        result1 = self.greeting.get_greeting_with_time("Alice", "MORNING")
        result2 = self.greeting.get_greeting_with_time("Alice", "Morning")
        result3 = self.greeting.get_greeting_with_time("Alice", "morning")
        
        expected = "Good morning, Alice!"
        assert result1 == expected
        assert result2 == expected
        assert result3 == expected
    
    def test_get_greeting_with_time_invalid_time(self):
        """Test invalid time of day raises ValueError."""
        with pytest.raises(ValueError, match="Time of day must be one of: morning, afternoon, evening"):
            self.greeting.get_greeting_with_time("Alice", "night")
            
        with pytest.raises(ValueError, match="Time of day must be one of: morning, afternoon, evening"):
            self.greeting.get_greeting_with_time("Alice", "midday")
    
    def test_get_greeting_with_time_invalid_name(self):
        """Test time greeting with invalid name."""
        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            self.greeting.get_greeting_with_time("", "morning")
            
        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            self.greeting.get_greeting_with_time(None, "morning")


class TestGreetingIntegration:
    """Integration tests for Greeting class."""
    
    def test_multiple_greetings_sequence(self):
        """Test using multiple greeting methods in sequence."""
        greeting = Greeting()
        
        hello = greeting.say_hello("Gabriel")
        morning = greeting.get_greeting_with_time("Gabriel", "morning")
        goodbye = greeting.say_goodbye("Gabriel")
        
        assert hello == "Hello, Gabriel!"
        assert morning == "Good morning, Gabriel!"
        assert goodbye == "Goodbye, Gabriel!"
    
    def test_class_instantiation(self):
        """Test that multiple instances work independently."""
        greeting1 = Greeting()
        greeting2 = Greeting()
        
        result1 = greeting1.say_hello("User1")
        result2 = greeting2.say_hello("User2")
        
        assert result1 == "Hello, User1!"
        assert result2 == "Hello, User2!"
        assert result1 != result2