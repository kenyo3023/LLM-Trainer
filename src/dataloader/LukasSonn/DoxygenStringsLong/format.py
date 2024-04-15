from dataclasses import dataclass
from typing import Literal

template_for_chatml = '''
<|im_start|>system
{question}<|im_end|>

<|im_start|>user
{context}<|im_end|>

<|im_start|>assistant
{answer}<|im_end|>
'''.strip()


template_for_llama2 = '''
[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
 
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<</SYS>>
 
Following <code> to generate corresponding doxygen.
 
<code>
 
{context}
 
[/INST] {answer}
'''.strip()


@dataclass
class ContextTemplate:
    chatml :str = template_for_chatml
    llama2 :str = template_for_llama2


# def format_context(row, template:Literal[tuple(ContextTemplate.__dataclass_fields__.keys())]='chatml'):
def apply_context(row, template='chatml'):

    template = getattr(ContextTemplate, template)

    context = template.format(**row)

    return {"context": context}