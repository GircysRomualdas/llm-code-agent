import os

def get_files_info(working_directory, directory="."):
    try:
        actual_target = os.path.join(working_directory, directory)
        working_directory_abs = os.path.abspath(working_directory)
        target_directory_abs = os.path.abspath(actual_target)
        base_safe_zone = os.path.dirname(working_directory_abs)

        if not (target_directory_abs == base_safe_zone or target_directory_abs.startswith(base_safe_zone + os.sep)):
            return f'Error: Cannot list \"{directory}\" as it is outside the permitted working directory'

        if not os.path.isdir(target_directory_abs):
            return f'Error: \"{directory}\" is not a directory'

        contents = ""
        for item in os.listdir(target_directory_abs):
            full_path = os.path.join(target_directory_abs, item)
            contents += (
                f"- {item}: file_size={os.path.getsize(full_path)} bytes, "
                f"is_dir={os.path.isdir(full_path)}\n"
            )

        return contents
    except Exception as e:
        return f"Error: {e}"

