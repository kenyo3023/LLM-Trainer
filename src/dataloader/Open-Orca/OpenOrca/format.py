


template = '''
<|im_start|>system
{system}<|im_end|>

<|im_start|>user
{question}<|im_end|>

<|im_start|>assistant
{answer}<|im_end|>
'''.strip()


def format_context(row):

    context = template.format(
        system   = row["system_prompt"],
        question = row["question"],
        answer   = row["response"],
    )

    return {"context": context}