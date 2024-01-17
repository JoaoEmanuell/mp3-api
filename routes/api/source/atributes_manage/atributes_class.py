from .interfaces import AtributeClassInterface


class AtributeClass(AtributeClassInterface):
    @classmethod
    def mangle_attribute(cls, source: object, attr: str) -> str:
        # return public attrs unchanged
        if not attr.startswith("__") or attr.endswith("__") or "." in attr:
            return attr
        # if source is an object, get the class
        if not hasattr(source, "__bases__"):
            source = source.__class__
        # mangle attr
        return "_%s%s" % (source.__name__.lstrip("_"), attr)

    @classmethod
    def setattr(cls, obj: object, name: str, value: object) -> None:
        setattr(obj, cls.mangle_attribute(obj, name), value)

    @classmethod
    def getattr(cls, obj: object, name: str) -> object:
        return getattr(obj, cls.mangle_attribute(obj, name))

    @classmethod
    def delattr(cls, obj: object, name: str) -> None:
        delattr(obj, cls.mangle_attribute(obj, name))

    @classmethod
    def hasattr(cls, obj: object, name: str) -> bool:
        return hasattr(obj, cls.mangle_attribute(obj, name))
