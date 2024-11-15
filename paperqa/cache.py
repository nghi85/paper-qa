from typing import Optional, Any

class Cache:
    _index: Optional[Any] = None

    @classmethod
    def set_index(cls, index: Any):
        cls._index = index

    @classmethod
    def get_index(cls) -> Optional[Any]:
        return cls._index