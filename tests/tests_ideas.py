# BitbucketService
def test_create_branch():
    # TODO: service should return correct branch name and default_branch hash

def test_create_pull_request():
    # TODO: service should return correct pull request info (description, source_branch, title)

def test_get_file_content():
    # TODO: service should return correct data from mock

def test_upload_file():
    # TODO: service should upload data correctly from mock

# DependencyUpdater
def test_validate_and_update_dependency_version():
    # TODO: test should return different results of validation for combinations of source and new dependency versions

def test_update_dependency_file():
    # TODO: test should check that DependencyUpdater calls the entire chain of methods from BitbucketService
