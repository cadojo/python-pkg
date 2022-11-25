"""
A REST api for interacting with PyPi servers.
"""

__export__ = {
    "metadata",
}

from typing import Any, Optional
from pypi_simple import PYPI_SIMPLE_ENDPOINT
from functools import cache
from os.path import curdir


@cache
def metadata(
    package: str,
    /,
    *,
    url: str = PYPI_SIMPLE_ENDPOINT,
    auth: Optional[tuple[str, str]] = None,
):
    """
    Fetch metadata for the provided package.
    """
    from pypi_simple import PyPISimple

    with PyPISimple(endpoint=url, auth=auth) as client:
        data = client.get_project_page(package)

    return data


@cache
def versions(
    package: str,
    /,
    *,
    url: str = PYPI_SIMPLE_ENDPOINT,
    auth: Optional[tuple[str, str]] = None,
):
    """
    Fetch all available versions of the provided package.
    """
    data = metadata(package, url=url, auth=auth)
    return {
        distribution.version
        for distribution in data.packages
        if distribution.version is not None
    }


@cache
def distribution(
    package: str,
    /,
    *,
    url: str = PYPI_SIMPLE_ENDPOINT,
    auth: Optional[tuple[str, str]] = None,
    version: Optional[str] = None,
):
    """
    Returns a `pypi_simple.DistributionPackage` instance for the specified package, and
    optionally a specific version. If no version is specified, the latest version is used.

    The `to` keyword argument specifies the download location, and defaults to the current
    directory. The `version` keyword argument specifiest the desired package version.
    """
    from packaging.version import parse

    data = metadata(package, url=url, auth=auth)

    vs = [parse(p.version) for p in data.packages]

    if version:

        try:
            i = vs.index(parse(version))
        except ValueError:
            raise ValueError(f"The specified version, {version} was not found!")

        return data.packages[i]

    else:

        packages = sorted(data.packages, key=lambda p: parse(p.version), reverse=True)
        return packages[0]


def download(
    package: str,
    /,
    *,
    url: str = PYPI_SIMPLE_ENDPOINT,
    auth: Optional[tuple[str, str]] = None,
    directory: str = curdir,
    version: Optional[str] = None,
):
    """
    Download the specified package.
    """
    from pathlib import Path
    from requests import get
    dist = distribution(package, url=url, auth=auth, version=version)
    
    response = get(dist.url)
    location = Path(directory) / dist.filename

    with open(location, "wb") as file:
        file.write(response.content)
    


if __name__ == "__main__":
    ...
else:
    import hygiene # type: ignore

    hygiene.cleanup()
