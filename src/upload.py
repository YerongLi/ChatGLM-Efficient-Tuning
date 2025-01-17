import os
import torch
import signal
import platform

from utils import prepare_infer_args, auto_configure_device_map, load_pretrained
model_args, finetuning_args, generating_args = prepare_infer_args()
model, tokenizer = load_pretrained(model_args, finetuning_args)
model = model.to('cpu')
print(model.parameters().__next__().device)
model.push_to_hub("hp")