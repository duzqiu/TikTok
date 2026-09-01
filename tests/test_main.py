"""
Tests for TikTok app.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def test_main():
    """Test that main module can be imported."""
    import src.main
    assert hasattr(src.main, 'main')
