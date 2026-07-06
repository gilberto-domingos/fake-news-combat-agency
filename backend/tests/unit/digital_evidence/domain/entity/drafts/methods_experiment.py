class MethodsExperiment:
    def __init__(self, is_active: bool, keywords: list[str]):
        self._is_active = is_active
        self._keywords = keywords

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value

    @property
    def keywords(self) -> list[str]:
        return self._keywords

    @keywords.setter
    def keywords(self, value: list[str]) -> None:
        self._keywords = value

    def activate(self) -> bool:
        self._is_active = True
        return self._is_active

    def deactivate(self) -> bool:
        self._is_active = False
        return self._is_active

    def activate2(self) -> None:
        if self._is_active:
            raise ValueError("Target is already is active")
        self._is_active = True

    def deactivate2(self) -> None:
        if not self._is_active:
            raise ValueError("Target is already is deactivate")
        self._is_active = False

    def if_monitoring(self) -> bool:
        return self._is_active

    def add_keywords(self, keywords: list[str]) -> None:
        self._keywords.extend(keywords)

    def update_keywords(self, keywords: list[str]) -> None:
        self._keywords = keywords

    def __str__(self) -> str:
        return f"Methods Experiment(is_active={self.is_active}, keywords={self.keywords})"
