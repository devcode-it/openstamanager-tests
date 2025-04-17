#!/usr/bin/env python3

import json
import subprocess
from pathlib import Path
import sys

def run_tests():
    directory = Path(__file__).parent
    config_file = directory / 'config.json'

    try:
        with open(config_file, 'r', encoding='utf-8') as json_file:
            tests = json.load(json_file)

        for test in tests:
            print(f"\nRunning test: {test}")
            result = subprocess.run(
                [sys.executable, "-m", "unittest", test],
                capture_output=True,
                text=True
            )

            print(result.stdout)

            if result.stderr:
                print(f"Errors: {result.stderr}")

            if result.returncode != 0:
                print(f"Test {test} failed with return code {result.returncode}")

    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_file}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in configuration file {config_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
