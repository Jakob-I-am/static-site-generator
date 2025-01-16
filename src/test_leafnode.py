import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode('p', 'This is a paragraph', {'href': 'google.com.au'})
        html = '<p href="google.com.au">This is a paragraph</p>'
        self.assertEqual(node.to_html(), html)

    def test_children_is_none(self):
        node = LeafNode('p', 'This is a paragraph', {'href': 'google.com.au'})
        self.assertIsNone(node.children)

    def test_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode('p', None, {'href': 'google.com.au'})
            
    def test_no_tag(self):
        node = LeafNode(None, 'This is a paragraph', {'href': 'google.com.au'})
        self.assertEqual(node.to_html(), node.value)

if __name__ == '__main__':
    unittest.main()
