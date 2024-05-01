class CrudBaseExc(Exception):
    """
        Error raises by one of the incorrect update/create/delete entity operation
        :param entity_id: Record ID from table
        :param entity_name: Name of table
        :param message: Error message
    """

    def __init__(
            self,
            entity_name: str,
            entity_id: int | None = None,
            message: str = "error"
    ):
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.message = message
        self.status_code = status.HTTP_400_BAD_REQUEST
        if self.entity_id is not None:
            super().__init__(f"{self.message} {self.entity_name}, id = {int(self.entity_id)}")
        else:
            super().__init__(f"{self.message} {self.entity_name}")

    def __repr__(self):
        if self.entity_id is not None:
            return f"{self.message} {self.entity_name}, id = {int(self.entity_id)}"
        else:
            return f"{self.message} {self.entity_name}"
