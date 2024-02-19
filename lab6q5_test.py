import lab6q5
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('1\n10\n30\nn\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q5.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'86.0F') != -1
    assert captured_stdout.strip().find(f'84.2F') != -1
    assert captured_stdout.strip().find(f'50.0F') != -1
    assert captured_stdout.strip().find(f'51.8F') != -1

def test_case1a(monkeypatch, capsys):
    number_inputs = StringIO('1\n10\n30\ny\n2\n60\n40\nn\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q5.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'Invalid Input') != -1

def test_case1b(monkeypatch, capsys):
    number_inputs = StringIO('1\n10\n30\ny\n3\nn\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q5.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'Invalid Selection!') != -1

def test_case1c(monkeypatch, capsys):
    number_inputs = StringIO('1\n10\n30\ny\n3\ny\n2\n30\n40\nn\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q5.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'-0.6C') != -1
    assert captured_stdout.strip().find(f'4.4C') != -1

def test_case1d(monkeypatch, capsys):
    number_inputs = StringIO('1\n10\n20\nu\nu\ny\n1\n40\n50\nn\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q5.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'104.0F') != -1
    assert captured_stdout.strip().find(f'122.0F') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab6q5.py") as tf:
    head = [next(tf) for _ in range(15)]
    s = tf.read().rsplit("\n",5)[0]
    assert(s.find("for") != -1 )
