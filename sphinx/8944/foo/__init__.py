from dataclasses import dataclass, field
from foo.descriptors import CustomDescriptor

@dataclass
class Foo:
    my_field: list = field(default_factory=list)
    """example class attribute"""

    custom_descr = CustomDescriptor()
    """example custom descriptor"""

    @property
    def name(self):
        """example instance property"""
        return "Foo"

