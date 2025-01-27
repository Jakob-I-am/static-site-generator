import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode('p', [
            LeafNode('b', 'Bold'),
            LeafNode(None, 'Normal'),
            LeafNode('i', 'Italic')
        ])
        html = '<p><b>Bold</b>Normal<i>Italic</i></p>'
        self.assertEqual(node.to_html(), html)

    def test_to_html_with_None_props(self):
        node = ParentNode('div', [], None)
        html = '<div></div>'
        self.assertEqual(node.to_html(), html)

    def test_to_html_with_nested_parentnodes(self):
        node = ParentNode('div', [
            ParentNode('p', [
                LeafNode('b', 'Nested')
            ])
        ])
        html = '<div><p><b>Nested</b></p></div>'
        self.assertEqual(node.to_html(), html)

    def test_error_None_children(self):
        with self.assertRaises(ValueError):
            ParentNode('div', None).to_html()

    def test_error_None_child(self):
        with self.assertRaises(ValueError):
            ParentNode('p', [LeafNode('b', 'Nested'), None], {'class': 'text-sm text-red-500'})

if __name__ == '__main__':
    unittest.main()
