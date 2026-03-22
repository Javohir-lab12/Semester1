def validate_password(password):
    if len(password) < 8:
        return False
    if "password" in password.lower():
        return False
    if len([c for c in password if "A" <= c <= "Z"]) == 0:
        return  False
    if len([c for c in password if "0" <= c <= "9"]) == 0:
        return False
    return True

print(validate_password("apple"))           # False (too short)
print(validate_password("Password123"))     # False (contains 'password')
print(validate_password("security"))        # False (no uppercase, no digit)
print(validate_password("SecureCode99"))    # True