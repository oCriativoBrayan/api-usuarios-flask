import sys
import os

# Ajuste de path para projeto sem estrutura formal
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import health_check


def test_health_check():
    assert health_check() is True

