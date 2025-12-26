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




def get_spark_version():
    try:
        spark_version = pyspark.__version__
        print(f"PySpark version: {spark_version}")
        spark_path = pyspark.__path__
        print(f"PySpark version: {spark_path}")       
    except Exception as e:
        print(f"Error while retrieving PySpark version: {e}")

def get_java_info():
    # Check if 'java' command exists in PATH
    java_path = shutil.which("java")
    if java_path is None:
        print("Java is not installed or not found in system PATH.")
        return

    print(f"Java executable path: {java_path}")

    try:
        # Get Java version
        # 'java -version' outputs to stderr, so we capture that
        result = subprocess.run(
            ["java", "-version"],
            capture_output=True,
            text=True
        )
        if result.stderr:
            print("Java version info:")
            print(result.stderr.strip())
        else:
            print("Unable to retrieve Java version.")
    except FileNotFoundError:
        print("Java command not found.")
    except Exception as e:
        print(f"Error while checking Java version: {e}")

if __name__ == "__main__":
    print_environment_variables()
    get_java_info()
    get_spark_version()
