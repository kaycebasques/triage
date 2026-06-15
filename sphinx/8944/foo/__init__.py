from dataclasses import dataclass, field


@dataclass
class Foo:
    field = field(default_factory=list)
    """example class attribute"""

    @property
    def name(self):
        """example instance property"""
        return "Foo"
