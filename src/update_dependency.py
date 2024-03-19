import argparse
from bitbucket_service import BitbucketService
from dependency_updater import DependencyUpdater


def parse_args(args=None):
    argument_parser = argparse.ArgumentParser(description="Dependency updater")
    argument_parser.add_argument("dependency_name", type=str, help="Dependency name")
    argument_parser.add_argument("dependency_version", type=str, help="Dependency version")
    argument_parser.add_argument("bitbucket_workspace", type=str, help="Bitbucket workspace")
    argument_parser.add_argument("bitbucket_repository", type=str, help="Bitbucket repository")
    argument_parser.add_argument("bitbucket_token", type=str, help="Bitbucket access token")
    return argument_parser.parse_args(args)


if __name__ == '__main__':
    parser = parse_args()
    bitbucket_service = BitbucketService(parser.bitbucket_token, parser.bitbucket_workspace,
                                         parser.bitbucket_repository)
    dependency_updater = DependencyUpdater(bitbucket_service)
    dependency_updater.update_dependency_file(parser.dependency_name, parser.dependency_version)
