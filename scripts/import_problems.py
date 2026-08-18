from pathlib import Path

import yaml

from app.core.database import SessionLocal
from app.models.problems import Problem


def read_yaml(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def import_problem(folder: Path):
    
    metadata = read_yaml(folder / "structure.yaml")

    
    statement_markdown= (folder / "Problem.md").read_text(encoding="utf-8")

    
    inputs = sorted((folder / "inputs").glob("*.txt"))
    outputs = sorted((folder / "outputs").glob("*.txt"))

    if len(inputs) != len(outputs):
        raise ValueError(f"Inputs and outputs count do not match: {folder}")

    
    problem = Problem(
        slug=metadata["slug"],
        title=metadata["title"],
        statement_markdown=statement_markdown,
        points=metadata["difficulty"],
        time_limit_seconds=metadata["time_limit_seconds"],
        memory_limit_mb=metadata["memory_limit_mb"],
    )

    
    db = SessionLocal()

    try:
        db.add(problem)
        db.commit()
        db.refresh(problem)

        print(f"Imported: {problem.title}")

    finally:
        db.close()


if __name__ == "__main__":
    problem_folder = Path("problems") / "two-sum"

    import_problem(problem_folder)