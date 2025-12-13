import subprocess

def test_help():
    result = subprocess.run(["python", "src/nxwitness_healthcheck/cli.py", "--help"], capture_output=True)
    assert result.returncode == 0
