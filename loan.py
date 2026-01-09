def check_eligibility(age: int, annual_income: float, credit_score: int, has_existing_loan: bool) -> str:
    """
    Determine loan eligibility based on applicant details.
    
    Rules:
    - Eligible: age >= 21, annual income >= 25000, credit_score >= 750, no existing loan
    - Partially Eligible: age >= 21, annual income >= 20000, credit_score between 650–749
    - Not Eligible: otherwise
    """
    if age >= 21 and annual_income >= 25000 and credit_score >= 750 and not has_existing_loan:
        return "Eligible"
    elif age >= 21 and annual_income >= 20000 and 650 <= credit_score < 750:
        return "Partially Eligible"
    else:
        return "Not Eligible"


def main():
    name = input("Enter Applicant Name: ").strip()
    age = int(input("Enter Age: "))
    annual_income = float(input("Enter Annual Income: "))
    credit_score = int(input("Enter Credit Score (300–850): "))
    has_existing_loan = input("Existing Loan (yes/no): ").strip().lower() == "yes"

    result = check_eligibility(age, annual_income, credit_score, has_existing_loan)

    print("\n--- Loan Eligibility Result ---")
    print(f"Applicant Name: {name}")
    print(f"Status: {result}")


if __name__ == "__main__":
    main()
