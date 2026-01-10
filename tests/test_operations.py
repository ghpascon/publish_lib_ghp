"""Tests for the operations module."""

from src.publish_lib_example.operations import Operations


class TestOperations:
    """Test class for Operations functionality."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.operations = Operations()
    
    def test_add_basic(self):
        """Test basic addition functionality."""
        result = self.operations.add(2, 3)
        assert result == 5
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        test_cases = [
            (1, 1, 2),
            (5, 10, 15),
            (100, 200, 300),
            (0, 5, 5),
        ]
        
        for a, b, expected in test_cases:
            result = self.operations.add(a, b)
            assert result == expected
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        test_cases = [
            (-1, -1, -2),
            (-5, 10, 5),
            (10, -5, 5),
            (-10, -20, -30),
        ]
        
        for a, b, expected in test_cases:
            result = self.operations.add(a, b)
            assert result == expected
    
    def test_add_zero(self):
        """Test addition with zero."""
        assert self.operations.add(0, 0) == 0
        assert self.operations.add(5, 0) == 5
        assert self.operations.add(0, -5) == -5
    
    def test_add_large_numbers(self):
        """Test addition with large numbers."""
        result = self.operations.add(999999999, 1)
        assert result == 1000000000
        
        result = self.operations.add(-999999999, -1)
        assert result == -1000000000


class TestOperationsIntegration:
    """Integration tests for Operations class."""
    
    def test_multiple_operations_sequence(self):
        """Test using multiple operations in sequence."""
        operations = Operations()
        
        result1 = operations.add(5, 3)
        result2 = operations.add(result1, 2)
        result3 = operations.add(result2, -5)
        
        assert result1 == 8
        assert result2 == 10
        assert result3 == 5
    
    def test_class_instantiation(self):
        """Test that multiple instances work independently."""
        ops1 = Operations()
        ops2 = Operations()
        
        result1 = ops1.add(10, 20)
        result2 = ops2.add(5, 15)
        
        assert result1 == 30
        assert result2 == 20
        assert result1 != result2