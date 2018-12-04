from _tester import run_test


def add3(a, b, c):
    return a + b + c


def test_given_correct_inputs_and_outputs_should_be_success():
    assert run_test(add3, [1, 2, 3, 6])['outcome'] == 'success'


def test_given_incorrect_inputs_and_outputs_should_be_failure():
    assert run_test(add3, [1, 2, 3, 4])['outcome'] == 'failure'


def test_given_inputs_causing_error_should_be_error():
    assert run_test(add3, [1, '2', 3, 4])['outcome'] == 'error'
