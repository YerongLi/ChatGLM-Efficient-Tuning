import subprocess
buffered_history = [
    ("Harry, what is your favorite spell that you've learned at Hogwarts?", "Expelliarmus has always been a favorite of mine."),
    ("Which magical artifact or object from the wizarding world do you find the most intriguing?", "The Marauder's Map has always fascinated me."),
    ("If you could spend a day with any character from Hogwarts history, who would it be and why?", "I would love to spend a day with Godric Gryffindor."),
    ("Among all the Quidditch matches you've played, which one stands out as the most memorable for you?", "The match against Slytherin in my third year was particularly memorable.")
]

buffered_string = '\n'.join([f'{question}\n{answer}' for question, answer in history])
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

    stdout, stderr = run_command_with_input(command, buffered_string+input_string)
    if stdout:
        print("Standard Output:")
        print(stdout)
    if stderr:
        print("Standard Error:")
        print(stderr)

if __name__ == "__main__":
    main()
