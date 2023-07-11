from huggingface_hub import HfApi

# Define the model and repository information
model_name = "ggml-model-q4_0"
repo_url = "umiuni/lhp"

# Load the model file
model_path = "ggml-model-q4_0.bin"

try:
    # Connect to the existing repository
    api = HfApi()

    # Upload the model file to the existing repository
    api.upload_file(
        path_or_fileobj=model_path,
        path_in_repo=model_name + ".bin",
        repo_id=repo_url,
        repo_type="model",
        use_auth_token="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"
    )

    print("Model uploaded successfully!")
except Exception as e:
    print(f"Error occurred: {e}")

