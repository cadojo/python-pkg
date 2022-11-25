"""
Definitions and methods for registries.
"""

__export__ = {
    "add",
    "remove",
    "PackageRegistry",
}

from typing import Protocol


class PackageRegistry(Protocol):
    """
    An abstract interface for Python registries.
    """

    __reg_alias__: str
    __reg_url__: str
    __reg_public__: bool

    def __reg_update__(self) -> None:
        """
        Fetch the latest package metadata changes from the registry.
        """


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
