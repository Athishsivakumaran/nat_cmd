import subprocess
import ollama
import re
import os, sys
import yaml

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)


OLLAMA_MODEL = config["ollama"]["model"]
SYSTEM_MESSAGE = config["ollama"]["system_message"]
DEBUG = config["general"]["debug"]

def get_shell_command(natural_text):
    response = ollama.chat(
        model=OLLAMA_MODEL, 
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": f"Current directory: {os.getcwd()}"},
            {"role": "user", "content": natural_text}
        ]
    )
    return response['message']['content'].strip()

def extract_command(response):
    match = re.search(r'```.*?\n(.*?)\n```', response, re.DOTALL)
    extracted = match.group(1).strip() if match else response.strip()
    return extracted

def execute_command(command):
    try:
        output = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        if DEBUG:
            print(f"[DEBUG] Running: {command}", file=sys.stderr)
        if output.returncode == 0:
            print(output.stdout, file=sys.stderr)  # Print to stderr instead of stdout
            return command  # Return just the command for eval
        else:
            error_message = f"Error: {output.stderr.strip()}"
            print(error_message, file=sys.stderr)  # Print to stderr instead of stdout
            return "echo 'Command failed'"  # Return a harmless command
    except Exception as e:
        print(f"Execution failed: {e}", file=sys.stderr)  # Print to stderr instead of stdout
        return "echo 'Command failed'"  # Return a harmless command

if __name__ == "__main__":
    user_query = " ".join(sys.argv[1:])
    shell_command = get_shell_command(user_query)
    extracted_command = extract_command(shell_command)
    
    # Print informational message to stderr so it doesn't get eval'd
    print(f"Executing in {os.getcwd()}: {extracted_command}", file=sys.stderr)
    
    # Only output the command itself to stdout for eval
    print(extracted_command)
