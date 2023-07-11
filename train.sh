python src/train_sft.py \
    --do_train \
    --checkpoint_dir 'harry_potter/checkpoint-1400' \
    --dataset harry_potter \
    --finetuning_type lora \
    --output_dir harry_potter \
    --per_device_train_batch_size 10 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 50 \
    --learning_rate 5e-5 \
    --num_train_epochs 10.0 \
    --fp16 \
    --quantization_bit 4

