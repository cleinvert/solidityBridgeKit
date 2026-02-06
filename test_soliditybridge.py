# test_soliditybridge.py
"""
Tests for solidityBridge module.
"""

import unittest
from soliditybridge import solidityBridge

class TestsolidityBridge(unittest.TestCase):
    """Test cases for solidityBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = solidityBridge()
        self.assertIsInstance(instance, solidityBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = solidityBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
