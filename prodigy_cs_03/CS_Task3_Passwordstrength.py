import re

def password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r'\d', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None
    common_patterns = ['password', '123456', '123456789', 'qwerty', 'abc123', '111111']

    # Initial strength
    strength = 0
    suggestions = []

    # Check each criteria
    if length_criteria:
        strength += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    if digit_criteria:
        strength += 1
    else:
        suggestions.append("Password should include at least one digit.")

    if lowercase_criteria:
        strength += 1
    else:
        suggestions.append("Password should include at least one lowercase letter.")

    if uppercase_criteria:
        strength += 1
    else:
        suggestions.append("Password should include at least one uppercase letter.")

    if special_char_criteria:
        strength += 1
    else:
        suggestions.append("Password should include at least one special character (@$!%*?&#).")

    if any(pattern in password for pattern in common_patterns):
        suggestions.append("Password should not contain common patterns (e.g., 'password', '123456').")

    # Calculate strength as a percentage
    strength_percentage = (strength / 5) * 100

    return strength_percentage, suggestions

def main():
    password = input("Enter a password to check its strength: ")
    strength_percentage, suggestions = password_strength(password)

    print(f"Password Strength: {strength_percentage}%")
    if suggestions:
        print("Suggestions for improving your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
