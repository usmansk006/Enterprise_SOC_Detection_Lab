import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "06-local-analysis-toolkit" / "rule-validator.py"
RULE = ROOT / "02-detections" / "DET-001-mshta-execution" / "det-001-mshta-execution.yml"


def test_accepts_basic_rule():
    result = subprocess.run([sys.executable, str(SCRIPT), "--input", str(RULE)], capture_output=True, text=True, check=True)
    assert "passed" in result.stdout.lower()


def test_rejects_missing_title(tmp_path):
    bad = tmp_path / "bad.yml"
    bad.write_text("id: 123\nstatus: experimental\nlogsource:\n  product: windows\ndetection: {}\n", encoding="utf-8")
    result = subprocess.run([sys.executable, str(SCRIPT), "--input", str(bad)], capture_output=True, text=True)
    assert result.returncode != 0
