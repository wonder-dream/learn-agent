from src.schemas import Severity, Category, ReviewComment, ReviewRequest
from pydantic import ValidationError
import pytest


@pytest.fixture
def valid_comment():
    return ReviewComment(
        file_path="src/main.py",
        line_number=42,
        severity=Severity.WARNING,
        category=Category.NAMING,
        message="变量名应使用 snake_case",
    )


@pytest.fixture
def sample_request():
    return ReviewRequest(
        file_path="src/main.py",
        file_content="print(hello)",
        language="python",
        review_level="high",
    )


def test_file_path(valid_comment):
    assert valid_comment.file_path == "src/main.py"


def test_line_number(valid_comment):
    assert valid_comment.line_number == 42


def test_severity(valid_comment):
    assert valid_comment.severity == Severity.WARNING


def test_message(valid_comment):
    assert valid_comment.message == "变量名应使用 snake_case"


def test_line_number_zero():
    with pytest.raises(ValidationError):
        return ReviewComment(
            file_path="src/main.py",
            line_number=0,
            severity=Severity.WARNING,
            category=Category.NAMING,
            message="变量名应使用 snake_case",
        )


def test_empty_message():
    with pytest.raises(ValidationError):
        return ReviewComment(
            file_path="src/main.py",
            line_number=42,
            severity=Severity.WARNING,
            category=Category.NAMING,
            message="",
        )


def test_invalid_severity():
    with pytest.raises(ValidationError):
        return ReviewComment(
            file_path="src/main.py",
            line_number=42,
            severity="Severity.WARNING",
            category=Category.NAMING,
            message="变量名应使用 snake_case",
        )


@pytest.mark.parametrize("lang", ["python", "go", "java", "rust", "typescript"])
def test_language(lang):
    request = ReviewRequest(file_path=f"x.{lang}", file_content="", language=lang)
    assert request.language == lang
