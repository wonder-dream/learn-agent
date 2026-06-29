import pytest
import httpx
from .schemas_test import sample_request


@pytest.fixture
async def client():
    async with httpx.AsyncClient as c:
        yield c


@pytest.fixture
def api_url():
    return "http://localhost:8080"


@pytest.fixture
def review_payload(sample_request):
    return sample_request.model_dump()


def test_payload(review_payload, sample_request):
    assert sample_request.model_dump() == review_payload
