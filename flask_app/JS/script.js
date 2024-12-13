// Toggle between Sign In and Sign Up (Single event listener for the toggle)
document.querySelector('.img-btn').addEventListener('click', function() {
    document.querySelector('.cont').classList.toggle('s-signup');
});

// Password validation for Sign Up
function validatePassword(password) {
    // Password rules: Minimum 8 characters, at least one uppercase letter, one number, and one special character
    const passwordPattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordPattern.test(password);
}

// Handle the Sign Up form submission
const signUpForm = document.getElementById('signUpForm');
const passwordField = document.getElementById('password');
const confirmPasswordField = document.getElementById('confirm_password');

// When the user tries to submit the sign-up form
signUpForm.addEventListener('submit', function(event) {
    const password = passwordField.value;
    const confirmPassword = confirmPasswordField.value;

    // Check if password is valid
    if (!validatePassword(password)) {
        Swal.fire({
            icon: 'error',
            title: 'Password Error',
            text: 'Password must be at least 8 characters long, include at least one uppercase letter, one number, and one special character.',
        });
        event.preventDefault(); // Prevent form submission
        return;  // Stop the function from running further
    }

    // Check if confirm password matches the password
    if (confirmPassword !== password) {
        Swal.fire({
            icon: 'warning',
            title: 'Password Mismatch',
            text: 'Confirm password does not match the entered password.',
        });
        event.preventDefault(); // Prevent form submission
        return;  // Stop the function from running further
    }
});

// Handle the Sign In form validation
const signInForm = document.getElementById('signInForm');
const signInEmailField = document.querySelector('input[name="email"]');
const signInPasswordField = document.querySelector('input[name="password"]');

// Password validation for Sign In
function validatePasswordSignIn(password) {
    // Basic validation: password must be at least 8 characters long
    const passwordPattern = /^(?=.*[A-Za-z\d@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordPattern.test(password);
}

// When the user tries to submit the sign-in form
signInForm.addEventListener('submit', function(event) {
    const email = signInEmailField.value;
    const password = signInPasswordField.value;

    // Basic validation to ensure both fields are filled
    if (!email || !password) {
        Swal.fire({
            icon: 'error',
            title: 'Empty Fields',
            text: 'Please enter both email and password.',
        });
        event.preventDefault(); // Prevent form submission
        return;
    }

    // Check if password is valid
    if (!validatePasswordSignIn(password)) {
        Swal.fire({
            icon: 'error',
            title: 'Password Error',
            text: 'Password must be at least 8 characters long and contain letters, numbers, or special characters.',
        });
        event.preventDefault(); // Prevent form submission
        return;
    }
});
