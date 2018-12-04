from functools import wraps
from _utils import noun_number
from _summary import summarize


_SEPARATOR = '=' * 50


def print_summary(results):
    summary = summarize(results)
    _print_summary_content(summary)
    _print_failures(summary['failures'])
    _print_errors(summary['errors'])


def _with_printed_prefix(sep):
    # This decorator isn't necessary at all, I'm just having fun
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(sep)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@_with_printed_prefix(_SEPARATOR)
def _print_summary_content(summary):
    _print_test_count(summary)
    _print_success_count(summary)
    _print_failure_count(summary)


@_with_printed_prefix(_SEPARATOR)
def _print_labeled_list(label, lst):
    print(label.upper())
    for x in lst:
        print(x)


def _print_failures(failures):
    if failures:
        _print_labeled_list('failures', failures)


def _print_errors(errors):
    if errors:
        _print_labeled_list('errors', errors)


def _print_test_count(summary):
    test_count = summary['test_count']
    print(f'{test_count} RAN')


def _print_success_count(summary):
    success_count = summary['success_count']
    print(f'{success_count} OK')


def _print_failure_count(summary):
    failure_count = summary['failure_count']
    error_count = summary['error_count']
    if failure_count:
        failure_ending = noun_number(failure_count).upper()
        failure_part = f'{failure_count} FAILURE' + failure_ending
        error_part = f' ({error_count} ERRORS)' if error_count else ''
        print(failure_part + error_part)
