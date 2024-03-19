import json
import uuid

from distutils.version import LooseVersion

from bitbucket_service import BitbucketService


class DependencyUpdater:
    def __init__(self, bitbucket_service: BitbucketService, package_file_path: str = "package.json"):
        self.bitbucket_service = bitbucket_service
        self.package_file_path = package_file_path

        # TODO: validate the package.json file structure
        self.package_json = self.bitbucket_service.get_file_content(self.package_file_path)

    def update_dependency_file(self, dependency_name: str, dependency_version: str):
        # TODO: validate dependency and version availability in the NPM repository

        if not self.validate_and_update_dependency_version(dependency_name, dependency_version):
            return

        # Uuid is used to make the branch name unique
        branch_name = f"update-{dependency_name}-to-{dependency_version}-{uuid.uuid4()}"
        branch_data = self.bitbucket_service.create_branch(branch_name)
        branch_hash = branch_data["target"]["hash"]

        self.bitbucket_service.upload_file(
            branch_name=branch_name,
            content=json.dumps(self.package_json, indent=2),
            filename=self.package_file_path,
            message=f"Update {dependency_name} dependency to {dependency_version} version",
            source_commit_id=branch_hash
        )

        # TODO: check pull request availability for the current branch
        pull_request_data = self.bitbucket_service.create_pull_request(
            title=f"Update {dependency_name} dependency version",
            description=f"Update {dependency_name} dependency to {dependency_version} version",
            source_branch=branch_name,
        )
        pull_request_link = pull_request_data["links"]["html"]["href"]
        print(f"Pull request created by the link - {pull_request_link}")

    def validate_and_update_dependency_version(self, dependency_name: str, dependency_version: str) -> bool:
        # TODO: check for missing dependency section
        dependencies = self.package_json.get("dependencies", {})
        source_dependency_version = dependencies.get(dependency_name)

        if not source_dependency_version:
            print(f"Dependency `{dependency_name}` not found in dependencies section")
            return False

        # TODO: Add checks for versions with letters and special characters (~xx.xx.xx and ^xx.xx.xx)
        # Not allowed to update to an older version
        if LooseVersion(dependency_version) > LooseVersion(source_dependency_version):
            print(f"Updating dependency [{dependency_name}] from {source_dependency_version} "
                  f"to {dependency_version} version")
            dependencies[dependency_name] = dependency_version
            return True
        else:
            print(f"Current [{dependency_name}] dependency version ({source_dependency_version}) "
                  f"is greater than {dependency_version}")
            return False
