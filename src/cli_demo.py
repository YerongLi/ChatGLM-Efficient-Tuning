# coding=utf-8
# Implements stream chat in command line for ChatGLM fine-tuned with PEFT.
# This code is largely borrowed from https://github.com/THUDM/ChatGLM-6B/blob/main/cli_demo.py
# Usage: python cli_demo.py --checkpoint_dir path_to_checkpoint [--quantization_bit 4]


import os
import torch
import random
import signal
import platform

from utils import prepare_infer_args, auto_configure_device_map, load_pretrained


os_name = platform.system()
clear_command = "cls" if os_name == "Windows" else "clear"
stop_stream = False
welcome = "Welcome, Harry Potter, the greatest wizard from Hogwarts!"


def build_prompt(history):
    prompt = welcome
    for query, response in history:
        if (query, response) in buffered_history: continue
        prompt += f"\n\n {query}"
        prompt += f"\n\n: Harry : {response}"
    return prompt


def signal_handler(signal, frame):
    global stop_stream
    stop_stream = True

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

def truncate_history(history):
    total_words = 0
    selected_history = []

    for i in range(len(history)-1, -1, -1):
        question, answer = history[i]
        words = len(question.split()) + len(answer.split())

        if total_words + words <= 1800:
            selected_history.append((question, answer))
            total_words += words
        else:
            break

    return selected_history

def main():

    global stop_stream
    model_args, finetuning_args, generating_args = prepare_infer_args()
    model, tokenizer = load_pretrained(model_args, finetuning_args)

    if torch.cuda.device_count() > 1:
        from accelerate import dispatch_model
        device_map = auto_configure_device_map(torch.cuda.device_count(), use_v2=model_args.use_v2)
        model = dispatch_model(model, device_map)
    else:
        model = model.cuda()

    model.eval()


    history = buffered_history.copy()
    print(welcome)
    while True:
        try:
            query = input("\nInput: ")
        except UnicodeDecodeError:
            print("Detected decoding error at the inputs, please set the terminal encoding to utf-8.")
            continue
        except Exception:
            raise

        if query.strip() == "stop":
            break
        if query.strip() == "clear":
            history = buffered_history.copy()
            os.system(clear_command)
            print(welcome)
            continue
        history = truncate_history(history)
        count = 0
        print(type(model))
        for _, history in model.stream_chat(tokenizer, query, history=history, **generating_args.to_dict()):
            if stop_stream:
                stop_stream = False
                break
            else:
                count += 1
                if count % 10 == 0:
                    os.system(clear_command)
                    print(build_prompt(history), flush=True)
                    signal.signal(signal.SIGINT, signal_handler)
        os.system(clear_command)
        print(build_prompt(history), flush=True)


if __name__ == "__main__":
    main()
