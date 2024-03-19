import requests


class BitbucketService:
    def __init__(self, token: str, workspace: str, repository: str, default_branch: str = "main",
                 url: str = "https://api.bitbucket.org/2.0"):
        # TODO: check auth token is valid
        self.auth_header = {"Authorization": f"Bearer {token}"}
        self.default_branch = default_branch
        self.repo_url_prefix = f"{url}/repositories/{workspace}/{repository}"

    def create_branch(self, branch_name: str) -> dict:
        data = {"name": branch_name, "target": {"hash": self.default_branch}}
        # TODO: check branch availability
        response = requests.post(f"{self.repo_url_prefix}/refs/branches", json=data, headers=self.auth_header)
        return response.json()

    def create_pull_request(self, description: str, source_branch: str, title: str,) -> dict:
        data = {
            "title": title,
            "description": description,
            "destination": {
                "branch": {
                    "name": self.default_branch
                }
            },
            "source": {
                "branch": {"name": source_branch}
            }
        }
        response = requests.post(f"{self.repo_url_prefix}/pullrequests", json=data, headers=self.auth_header)
        return response.json()

    def get_file_content(self, filename: str) -> dict:
        response = requests.get(f"{self.repo_url_prefix}/src/{self.default_branch}/{filename}",
                                headers=self.auth_header)
        return response.json()

    def upload_file(self, branch_name: str, content: any, filename: str, message: str, source_commit_id: str):
        data = {
            "branch": branch_name,
            "message": message,
            "parents": [source_commit_id],
        }
        files = {filename: (filename, content)}
        return requests.post(f"{self.repo_url_prefix}/src", data=data, files=files, headers=self.auth_header)
