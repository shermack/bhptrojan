import json
import os


def run_module(module_name, module_args):
    # Dynamically import the module
    module = __import__(module_name)
    # Execute the run function of the module
    result = module.run(**module_args)
    print(f"Module {module_name} executed with result:\n{result}\n")


def main():
    config_file = "config/trojan_config.json"
    with open(config_file, "r") as f:
        config = json.load(f)

    for module_info in config["modules"]:
        module_name = module_info["name"]
        module_args = module_info["args"]
        run_module(module_name, module_args)


if __name__ == "__main__":
    main()