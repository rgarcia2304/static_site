import unittest

from main import *

class TestExtractTitle(unittest.TestCase):
    
    def test_with_header(self):
        txt = "# Hello"

        case = extract_title(txt)

        self.assertEqual(case, "Hello")
    
    def test_with_no_header(self):
        text = "hello"
        with self.assertRaises(Exception) as cm:
            extract_title(text)
    
        self.assertEqual(str(cm.exception), "No header")
if __name__ == "__main__":
    unittest.main()
