from typing import Any, Dict, List, Optional, Union


class Storage:
    """Abstract base class defining the storage interface"""

    def save(self, value: Any, metadata: Dict[str, Any]) -> None:
        pass

    def search(self, key: str) -> Dict[str, Any]:  # type: ignore
        pass

    def reset(self) -> None:
        pass


class LTMStorage:
    """Abstract base class for Long-term storage"""

    def save(
        self,
        task_description: str,
        metadata: Dict[str, Any],
        datetime: str,
        score: Union[int, float],
    ) -> None:
        pass

    def load(
        self, task_description: str, latest_n: int
    ) -> Optional[List[Dict[str, Any]]]:
        pass

    def reset(self) -> None:
        pass
