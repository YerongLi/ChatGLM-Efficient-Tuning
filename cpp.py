import subprocess

def run_command_with_input(command, input_string):
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    stdout, stderr = process.communicate(input_string)
    return stdout, stderr

def main():
    input_string = input("Enter a string: ")

    command = ["./build/bin/main", "-m", "chatglm-ggml.bin", "-p", input_string]

    stdout, stderr = run_command_with_input(command, input_string)
    if stdout:
        print("Standard Output:")
        print(stdout)
    if stderr:
        print("Standard Error:")
        print(stderr)

if __name__ == "__main__":
    main()
