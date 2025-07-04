# tests/test_sanity.py
def test_math():
    assert 1 + 1 == 2


def test_env_check():
    """Ensure basic environment is working."""
    import optuna
    import pandas
    import torch

    assert pandas.__version__
    assert torch.__version__
    assert optuna.__version__
