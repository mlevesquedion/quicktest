from quicktest.summary import summarize


def test_summarize():
    summary = [
        {'outcome': 'success'},
        {'outcome': 'success'},
        {'outcome': 'failure', 'info': 'failure 1'},
        {'outcome': 'error', 'info': 'error 1'}
    ]
    expected = {
        'test_count': 4,
        'success_count': 2,
        'failure_count': 2,
        'error_count': 1,
        'failures': ['failure 1'],
        'errors': ['error 1']
    }
    assert summarize(summary) == expected
