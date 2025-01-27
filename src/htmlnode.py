class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return ''

        s = ''
        for k, v in self.props.items():
            s += f' {k}="{v}"'

        return s

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self):
        return f'tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)
        if self.value == None:
            raise ValueError()
    
    def to_html(self):
        if self.tag == None:
            return self.value
        if self.tag == 'img':
            return f'<{self.tag}{self.props_to_html()} />'

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
        if self.children != None:
            for child in self.children:
                if child == None:
                    raise ValueError('None is not a valid child value')
   
    def to_html(self):
        if self.tag == None:
            raise ValueError()
        if self.children == None:
            raise ValueError('Children can not be None')
        
        html = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html += child.to_html()
        html += f'</{self.tag}>'

        return html

