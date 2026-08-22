from pathlib import Path
import sys
import yaml
from sqlalchemy import select
from sqlalchemy.orm import Session

ROOT_DIR=Path(__file__).resolve().parents[1]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0,str(ROOT_DIR))

from app.core.database import SessionLocal
from app.models.problems import Problem,DefaultCodes

PROBLEMS_DIR=ROOT_DIR/"problems"

LANGUAGES={
    "python":"function.py",
    "c++":"function.cpp",
    "javascript":"function.js"
}

def read_yaml(path):
    with path.open("r",encoding="utf-8") as file:
        return yaml.safe_load(file)

def import_problem(db:Session,folder:Path,existing_slugs:set):
    metadata=read_yaml(folder/"structure.yaml")
    slug=metadata["slug"]

    if slug in existing_slugs:
        print(f"Skipped: {slug}")
        return False

    statement=(folder/"problem.md").read_text(encoding="utf-8")

    inputs=sorted((folder/"tests"/"inputs").glob("*.txt"))
    outputs=sorted((folder/"tests"/"outputs").glob("*.txt"))

    if len(inputs)!=len(outputs):
        raise ValueError(f"Input/output count mismatch: {folder}")

    problem=Problem(
        slug=slug,
        title=metadata["title"],
        statement_markdown=statement,
        points=metadata["difficulty"],
        time_limit_seconds=metadata["time_limit_seconds"],
        memory_limit_mb=metadata["memory_limit_mb"]
    )

    db.add(problem)
    db.flush()

    for language,file_name in LANGUAGES.items():
        starter_code=(folder/"boilerplate"/file_name).read_text(encoding="utf-8")
        full_boilerplate=(folder/"boilerplate-full"/file_name).read_text(encoding="utf-8")

        db.add(
            DefaultCodes(
                problem_id=problem.id,
                language=language,
                starter_code=starter_code,
                full_boilerplate=full_boilerplate
            )
        )

    existing_slugs.add(slug)

    print(f"Imported: {problem.title}")
    return True

def import_all_problems(db:Session):
    existing_slugs=set(db.scalars(select(Problem.slug)).all())

    try:
        for folder in sorted(PROBLEMS_DIR.iterdir()):
            if folder.is_dir():
                import_problem(db,folder,existing_slugs)

        db.commit()
        print("Import completed!")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

if __name__=="__main__":
    import_all_problems(SessionLocal())