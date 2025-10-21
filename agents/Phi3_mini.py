import argparse
import sys
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch


def get_device_map(use_cuda: bool):
    if use_cuda and torch.cuda.is_available():
        return "auto"
    # force CPU
    return None


def build_pipeline(model_name: str, device_map=None, dtype=None, max_new_tokens=200, temperature=0.7):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

    # load model with safe defaults
    model_kwargs = {"trust_remote_code": True}
    if device_map is not None:
        model_kwargs["device_map"] = device_map
    if dtype is not None:
        model_kwargs["torch_dtype"] = dtype

    model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
        return_full_text=False,
    )

    return pipe


def main():
    parser = argparse.ArgumentParser(description="Lightweight Phi-3 mini conversational loop")
    parser.add_argument("--model", default="microsoft/Phi-3-mini-4k-instruct", help="Model name or path")
    parser.add_argument("--cpu", action="store_true", help="Force CPU (disable CUDA)")
    parser.add_argument("--max-new-tokens", type=int, default=200)
    parser.add_argument("--temperature", type=float, default=0.7)
    args = parser.parse_args()

    use_cuda = not args.cpu and torch.cuda.is_available()
    device_map = get_device_map(use_cuda)
    dtype = torch.float16 if use_cuda else None

    try:
        pipe = build_pipeline(
            args.model, device_map=device_map, dtype=dtype, max_new_tokens=args.max_new_tokens, temperature=args.temperature
        )
    except Exception as e:
        print(f"Failed to load model '{args.model}': {e}")
        sys.exit(1)

    print("🤙 SurfSense is ready! Type 'quit' or Ctrl-D to exit.")

    chat_template = "<|user|>\n{user_input}<|end|>\n<|assistant|>\n"

    try:
        while True:
            try:
                user_input = input("You: ")
            except EOFError:
                print()
                break

            if user_input.strip().lower() in ["quit", "exit"]:
                break

            formatted_input = chat_template.format(user_input=user_input)
            try:
                out = pipe(formatted_input)
                # pipeline returns list of dicts with 'generated_text' when return_full_text=False
                if isinstance(out, list) and len(out) > 0 and "generated_text" in out[0]:
                    resp = out[0]["generated_text"]
                else:
                    # fallback: str()
                    resp = str(out)

                print("Bot:", resp.strip())
            except Exception as e:
                print(f"Generation error: {e}")
    except KeyboardInterrupt:
        print("\nExiting.")


if __name__ == "__main__":
    main()