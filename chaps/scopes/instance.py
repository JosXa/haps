from typing import Any, Callable

from chaps.scopes import Scope


class InstanceScope(Scope):
    """
    Dependencies within InstanceScope are created every injection.
    """

    def get_object(self, type_: Callable) -> Any:
        return type_()
