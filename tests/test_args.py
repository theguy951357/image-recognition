import pytest

import src.core as core


def test_null_args():
    """
    No arguments. Should throw an error on parse attempt.
    """
    args = []
    with pytest.raises(ValueError):
        core.parse_args(args)


def test_arg_validation_invalid():  # Model path can be invalid for this test, it's irrelevant.
    """
    Tests for argument incompatibilities, such as image mode and training mode being triggered simultaneously.
    :return:
    """
    args = [['-i', 'some/path', '-t', 'some/path'], ['-v'], ['-e', '10'],
            ['-i', 'some/path', '-t', 'some/path', '-m', 'some/path', '-v', '-e', '25', '-n', 'my-name',
             '-m', 'some/model']]
    parsed = [core.parse_args(x) for x in args]
    for p in parsed:
        with pytest.raises(ValueError):
            print(f'Testing: {p}')
            _ = core.Config.from_parsed_args(p)
            print(f'Passed: {p}')


def test_arg_validation_valid():
    args = [['-i', 'some/path'], ['-i', 'some/path', '-m', 'some/path'], ['-t', 'some/path', '-e', '50'],
            ['-i', 'some/path', '-m', 'some/path', '-n my-special-name', '-o my/special/path', '-v']]
    parsed = [core.parse_args(x) for x in args]
    for p in parsed:
        print(f'Testing: {p}')
        assert core.Config.from_parsed_args(p)
        print(f'Passed: {p}')
