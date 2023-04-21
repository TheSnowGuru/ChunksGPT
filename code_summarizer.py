import re

def extract_comments_and_definitions(code_section):
    """Extract comments and function or class definitions from the code section."""
    lines = code_section.split("\n")
    summary_lines = []

    for line in lines:
        # Extract comments
        comment_match = re.search(r"#(.*)", line)
        if comment_match:
            summary_lines.append(comment_match.group(1).strip())

        # Extract function or class definitions
        definition_match = re.search(r"def (.+?)\(|class (.+?)\(", line)
        if definition_match:
            func_name = definition_match.group(1) or definition_match.group(2)
            summary_lines.append(f"Function/Class: {func_name.strip()}")

    return summary_lines


def generate_summary(code_section):
    """Generate a high-level summary of the code section."""
    summary_lines = extract_comments_and_definitions(code_section)
    return "\n".join(summary_lines)

