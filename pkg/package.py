"""
Interact with Python packages, and make sure to store where they came from!
"""

__export__ = {
    "name",
    "uuid",
    "registry",
    "PythonPackage",
}

from typing import Protocol, Optional
from .registry import PackageRegistry


class PythonPackage(Protocol):
    """
    An abstract interface for any type which describes a Python package!
    """

    __pkg_name__: str
    __pkg_uuid__: str
    __pkg_registry__: Optional[PackageRegistry]


def name(package: PythonPackage) -> str:
    """
    Return the install-able name of the package.
    """
    return package.__pkg_name__


def uuid(package: PythonPackage) -> Optional[str]:
    """
    Return the universally unique identifier (UUID) for the provided package.
    """
    return package.__pkg_uuid__


def registry(package: PythonPackage) -> Optional[PackageRegistry]:
    """
    Return the package registry used to install the package.
    """
    return package.__pkg_registry__


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
