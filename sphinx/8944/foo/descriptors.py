class CustomDescriptor:
    """A custom descriptor class."""
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return "value"
