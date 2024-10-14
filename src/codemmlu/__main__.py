import os
import argparse
import pkg_resources

from codemmlu.task_utils import ALL_TASK

def get_args():
    parser = argparse.ArgumentParser(description=f"{20*'='} CodeMMLU {20*'='}")
    
    parser.add_argument("-V", "--version", action="version", help="Get version",
                        version=pkg_resources.get_distribution("codemmlu").version)
    
    # Data args
    parser.add_argument("--subset", default="all", type=str,
                        help='Select evaluate subset')
    parser.add_argument("--batch_size", default=16, type=int)
    parser.add_argument("--instruction_prefix", default="", type=str)
    parser.add_argument("--assistant_prefix", default="", type=str)
    parser.add_argument("--output_dir", default="./output", type=str,
                        help='Save generation and result path')
    
    # Generation args
    parser.add_argument("--model_name", type=str,
                        help='Local path or Huggingface Hub link to load model')
    parser.add_argument("--peft_model", default=None, type=str,
                        help='Lora config')
    parser.add_argument("--backend", default="hf", type=str,
                        help="LLM generation backend (default: hf)")
    parser.add_argument("--max_new_tokens", default=128, type=int,
                        help='Number of max new tokens')
    parser.add_argument("--temperature", default=0.0, type=float)
    parser.add_argument("--cache_dir", default=None, type=str,
                        help='Cache for save model download checkpoint and dataset')
    
    args = parser.parse_args()
    
    if not args.cache_dir:
        TRANSFORMER_CACHE = os.getenv("TRANSFORMER_CACHE")
        HF_HOME = os.getenv("HF_HOME")
        if TRANSFORMER_CACHE:
            args.cache_dir = TRANSFORMER_CACHE
        else:
            args.cache_dir = HF_HOME
    
    assert args.subset in ALL_TASK, f"Invalid subset name, expect {ALL_TASK}, but got {args.subset}"

    return args, parser


def main():
    args, parsre = get_args()
    if args.task:
        generate(args=args)
    else:
        parsre.print_help()
    

def generate(args):
    from codemmlu import Evaluator

    evaluator = Evaluator(
        model_name=args.model_name,
        peft_model=args.peft_model,
        backend=args.backend,
        batch_size=args.batch_size,
        cache_dir=args.cache_dir,
        output_dir=args.output_dir,
        trust_remote_code=args.trust_remote_code,
        instruction_prefix=args.instruction_prefix,
        assistant_prefix=args.assistant_prefix
    )

    evaluator.generate(
        temperature=args.temperature,
        max_new_tokens=args.max_new_tokens,
    )
    
    print("======= Finish generated =======")


if __name__ == '__main__':
    main()