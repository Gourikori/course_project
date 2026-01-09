def check_eligibility(age, income, credit_score, existing_loan):
    if age >= 21 and income >= 25000 and credit_score >= 750 and not existing_loan:
        return "Eligible"
    elif age >= 21 and income >= 20000 and 650 <= credit_score < 750:
        return "Partially Eligible"
    else:
        return "Not Eligible"


def main():
    name = input("Enter Applicant Name: ")
    age = int(input("Enter Age: "))
    income = int(input("Enter Monthly Income: "))
    credit_score = int(input("Enter Credit Score: "))
    existing_loan = input("Existing Loan (yes/no): ").lower() == "yes"

    result = check_eligibility(age, income, credit_score, existing_loan)

    print("\n--- Loan Eligibility Result ---")
    print("Applicant Name:", name)
    print("Status:", result)


if __name__ == "__main__":
    main()