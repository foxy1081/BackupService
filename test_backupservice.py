# test_backupservice.py
"""
Tests for BackupService module.
"""

import unittest
from backupservice import BackupService

class TestBackupService(unittest.TestCase):
    """Test cases for BackupService class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BackupService()
        self.assertIsInstance(instance, BackupService)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BackupService()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
