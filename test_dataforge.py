# test_dataforge.py
"""
Tests for DataForge module.
"""

import unittest
from dataforge import DataForge

class TestDataForge(unittest.TestCase):
    """Test cases for DataForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataForge()
        self.assertIsInstance(instance, DataForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
