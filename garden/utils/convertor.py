import re

def camel_case_to_snake_case(input_str: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', input_str).lower()
