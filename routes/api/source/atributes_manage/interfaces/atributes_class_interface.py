from abc import ABC, abstractclassmethod


class AtributeClassInterface(ABC):

    """
    This class is an interface for the AtributeClass.
    AtributeClass is a class that contains methods of the manage atributes of a class.

    Args:
        ABC (_type_): Abstract Base Class

    Raises:
        NotImplementedError: NotImplementedError
    """

    @abstractclassmethod
    def mangle_attribute(cls, source: object, attribute: str) -> str:
        """
        Mangle the attribute of the source object.
        Unpack the attribute for manage it.

        Args:
            source (object): Source object.
            attribute (str): Attribute name.

        Raises:
            NotImplementedError: NotImplementedError
        """

        raise NotImplementedError()

    @abstractclassmethod
    def setattr(cls, obj: object, name: str, value: object) -> None:
        """
        Set the attribute of the object.

        Args:
            obj (object): Object.
            name (str): Attribute name.
            value (object): New attribute value.

        Raises:
            NotImplementedError: NotImplementedError
        """

        raise NotImplementedError()

    @abstractclassmethod
    def getattr(cls, obj: object, name: str) -> object:
        """
        Get the attribute of the object.

        Args:
            obj (object): Object.
            name (str): Attribute name.

        Raises:
            NotImplementedError: NotImplementedError
        """

        raise NotImplementedError()

    @abstractclassmethod
    def delattr(cls, obj: object, name: str) -> None:
        """
        Delete the attribute of the object.

        Args:
            obj (object): Object.
            name (str): Attribute name.

        Raises:
            NotImplementedError: NotImplementedError
        """

        raise NotImplementedError()

    @abstractclassmethod
    def hasattr(cls, obj: object, name: str) -> bool:
        """
        Check if the object has the attribute.

        Args:
            obj (object): Object.
            name (str): Attribute name.

        Raises:
            NotImplementedError: NotImplementedError
        """

        raise NotImplementedError()
