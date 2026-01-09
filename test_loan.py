from loan import check_eligibility

def test_eligible():
    assert check_eligibility(30, 30000, 780, False) == "Eligible"

def test_partially_eligible():
    assert check_eligibility(25, 22000, 700, False) == "Partially Eligible"

def test_not_eligible_low_income():
    assert check_eligibility(28, 15000, 720, False) == "Not Eligible"

def test_not_eligible_low_credit():
    assert check_eligibility(35, 40000, 600, False) == "Not Eligible"