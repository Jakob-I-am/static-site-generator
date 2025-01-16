import unittest

from htmlnode import HTMLNode

class testHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode('h1', 'Heading', None, {'class': 'mb-2'})
        node2 = HTMLNode('h1', 'Heading', None, {'class': 'mb-2'})
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = HTMLNode('h1', 'Heading', None, {'class': 'mb-2'})
        node2 = HTMLNode('h1', 'Heading', [HTMLNode('p', 'This is a paragraph', None, None)], {'class': 'mb-2'})
        self.assertNotEqual(node1, node2)

    def test_default_values(self):
        node = HTMLNode()
        self.assertIsNone(node.children)

    def test_props_to_html(self):
        node = HTMLNode('h1', 'Heading', None, {'class': 'mb-2'})
        t = node.props_to_html()
        self.assertEqual(t, ' class="mb-2"')

if __name__ == '__main__':
   unittest.main() 
