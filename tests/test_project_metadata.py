from pathlib import Path

def test_core_project_documents_exist():
    root = Path(__file__).resolve().parents[1]
    for relative in (
        "README.md",
        "README_CN.md",
        "docs/model-catalog.md",
        "docs/evaluation-protocol.md",
        "docs/data-standard.md",
    ):
        assert (root / relative).is_file(), relative
