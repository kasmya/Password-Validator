import tkinter as tk
from tkinter import messagebox

# Base class for basic password validation
class BasePasswordValidator:
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        """Checks if the password satisfies the base conditions."""
        has_lowercase = False
        has_uppercase = False
        has_digit = False
        has_special_char = False

        # Check each character in the password
        for char in self.password:
            if 'a' <= char <= 'z':
                has_lowercase = True
            elif 'A' <= char <= 'Z':
                has_uppercase = True
            elif '0' <= char <= '9':
                has_digit = True
            elif char in '#$₹':
                has_special_char = True

        # Rule 1: At least one lowercase letter
        if not has_lowercase:
            return "Password must contain at least one lowercase letter (a-z)."

        # Rule 2: At least one digit
        if not has_digit:
            return "Password must contain at least one digit (0-9)."

        # Rule 3: At least one uppercase letter
        if not has_uppercase:
            return "Password must contain at least one uppercase letter (A-Z)."

        # Rule 4: At least one special character from `#`, `$`, `₹`
        if not has_special_char:
            return "Password must contain at least one special character (#, $, ₹)."

        return True

# Advanced validator class for additional security features
class AdvancedPasswordValidator(BasePasswordValidator):
    def __init__(self, password):
        super().__init__(password)

    def is_valid(self):
        """Extends validation with advanced rules."""
        base_validation = super().is_valid()
        if base_validation is not True:
            return base_validation

        # Rule 5: Minimum length of 6 characters
        if len(self.password) < 6:
            return "Password must be at least 6 characters long."

        # Rule 6: Maximum length of 20 characters
        if len(self.password) > 20:
            return "Password must not exceed 20 characters."

        return "Password is valid!"

# GUI Implementation
def validate_password():
    password = password_entry.get()
    validator = AdvancedPasswordValidator(password)
    result = validator.is_valid()
    messagebox.showinfo("Validation Result", result)

# Create main window
root = tk.Tk()
root.title("Password Validator")

# GUI Layout
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack(pady=10)

validate_button = tk.Button(root, text="Validate Password", font=("Arial", 12), command=validate_password)
validate_button.pack(pady=10)

# Run the application
root.mainloop()
