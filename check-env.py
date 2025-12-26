import sys
import pyspark
import subprocess
import shutil
import os
import boto3
from pprint import pprint

def print_environment_variables():
    """
    Prints all environment variables in a readable format.
    Works on Windows, macOS, and Linux.
    """
    try:
        # os.environ behaves like a dictionary
        env_vars = dict(os.environ)

        if not env_vars:
            print("No environment variables found.")
            return

        print("=== Environment Variables ===")
        pprint(env_vars)  # Pretty print for readability

    except Exception as e:
        print(f"Error retrieving environment variables: {e}", file=sys.stderr)
