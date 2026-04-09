import re

# Common passwords list (Can be expanded later)
COMMON_PASSWORDS = [
    "password", "123456", "qwerty", "letmein", "admin", "welcome", "iloveyou", "12345678"
]

def check_password_strength(password: str):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    else:
        feedback.append("Password should be at least 12 characters long.")

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")
    # Special character check
    if re.search(r"[!@#$%^&*()<.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")
    # Common password check
    if password.lower() not in COMMON_PASSWORDS:
        score += 2
    else:
        feedback.append("Password is too common.")

    # Repeated character check
    if not re.search(r"(.)\1{2,}", password):
        score += 2
    else:
        feedback.append("Avoid repeated characters.")
    return score, feedback

def strength_label(score: int) -> str:
    if score <= 3:
        return "Weak"
    elif score <= 6:
        return "Moderate"
    elif score <= 8:
        return "Strong"
    else:
        return "Very Strong"
def main():
    password = input("Enter a password to evaluate: ")

    score, feedback = check_password_strength(password)

    print("\nPassword Strength Report")
    print("-" * 30)
    print(f"Score: {score}/10")
    print(f"Strength: {strength_label(score)}")

    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Excellent password! No improvements needed.")

if __name__ == "__main__":
    main()