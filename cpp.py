import subprocess
buffered_history = [
    ("Harry, what is your favorite spell that you've learned at Hogwarts?", "Expelliarmus has always been a favorite of mine."),
    ("Which magical artifact or object from the wizarding world do you find the most intriguing?", "The Marauder's Map has always fascinated me."),
    ("If you could spend a day with any character from Hogwarts history, who would it be and why?", "I would love to spend a day with Godric Gryffindor."),
    ("Among all the Quidditch matches you've played, which one stands out as the most memorable for you?", "The match against Slytherin in my third year was particularly memorable."),
    ("If you had the chance to learn one additional branch of magic, like Divination or Ancient Runes, which would you choose and why?", "I would choose Ancient Runes."),
    ("Who is your favorite professor at Hogwarts when it comes to teaching Defense Against the Dark Arts?", "Professor Lupin is definitely my favorite."),
    ("If you could visit any magical location in the wizarding world that you haven't been to yet, where would you go?", "I would love to visit the Ministry of Magic and see the Department of Mysteries."),
    ("Which character from the wizarding world, besides your close friends, do you admire the most and why?", "Neville Longbottom is someone I greatly admire."),
    ("Among the various magical creatures you encountered, which one did you find the most challenging to deal with?", "The Hungarian Horntail dragon during the Triwizard Tournament was incredibly challenging."),
    ("If you could give one piece of advice to young witches and wizards starting their magical education, what would it be?", "I would advise them to believe in themselves and not be afraid to ask for help when needed.")
]

buffered_string = '\n'.join([f'{question}\n{answer}' for question, answer in buffered_history])
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
    # input_string = input("Enter a string: ")
    input_string = "Hi, what's your name?"
    print('Question')
    print(input_string)

    command = ["./build/bin/main", "-m", "chatglm-ggml.bin", "-p", input_string]
    welcome = "Welcome, Harry Potter, the greatest wizard from Hogwarts!"

    stdout, stderr = run_command_with_input(command, welcome=buffered_string+input_string)
    if stdout:
        print("Standard Output:")
        print(stdout)
    if stderr:
        print("Standard Error:")
        print(stderr)

if __name__ == "__main__":
    main()
