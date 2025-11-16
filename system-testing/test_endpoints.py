#-----------------------------------------------------------

import requests

import pytest

#-----------------------------------------------------------

# Define once (each test below will use this url)
API_ROOT = "http://localhost:8888"

#-----------------------------------------------------------
# /sum endpoint
# -----------------------------------------------------------

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),        # positive
        (-2, -3, -5),     # negative
        (5, -2, 3),       # mixed
    ],
)
def test_sum_endpoint_scenarios(a, b, expected):
    r = requests.get(f"{API_ROOT}/sum", params={"a": a, "b": b}, timeout=2)
    assert r.status_code == 200
    body = r.json()
    assert "result" in body
    assert body["result"] == pytest.approx(expected, rel=1e-6)

# -----------------------------------------------------------
# /difference endpoint
# -----------------------------------------------------------

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),        # positive
        (-5, -3, -2),     # negative
        (5, -3, 8),       # mixed
    ],
)
def test_difference_endpoint_scenarios(a, b, expected):
    r = requests.get(f"{API_ROOT}/difference", params={"a": a, "b": b}, timeout=2)
    assert r.status_code == 200
    body = r.json()
    assert "result" in body
    assert body["result"] == pytest.approx(expected, rel=1e-6)

# -----------------------------------------------------------
# /product endpoint
# -----------------------------------------------------------

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),        # positive
        (-2, -3, 6),      # negative
        (2, -3, -6),      # mixed
    ],
)
def test_product_endpoint_scenarios(a, b, expected):
    r = requests.get(f"{API_ROOT}/product", params={"a": a, "b": b}, timeout=2)
    assert r.status_code == 200
    body = r.json()
    assert "result" in body
    assert body["result"] == pytest.approx(expected, rel=1e-6)

# -----------------------------------------------------------