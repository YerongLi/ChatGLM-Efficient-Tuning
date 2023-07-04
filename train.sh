python src/train_sft.py \
    --do_train \
    --dataset elon_musk \
    --finetuning_type lora \
    --output_dir elon_musk \
    --per_device_train_batch_size 8 \
    --gradient_accumulation_steps 2 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 50 \
    --learning_rate 5e-5 \
    --num_train_epochs 3.0 \
    --fp16 \
    --quantization_bit 4

