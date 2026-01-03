
from typing import Any

# The tests are defined as such:
# def validate_{topLevelConfig}(relevantConfig: {correct type}) -> bool:
# where "topLevelConfig" is replaced by the name of every single top level key (e.g., basics, bgp, container, etc.)
# Ensure that the test returns True/False based on the result
# Add the function object itself for the test as a value to the enabledTest dict (key = description of the test)

def validate_basics(relevantConfig: dict[str, Any]) -> bool:
    """Test to validate the configuration included in the basics top-level section"""
    pass

def validate_bgp(relevantConfig: dict[str, Any]) -> bool:
    """Test to validate the configuration included in the bgp top-level section"""
    pass

def validate_container(relevantConfig: dict[str, Any]) -> bool:
    """Test to validate the configuration included in the container top-level section"""
    # Validate that it is an eBGP peering
    pass

def validateConfig(config: dict[str, Any]) -> None:
    """Run all enabled tests against the provided configuration and handle/raise failures/exceptions as required"""
    enabledTests = {
        "Validate the basic functionality of the "
    }
    for test in enabledTests:
        enabledTests[test]()