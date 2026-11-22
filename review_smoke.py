def normalize_task_title(title: str) -> str:
    words = title.strip().split()
    normalized = " ".join(words)
    return normalized
