<?php
// Include the database connection file
include('../settings/db_connection.php');  

// Password validation function
function validatePassword($password) {
    // Password rules: Minimum 8 characters, at least one uppercase letter, one number, and one special character
    $passwordPattern = '/^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/';
    return preg_match($passwordPattern, $password);
}

// Get the action from the request
$action = $_POST['action'] ?? '';

// Handle signup action
if ($action == 'signup') {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];

    // Check if the email already exists
    $stmt = $conn->prepare("SELECT * FROM Users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();
    $existingUser = $result->fetch_assoc();

    if ($existingUser) {
        echo json_encode(['success' => false, 'message' => 'Email already exists']);
    } else {
        // Check if the password is strong and confirm password matches
        if (!validatePassword($password)) {
            echo json_encode(['success' => false, 'message' => 'Password does not meet the required criteria']);
            return;
        }

        if ($password !== $confirm_password) {
            echo json_encode(['success' => false, 'message' => 'Passwords do not match']);
            return;
        }

        // Insert the new user
        $passwordHash = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $conn->prepare("INSERT INTO Users (username, email, password_hash) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $username, $email, $passwordHash);
        $stmt->execute();

        if ($stmt->affected_rows > 0) {
            // Redirect to the login page after successful registration
            header("Location: ../view/login.php");
            exit();  // Ensure the script stops executing after the redirect
        } else {
            echo json_encode(['success' => false, 'message' => 'Error during registration']);
        }
        $stmt->close();
    }
}

$conn->close();
?>