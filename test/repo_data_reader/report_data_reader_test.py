import os
from repo_data_reader import yml_reader

path_to_test = os.path.dirname(os.path.abspath(__file__))
_expected_listed_repos_structure = ["repo1", "repo2", "repo3"]
_expected_empty_array = []


def test_read_listed_repos():
    path_to_yml = path_to_test + '/listed_repos.yml'
    received_data = yml_reader.read_repos_list(path_to_yml)
    assert (_expected_listed_repos_structure == received_data)


def test_read_path_repos():
    path_to_yml = path_to_test + '/path_repos.yml'
    received_data = yml_reader.read_repos_list(path_to_yml)
    assert (_expected_empty_array == received_data)


def test_verify_mixed_structures():
    path_to_yml = path_to_test + '/mixed_repos_structure.yml'
    received_data = yml_reader.read_repos_list(path_to_yml)
    assert (_expected_empty_array == received_data)


def test_verify_bad_path_structure():
    path_to_yml = path_to_test + '/bad_path_structure.yml'
    received_data = yml_reader.read_repos_list(path_to_yml)
    assert (_expected_empty_array == received_data)

