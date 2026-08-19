from pathlib import Path

import yaml
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.problems import Problem

PROBLEMS_DIR = Path("problems")


def read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def import_problem(db: Session, folder: Path, existing_slugs: set) -> bool:
    metadata = read_yaml(folder / "structure.yaml")
    slug = metadata["slug"]

    if slug in existing_slugs:
        print(f"Skipped: {slug} (already exists)")
        return False

    statement = (folder / "Problem.md").read_text(encoding="utf-8")

    inputs = sorted((folder / "inputs").glob("*.txt"))
    outputs = sorted((folder / "outputs").glob("*.txt"))

    if len(inputs) != len(outputs):
        raise ValueError(f"Input/output count mismatch: {folder}")

    problem = Problem(
        slug=slug,
        title=metadata["title"],
        statement_markdown=statement,
        points=metadata["difficulty"],
        time_limit_seconds=metadata["time_limit_seconds"],
        memory_limit_mb=metadata["memory_limit_mb"],
    )

    db.add(problem)
    existing_slugs.add(slug)

    print(f"Imported: {problem.title}")
    return True


def import_all_problems():
    if not PROBLEMS_DIR.exists():
        raise FileNotFoundError(f"Problems directory not found: {PROBLEMS_DIR}")

    imported = 0
    skipped = 0

    with SessionLocal() as db:
        try:
            existing_slugs = set(
                db.scalars(select(Problem.slug)).all()
            )

            for folder in sorted(PROBLEMS_DIR.iterdir()):
                if not folder.is_dir():
                    continue

                if import_problem(db, folder, existing_slugs):
                    imported += 1
                else:
                    skipped += 1

            db.commit()

        except Exception:
            db.rollback()
            raise

    print("\nImport completed!")
    print(f"Imported: {imported}")
    print(f"Skipped: {skipped}")


if __name__ == "__main__":
    import_all_problems()