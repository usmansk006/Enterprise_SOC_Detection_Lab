import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "06-local-analysis-toolkit" / "event-correlator.py"


def test_correlates_by_guid(tmp_path):
    events = [
        {
            "timestamp": "2026-10-28T14:00:00Z",
            "process_name": "mshta.exe",
            "pid": 4400,
            "process_guid": "{GUID-1}",
            "parent_process_name": "powershell.exe",
        },
        {
            "timestamp": "2026-10-28T14:00:30Z",
            "process_name": "powershell.exe",
            "pid": 4420,
            "process_guid": "{GUID-1}",
            "parent_process_name": "cmd.exe",
        },
    ]
    p = tmp_path / "events.json"
    p.write_text(json.dumps(events), encoding="utf-8")
    result = subprocess.run([sys.executable, str(SCRIPT), "--input", str(p)], capture_output=True, text=True, check=True)
    assert "GUID-1" in result.stdout
