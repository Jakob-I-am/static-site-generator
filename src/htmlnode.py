class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
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

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

