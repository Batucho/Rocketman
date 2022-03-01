from spacemanpy.types.history import HistoricEventData


class HistoricEvent:
    def __init__(self, data: HistoricEventData):
        self._update(data)

    def _update(self, data: HistoricEventData):
        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "title": self.title,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
