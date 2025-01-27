import unittest

from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node

class Test_text_node_to_html_node(unittest.TestCase):
    def test_text_node_to_html_node(self):
        node = TextNode('Just text', TextType.TEXT)
        html = text_node_to_html_node(node).to_html()
        self.assertEqual(html, 'Just text')

        node = TextNode('Bold text', TextType.BOLD)
        html = text_node_to_html_node(node).to_html()
        self.assertEqual(html, '<b>Bold text</b>')

        node = TextNode('Italic text', TextType.ITALIC)
        html = text_node_to_html_node(node).to_html()
        self.assertEqual(html, '<i>Italic text</i>')

        node = TextNode('Code text', TextType.CODE)
        html = text_node_to_html_node(node).to_html()
        self.assertEqual(html, '<code>Code text</code>')

        node = TextNode('Link text', TextType.LINK, 'https://google.com')
        html = text_node_to_html_node(node)
        self.assertEqual(html.props['href'], 'https://google.com')
        self.assertEqual(html.to_html(), '<a href="https://google.com">Link text</a>')

        node = TextNode('Alt text', TextType.IMAGE, 'image.com')
        html = text_node_to_html_node(node)
        self.assertEqual(html.props['src'], 'image.com')
        self.assertEqual(html.props['alt'], 'Alt text')
        self.assertEqual(html.to_html(), '<img src="image.com" alt="Alt text" />')

        node = TextNode('Error', TextType.TEXT)
        node.text_type = 'error'
        with self.assertRaises(ValueError):
            text_node_to_html_node(node).to_html()


if __name__ == '__main__':
    unittest.main()
