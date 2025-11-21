import pytest

from main import hello, main


def test_hello():
    assert hello() == "Hello World!"


def test_main_prints(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from extra-points-task0!" in captured.out
