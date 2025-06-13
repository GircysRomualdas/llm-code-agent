import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file


def main():
    verbose = False
    try:
        user_prompt = sys.argv[1]
        if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
            verbose = True
    except:
        print("Usage:")
        print('\tpython main.py "your prompt here" [--verbose]')
        sys.exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        try:
            function_call_result = call_function(function_call_part, verbose)
            print(f"-> {function_call_result.parts[0].function_response.response}")
        except Exception as e:
            raise Exception("Error: call function")

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_call_part.args["working_directory"] = "./calculator"
    match function_call_part.name:
        case "get_file_content":
            function_result = get_file_content(**function_call_part.args)
        case "get_files_info":
            function_result = get_files_info(**function_call_part.args)
        case "run_python_file":
            function_result = run_python_file(**function_call_part.args)
        case "write_file":
            function_result = write_file(**function_call_part.args)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_result},
            )
        ],
    )

if __name__ == "__main__":
    main()
