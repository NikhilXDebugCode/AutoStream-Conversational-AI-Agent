from pathlib import Path

DATA_FILE = Path("data/knowledge.md")


def load_content() -> str:
    if not DATA_FILE.exists():
        return ""
    return DATA_FILE.read_text(encoding="utf-8")


def get_section(content: str, header: str) -> str:
    lines = content.splitlines()
    section = []
    capture = False

    for line in lines:
        if line.strip().lower() == header.lower():
            capture = True
            section.append(line)
            continue

        if capture:
            if line.startswith("## "):
                break
            section.append(line)

    return "\n".join(section).strip()


def rag_answer(query: str) -> str:
    content = load_content()
    q = query.lower()

    if any(w in q for w in ["price", "pricing", "plan", "cost", "basic", "pro"]):
        return get_section(content, "## Pricing & Plans")

    if any(w in q for w in ["feature", "features", "ai", "edit", "editing"]):
        return get_section(content, "## Features")

    if any(w in q for w in ["youtube", "instagram", "platform"]):
        return get_section(content, "## Supported Platforms")

    if any(w in q for w in ["refund", "policy", "support"]):
        return get_section(content, "## Company Policies")

    if any(w in q for w in ["secure", "security", "safe"]):
        return get_section(content, "## Security & Reliability")

    if any(w in q for w in ["account", "subscription", "cancel", "billing"]):
        return get_section(content, "## Account & Subscription")

    if any(w in q for w in ["use", "access", "browser", "cloud"]):
        return get_section(content, "## Usage & Access")

    if any(w in q for w in ["what is", "about", "autostream"]):
        return get_section(content, "## AutoStream Overview")

    return "No relevant information found."
