from typing import Any
from pathlib import Path
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class PkgBuilder(BuildHookInterface):
    """
    Includes custom package metadata contained under "tool.pkg.project".
    """

    def initialize(self, version: str, build_data: dict[str, Any]):
        """
        An intialization step, followed by writing a temporary metadata file.
        """
        super().initialize(version, build_data)
        
        try:
            uuid = self.config["tool"]["pkg"]["project"]["uuid"]
        except KeyError:
            return

        with open("UUID.txt", "w") as file:
            file.write(f"{uuid}\n")
        
        build_data.extra_metadata["UUID.txt"] = "UUID"

    def finalize(self, version: str, build_data: dict[str, Any], artifact_path: str):
        """
        A final step to clean up the temporary metadata file created in initialize.
        """
        super().finalize(version, build_data, artifact_path)
        Path("UUID.txt").unlink(missing_ok=True)

    