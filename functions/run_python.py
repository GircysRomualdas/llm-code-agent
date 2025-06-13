import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python3", abs_file_path],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir
        )

        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout.strip()}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr.strip()}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not output:
            return "No output produced."
        return "\n\n".join(output)
    except Exception as e:
        return f"Error: writing to file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=(
        "Executes a Python (.py) file located in the working directory and returns the output, "
        "including STDOUT, STDERR, and exit code. Execution is limited to 30 seconds."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python (.py) file to execute, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
