class ExtractLogInfosError(Exception):
    def __init__(self, message: str = "Extract Log Infos Error") -> None:
        """Init

        Args:
            message (str, optional):
                Error message. Defaults to 'Extract Log Infos Error'.

        """
        self.__message = message
        super().__init__(self.__message)

    def __str__(self) -> str:
        return self.__message
