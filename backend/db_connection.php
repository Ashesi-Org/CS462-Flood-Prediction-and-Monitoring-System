<?php
// Database credentials
require('db_cred.php');

// Creating a connection to link your database
$conn = mysqli_connect(Server, Username, Password, Database); 


// Checking connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
