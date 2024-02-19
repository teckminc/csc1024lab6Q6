import lab6q6
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('22\n24\n56\n31\n32\n6\n89\n99\n66\n77\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q6.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'99') != -1
    assert captured_stdout.strip().find(f'1') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab6q6.py") as tf:
    head = [next(tf) for _ in range(28)]
    s = tf.read()
    assert(s.find("for") != -1 )

def test_case3(monkeypatch, capsys):
  with open(f"lab6q6.py") as tf:
    head = [next(tf) for _ in range(28)]
    s = tf.read()
    assert(s.find("min(") == -1 )

def test_case3(monkeypatch, capsys):
  with open(f"lab6q6.py") as tf:
    head = [next(tf) for _ in range(28)]
    s = tf.read()
    assert(s.find("max(") == -1 )





