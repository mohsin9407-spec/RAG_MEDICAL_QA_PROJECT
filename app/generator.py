# Placeholder generator that creates a conservative answer using retrieved passages and a prompt template.
# Replace this with an LLM call (OpenAI, local Llama, etc.) for production.
from pathlib import Path

PROMPT_TMPL = Path(__file__).resolve().parents[1] / 'prompts' / 'prompt_template.md'
tmpl = PROMPT_TMPL.read_text()

def generate_answer(question, retrieved_passages):
    retrieved = ''
    for i, p in enumerate(retrieved_passages, start=1):
        retrieved += f'[doc_{i}] ' + p + '\n\n'
    prompt = tmpl.replace('{question}', question).replace('{retrieved}', retrieved)
    # Simple heuristic: if passages contain keywords from question, return a short summary.
    # This is only a placeholder.
    if len(retrieved_passages) == 0:
        return "I don't know — the provided documents do not contain enough information."
    # naive summarization: return first sentences from retrieved_passages
    answer_parts = []
    for p in retrieved_passages:
        s = p.split('.')[:2]  # first two sentence fragments
        answer_parts.append('.'.join(s).strip() + '.')
    return ' '.join(answer_parts)        