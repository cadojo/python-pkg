"""
Interact with Python environments.
"""

__export__ = {
    "update",
    "packages",
    "manifest",
    "registries",
    "PythonEnvironment",
}

from typing import Protocol, Literal
from .package import PythonPackage
from .registry import PackageRegistry

__envfile__: Literal["pkg.toml"] = "pkg.toml"
__envlock__: Literal["pkg.lock"] = "pkg.lock"


class PythonEnvironment(Protocol):
    """
    An abstract interface for a Python environment.
    """

    __env_path__: str

    def __env_update__(self, *packages: str, cautious: bool = False) -> None:
        """
        Update every package in the environment. If cautious is set to False, an "eager"
        update style is applied, and every package dependency is also checked for
        update-ability.
        """

    def __env_registries__(self) -> set[PackageRegistry]:
        """
        Return all available registires added to this environment.
        """

    def __env_packages__(self) -> set[PythonPackage]:
        """
        Return the set of explicitly installed Python packages.
        """

    def __env_manifest__(self) -> set[PythonPackage]:
        """
        Return the set of all installed Python packages (explicitly, or implicitly).
        """


def update(env: PythonEnvironment, *packages: str, cautious: bool = False) -> None:
    """
    Update every package in the environment. If cautious is set to False, an "eager" update
    strategy is applied where every's package's dependencies are also evaluated for possible
    updates.
    """
    return env.__env_update__(*packages, cautious=cautious)


def registries(env: PythonEnvironment) -> set[PackageRegistry]:
    """
    Return the registries added to the provided environment.
    """
    return env.__env_registries__()


def packages(env: PythonEnvironment) -> set[PythonPackage]:
    """
    Return the packages installed to the provided environment.
    """
    return env.__env_packages__()


def manifest(env: PythonEnvironment) -> set[PythonPackage]:
    """
    Return all packages within the provided environment.
    """
    return env.__env_manifest__()


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
