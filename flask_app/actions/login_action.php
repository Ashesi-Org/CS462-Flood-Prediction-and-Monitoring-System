<?php
// Include the database connection file
include('../settings/db_connection.php');  

// Get the action from the request
$action = $_POST['action'] ?? '';

// Handle login action
if ($action == 'login') {
    $email = $_POST['email'];
    $password = $_POST['password']; 

    // Check if the user exists
    $stmt = $conn->prepare("SELECT * FROM Users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();
    $user = $result->fetch_assoc();

    if ($user && password_verify($password, $user['password_hash'])) {
        // Login success - redirect to home.php
        header("Location: ../view/home.php");  // Adjust the path if needed
        exit();  // Ensure no further code is executed after redirect
    } else {
        // Invalid credentials - return error message
        echo json_encode(['success' => false, 'message' => 'Invalid email or password']);
    }

    $stmt->close();
}

$conn->close();
?>