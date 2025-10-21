import importlib.util
import os


def test_import_build_pipeline():
    """Import the agents/Phi3_mini.py module by file path and check build_pipeline is present."""
    repo_root = os.path.dirname(os.path.dirname(__file__))
    module_path = os.path.join(repo_root, "agents", "Phi3_mini.py")
    spec = importlib.util.spec_from_file_location("phi3_mini", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert hasattr(module, "build_pipeline"), "build_pipeline not found in Phi3_mini.py"
    assert callable(module.build_pipeline)
