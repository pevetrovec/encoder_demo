import argparse
from ciphers import CIPHERS


def run_cli():
    # First parse just the cipher name, mode, and text (known args)
    base_parser = argparse.ArgumentParser(add_help=False)
    base_parser.add_argument("cipher", choices=CIPHERS.keys())
    base_parser.add_argument("mode", choices=["encode", "decode"])
    base_parser.add_argument("text")

    # Parse known args first to know which cipher to load
    args, remaining_argv = base_parser.parse_known_args()

    cipher = CIPHERS[args.cipher]
    

    # Now build full parser including cipher-specific params
    parser = argparse.ArgumentParser(
        description=f"Use the {args.cipher} cipher",
        parents=[base_parser]
    )

    for param, default in cipher.parameters.items():
        param_type = type(default)
        # convert param name to CLI flag format, e.g. 'shift' → '--shift'
        parser.add_argument(f"--{param}", type=param_type, default=default)

    # Parse all args now
    full_args = parser.parse_args()

    # Extract params dict dynamically from parsed args
    params = {param: getattr(full_args, param) for param in cipher.parameters.keys()}

    func = getattr(cipher, args.mode)
    output = func(args.text, **params)
    print(output)