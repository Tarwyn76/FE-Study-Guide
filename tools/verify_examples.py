# tools/verify_examples.py
# =====================================================================
# Independent worked-example numerical verification for the FE Study Guide.
#
# ALIGNED WITH technical_audit_all_layers_fixed_v7.py
#
# Default scope:
#   layer-1-substrate
#   layer-2-core
#   layer-3-tracks
#
# Layer 0 is excluded by default because the technical audit's release scope is
# Layers 1-3. Use --include-layer0 when you intentionally want orientation
# worked examples included.
#
# Numeric-candidate rule:
#   A worked example requires independent numeric verification only when:
#     1) its parsed problem contains a numeric token, AND
#     2) the technical-audit-style expects_numeric_result() heuristic says the
#        prompt asks for a numerical result.
#
# This intentionally excludes many examples that contain numbers but ask the
# reader to identify, classify, select, explain, formulate, or choose a model.
#
# Correct independent VERIFY schema:
#
#   <!-- VERIFY
#        id="WE-02-23-001"
#        expr="250*0.3048"
#        expected="76.2"
#        units="m"
#        atol="0.01"
#        rtol="1e-6"
#   -->
#
# expr= and expected= are separate.  The legacy result= self-comparison schema
# is rejected.
#
# Default outputs:
#   meta/example-verification-results.csv
#   meta/example-verification-summary.md
#
# Development mode:
#   missing VERIFY metadata -> REVIEW
#
# --strict:
#   missing VERIFY metadata -> FAIL
# =====================================================================

from __future__ import annotations

import argparse
import ast
import csv
import math
import operator
import re
import statistics
import yaml
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_CHAPTER_GLOBS = [
    "layer-1-substrate/*.md",
    "layer-2-core/**/*.md",
    "layer-3-tracks/**/*.md",
]

LAYER0_GLOB = "layer-0-orientation/*.md"

WORKED_HEADING_RE = re.compile(
    r"(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$"
)

VERIFY_COMMENT_RE = re.compile(
    r"<!--\s*VERIFY\b(?P<body>.*?)-->",
    re.IGNORECASE | re.DOTALL,
)

ATTR_RE = re.compile(
    r'(?P<key>[A-Za-z_][A-Za-z0-9_-]*)\s*=\s*"(?P<value>[^"]*)"'
)

# Exact numeric-token convention used by technical_audit_all_layers_fixed_v7.py.
NUM_TOKEN_RE = re.compile(
    r"(?<![\w.-])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?"
)

SOLUTION_MARKER_RE = re.compile(
    r"(?mi)^\s*\*\*(?:"
    r"Solution(?:\s*[—:\-]\s*[^*]+)?|"
    r"Approach(?:\s*[—:\-]\s*[^*]+)?|"
    r"Fast\s+approach(?:\s*[—:\-]\s*[^*]+)?|"
    r"Calculation(?:\s*[—:\-]\s*[^*]+)?|"
    r"Work(?:\s*[—:\-]\s*[^*]+)?|"
    r"Analysis(?:\s*[—:\-]\s*[^*]+)?|"
    r"Answer(?:\s*[—:\-]\s*[^*]+)?"
    r")\.?\*\*\s*"
)

PROMPT_MARKER_RE = re.compile(
    r"(?mi)^\s*\*\*(?:Problem|Given|Find|Question|Scenario|Task|Asked)\.?\*\*\s*"
)


SAFE_FUNCS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "log": math.log,
    "ln": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "erf": math.erf,
    "abs": abs,
    "pow": pow,
    "radians": math.radians,
    "degrees": math.degrees,
    "ceil": math.ceil,
    "floor": math.floor,
    "comb": lambda n, k: math.comb(int(n), int(k)),
    "factorial": lambda n: math.factorial(int(n)),
    "min": min,
    "max": max,
    "norm_ppf": statistics.NormalDist().inv_cdf,
}

SAFE_CONSTS = {"pi": math.pi, "e": math.e}

BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}

UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


@dataclass
class WorkedExample:
    chapter: str
    file: Path
    label: str
    block: str
    problem: str
    prompt_text: str


def strip_markdown(text: str) -> str:
    """Exact helper used by the technical audit's intent classifier."""
    s = re.sub(r"```.*?```", " ", text, flags=re.S)
    s = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", s)
    s = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"[*_>#|]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def has_numeric_token(text: str) -> bool:
    return bool(NUM_TOKEN_RE.search(text))


def expects_numeric_result(text: str) -> bool:
    """
    Match technical_audit_all_layers_fixed_v7.py.

    Numeric context alone is insufficient: classification, model-selection,
    hypothesis-translation, and explanation questions routinely contain numbers
    but correctly return categorical or symbolic answers.
    """
    s = strip_markdown(text).lower()

    conceptual = re.search(
        r"\b(?:classify|identify|explain|interpret|select|choose|describe|state which|"
        r"which (?:model|design|distribution|procedure|method|alternative)|"
        r"test whether|write|formulate|translate|why|whether)\b",
        s,
    )
    quantitative = re.search(
        r"\b(?:calculate|compute|evaluate|find|determine|solve|estimate|convert)\b",
        s,
    )

    if quantitative:
        categorical_object = re.search(
            r"\b(?:find|determine|choose|select)\b.{0,80}"
            r"\b(?:model|design|distribution|procedure|method|classification|"
            r"hypotheses?|decision structure|alternative|boolean|condition|"
            r"pseudocode|logic|flowchart|algorithm|code)\b",
            s,
        )
        if categorical_object:
            return False
        return True

    if conceptual:
        return False

    if re.search(r"\b(?:what is|how many|how much)\b", s):
        return True

    return False


def safe_eval(expression: str) -> float:
    """Evaluate a restricted numeric expression without eval()."""
    tree = ast.parse(expression, mode="eval")

    def walk(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.Name):
            if node.id in SAFE_CONSTS:
                return float(SAFE_CONSTS[node.id])
            raise ValueError(f"unknown name '{node.id}'")
        if isinstance(node, ast.BinOp) and type(node.op) in BIN_OPS:
            return float(BIN_OPS[type(node.op)](walk(node.left), walk(node.right)))
        if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPS:
            return float(UNARY_OPS[type(node.op)](walk(node.operand)))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            fn = SAFE_FUNCS.get(node.func.id)
            if fn is None:
                raise ValueError(f"function '{node.func.id}' is not allowed")
            return float(fn(*(walk(arg) for arg in node.args)))
        raise ValueError(f"unsupported expression element: {type(node).__name__}")

    value = walk(tree)
    if not math.isfinite(value):
        raise ValueError("expression produced a non-finite value")
    return value


def chapter_id(path: Path, text: str) -> str:
    m = re.search(r'(?m)^chapter:\s*["\']?([^"\'\s]+)', text[:1500])
    if m:
        return m.group(1)
    m = re.match(r"^(\d{2}-\d{2})-", path.name)
    return m.group(1) if m else path.stem


def iter_chapter_files(include_layer0: bool):
    patterns = list(DEFAULT_CHAPTER_GLOBS)
    if include_layer0:
        patterns.insert(0, LAYER0_GLOB)

    seen: set[Path] = set()
    for pattern in patterns:
        for path in sorted(BASE_DIR.glob(pattern)):
            if path.is_file() and path not in seen:
                seen.add(path)
                yield path


def has_substantive_unlabeled_solution(block: str) -> bool:
    """
    Kept for parser alignment with the technical audit.  The verifier does not
    need the parsed solution itself, but this preserves the same problem-block
    interpretation for chapters with implicit solution structure.
    """
    if not block or len(strip_markdown(block).split()) < 18:
        return False

    # Conservative signals copied in spirit from the technical audit:
    # equations plus substantive explanatory text, or known analysis labels.
    if re.search(
        r"(?mi)^\s*\*\*(?:Hypotheses|Statistic|Critical value|Decision|Conclusion|"
        r"Substitution|Result|Check|Interpretation)\b",
        block,
    ):
        return True
    if len(re.findall(r"\$\$.*?\$\$|\\\[.*?\\\]", block, flags=re.S)) >= 1:
        return True
    return False


def extract_examples(path: Path) -> list[WorkedExample]:
    """
    Parser aligned to technical_audit_all_layers_fixed_v7.py:
      - identical Worked Example heading regex
      - identical solution marker family
      - identical prompt marker family
      - identical H2 stopping rule
    """
    text = path.read_text(encoding="utf-8-sig")
    cid = chapter_id(path, text)
    matches = list(WORKED_HEADING_RE.finditer(text))
    examples: list[WorkedExample] = []

    for i, match in enumerate(matches):
        start_block = match.end()
        end_block = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        next_h2 = re.search(r"(?m)^##\s+", text[start_block:end_block])
        if next_h2:
            end_block = start_block + next_h2.start()

        block = text[start_block:end_block].strip()
        label = (match.group(1) or str(i + 1)).strip()

        sm = SOLUTION_MARKER_RE.search(block)
        pre_solution = block[:sm.start()].strip() if sm else block
        prompt_markers = list(PROMPT_MARKER_RE.finditer(pre_solution))

        if prompt_markers:
            problem = PROMPT_MARKER_RE.sub("", pre_solution).strip()
        elif sm:
            problem = pre_solution
        elif block:
            problem = block
        else:
            problem = ""

        examples.append(
            WorkedExample(
                chapter=cid,
                file=path,
                label=label,
                block=block,
                problem=problem,
                prompt_text=pre_solution,
            )
        )

    return examples


def is_numeric_candidate(ex: WorkedExample) -> bool:
    """
    Exact release-intent rule used by the technical audit for numeric-result
    checks: numeric data must be present AND the prompt must ask for a numeric
    result.
    """
    if not has_numeric_token(ex.problem):
        return False
    intent_text = f"{ex.label} {ex.prompt_text or ex.problem}"
    return expects_numeric_result(intent_text)


def parse_verify_tags(block: str) -> list[dict[str, str]]:
    tags: list[dict[str, str]] = []
    for match in VERIFY_COMMENT_RE.finditer(block):
        attrs = {
            m.group("key"): m.group("value")
            for m in ATTR_RE.finditer(match.group("body"))
        }
        tags.append(attrs)
    return tags


def check_tag(
    attrs: dict[str, str],
    ex: WorkedExample,
    seen_ids: set[str],
) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    record: dict[str, Any] = {
        "chapter": ex.chapter,
        "example": ex.label,
        "verify_id": attrs.get("id", ""),
        "expr": attrs.get("expr", ""),
        "expected": attrs.get("expected", ""),
        "units": attrs.get("units", ""),
        "status": "ok",
        "detail": "",
    }

    if "result" in attrs and "expr" not in attrs:
        errors.append(
            f"{ex.chapter} Worked Example {ex.label}: legacy VERIFY tag uses "
            "result= without expr=/expected=; it cannot independently verify."
        )

    required = ["id", "expr", "expected", "units"]
    missing = [key for key in required if key not in attrs]
    if missing:
        errors.append(
            f"{ex.chapter} Worked Example {ex.label}: VERIFY tag missing "
            f"{', '.join(missing)}"
        )
        record["status"] = "error"
        record["detail"] = "missing required attributes"
        return errors, record

    vid = attrs["id"]
    if vid in seen_ids:
        errors.append(
            f"{ex.chapter} Worked Example {ex.label}: duplicate VERIFY id '{vid}'"
        )
    seen_ids.add(vid)

    try:
        computed = safe_eval(attrs["expr"])
    except Exception as exc:
        errors.append(
            f"{ex.chapter} Worked Example {ex.label} [{vid}]: "
            f"cannot evaluate expr='{attrs['expr']}': {exc}"
        )
        record["status"] = "error"
        record["detail"] = str(exc)
        return errors, record

    try:
        expected = float(attrs["expected"].replace(",", ""))
    except Exception:
        errors.append(
            f"{ex.chapter} Worked Example {ex.label} [{vid}]: "
            f"expected='{attrs['expected']}' must be a numeric literal"
        )
        record["status"] = "error"
        record["detail"] = "invalid expected"
        return errors, record

    try:
        atol = float(attrs.get("atol", attrs.get("tol", "1e-9")))
        rtol = float(attrs.get("rtol", "1e-9"))
    except Exception:
        errors.append(
            f"{ex.chapter} Worked Example {ex.label} [{vid}]: invalid atol/rtol"
        )
        record["status"] = "error"
        record["detail"] = "invalid tolerance"
        return errors, record

    allowed = atol + rtol * abs(expected)
    diff = abs(computed - expected)

    record["computed"] = computed
    record["difference"] = diff
    record["allowed"] = allowed

    if diff > allowed:
        errors.append(
            f"{ex.chapter} Worked Example {ex.label} [{vid}]: "
            f"computed {computed:.12g} {attrs['units']} but expected "
            f"{expected:.12g} {attrs['units']}; diff={diff:.6g}, "
            f"allowed={allowed:.6g}"
        )
        record["status"] = "fail"
        record["detail"] = "numeric mismatch"

    return errors, record



def load_exclusions(path: Path) -> dict[tuple[str, str], str]:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    rows = data.get("exclusions", [])
    if not isinstance(rows, list):
        raise ValueError("exclusions must be a list")
    out: dict[tuple[str, str], str] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("each exclusion must be a mapping")
        chapter = str(row.get("chapter", "")).strip()
        example = str(row.get("example", "")).strip()
        reason = str(row.get("reason", "")).strip()
        if not chapter or not example or not reason:
            raise ValueError("each exclusion needs chapter, example, and reason")
        key = (chapter, example)
        if key in out:
            raise ValueError(f"duplicate exclusion: {chapter} / {example}")
        out[key] = reason
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail numeric candidates that lack independent VERIFY metadata.",
    )
    parser.add_argument(
        "--include-layer0",
        action="store_true",
        help="Also scan layer-0-orientation. Default scope matches the technical audit: Layers 1-3.",
    )
    parser.add_argument(
        "--csv",
        default="meta/example-verification-results.csv",
        help=(
            "CSV path for verification coverage/results "
            "(default: meta/example-verification-results.csv)."
        ),
    )
    parser.add_argument(
        "--summary",
        default="meta/example-verification-summary.md",
        help=(
            "Markdown summary path "
            "(default: meta/example-verification-summary.md)."
        ),
    )
    parser.add_argument(
        "--exclusions",
        default="meta/example-verification-exclusions.yaml",
        help=(
            "Curated exclusions for heuristic numeric-candidate false positives "
            "(default: meta/example-verification-exclusions.yaml)."
        ),
    )
    args = parser.parse_args()

    exclusions_path = Path(args.exclusions)
    if not exclusions_path.is_absolute():
        exclusions_path = BASE_DIR / exclusions_path
    try:
        exclusions = load_exclusions(exclusions_path)
    except Exception as exc:
        print(f"ERROR  Could not load verification exclusions: {exc}")
        return 2

    examples: list[WorkedExample] = []
    for chapter_file in iter_chapter_files(args.include_layer0):
        examples.extend(extract_examples(chapter_file))

    if not examples:
        print("ERROR  No Worked Example blocks found in the selected scope.")
        return 2

    errors: list[str] = []
    reviews: list[str] = []
    rows: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    candidate_count = 0
    tagged_candidate_count = 0
    tag_count = 0
    noncandidate_tag_count = 0
    excluded_count = 0
    matched_exclusions: set[tuple[str, str]] = set()

    for ex in examples:
        candidate = is_numeric_candidate(ex)
        tags = parse_verify_tags(ex.block)
        exclusion_reason = exclusions.get((ex.chapter, ex.label), "")
        if exclusion_reason:
            matched_exclusions.add((ex.chapter, ex.label))

        if candidate:
            candidate_count += 1

        # Any explicit tag is always validated, even if the current heuristic
        # does not classify the example as a required numeric candidate.
        if tags:
            if candidate:
                tagged_candidate_count += 1
            else:
                noncandidate_tag_count += len(tags)

            tag_count += len(tags)
            for tag in tags:
                tag_errors, row = check_tag(tag, ex, seen_ids)
                errors.extend(tag_errors)
                row["numeric_candidate"] = candidate
                rows.append(row)

        if candidate and not tags:
            if exclusion_reason:
                excluded_count += 1
                rows.append({
                    "chapter": ex.chapter,
                    "example": ex.label,
                    "numeric_candidate": True,
                    "verify_id": "",
                    "expr": "",
                    "expected": "",
                    "units": "",
                    "status": "excluded",
                    "detail": exclusion_reason,
                })
            else:
                msg = (
                    f"{ex.chapter} Worked Example {ex.label}: "
                    "numeric-result example has no independent VERIFY tag"
                )
                if args.strict:
                    errors.append(msg)
                    status = "missing-tag-error"
                else:
                    reviews.append(msg)
                    status = "missing-tag-review"

                rows.append({
                    "chapter": ex.chapter,
                    "example": ex.label,
                    "numeric_candidate": True,
                    "verify_id": "",
                    "expr": "",
                    "expected": "",
                    "units": "",
                    "status": status,
                    "detail": "numeric-result example lacks independent VERIFY metadata",
                })

    stale_exclusions = sorted(set(exclusions) - matched_exclusions)
    for chapter, example in stale_exclusions:
        errors.append(
            f"verification exclusion does not match any example in selected scope: "
            f"{chapter} / {example}"
        )

    csv_path = Path(args.csv)
    if not csv_path.is_absolute():
        csv_path = BASE_DIR / csv_path
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "chapter", "example", "numeric_candidate", "verify_id", "expr",
        "expected", "units", "status", "detail", "computed", "difference",
        "allowed",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})

    summary_path = Path(args.summary)
    if not summary_path.is_absolute():
        summary_path = BASE_DIR / summary_path
    summary_path.parent.mkdir(parents=True, exist_ok=True)

    scope = "Layers 0-3" if args.include_layer0 else "Layers 1-3"
    summary_lines = [
        "# Worked Example Verification Summary",
        "",
        f"- Scope: **{scope}**",
        f"- Worked examples found: **{len(examples)}**",
        f"- Numeric-result candidates: **{candidate_count}**",
        f"- Tagged numeric candidates: **{tagged_candidate_count}**",
        f"- Independent VERIFY checks: **{tag_count}**",
        f"- VERIFY tags on non-required examples: **{noncandidate_tag_count}**",
        f"- Curated numeric-candidate exclusions: **{excluded_count}**",
        f"- Failures: **{len(errors)}**",
        f"- Coverage reviews: **{len(reviews)}**",
        "",
        "## Classification rule",
        "",
        "The numeric-candidate rule is aligned to `technical_audit_all_layers_fixed_v7.py`: "
        "the parsed problem must contain a numeric token and the prompt must ask for a numeric result. "
        "Classification/model-selection/explanation/symbolic tasks that merely contain numbers are not verification-required by this heuristic.",
        "",
        "## Interpretation",
        "",
        "A coverage review means the example was classified as requiring a numeric result but does not yet have independent machine-readable verification metadata. It is not, by itself, evidence that the worked example is wrong.",
        "",
    ]

    if errors:
        summary_lines += ["## Failures", ""]
        summary_lines.extend(f"- {msg}" for msg in errors)
        summary_lines.append("")

    if reviews:
        summary_lines += ["## Coverage reviews", ""]
        summary_lines.extend(f"- {msg}" for msg in reviews)
        summary_lines.append("")

    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")

    for msg in errors[:100]:
        print(f"FAIL  {msg}")
    if len(errors) > 100:
        print(f"FAIL  ... {len(errors) - 100} additional failures omitted.")

    for msg in reviews[:20]:
        print(f"REVIEW  {msg}")
    if len(reviews) > 20:
        print(f"REVIEW  ... {len(reviews) - 20} additional coverage reviews omitted.")

    print()

    if errors:
        status = "FAIL"
    elif reviews:
        status = "PASS WITH REVIEW REQUIRED"
    else:
        status = "PASS"

    print(
        f"{status}  "
        f"{len(examples)} worked examples; "
        f"{candidate_count} numeric-result candidates; "
        f"{tagged_candidate_count} tagged candidates; "
        f"{tag_count} independent VERIFY checks; "
        f"{excluded_count} curated exclusions; "
        f"{len(errors)} failures; "
        f"{len(reviews)} coverage reviews."
    )

    try:
        csv_display = csv_path.relative_to(BASE_DIR)
    except ValueError:
        csv_display = csv_path
    try:
        summary_display = summary_path.relative_to(BASE_DIR)
    except ValueError:
        summary_display = summary_path

    print(f"OUTPUT  {csv_display}")
    print(f"OUTPUT  {summary_display}")

    if reviews and not args.strict:
        print(
            "INFO  Use --strict for the release gate. Strict mode requires "
            "independent VERIFY metadata on every numeric-result candidate."
        )

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
