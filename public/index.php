<?php
require_once '../app/history.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Log a new user action
    $userId = 1; // Hardcoded for simplicity
    $action = $_POST['action'];
    $details = $_POST['details'];

    logUserAction($userId, $action, $details);
    header("Location: index.php");
    exit();
}

// Fetch all user history
$history = getUserHistory();

// Fetch Prometheus metrics
$prometheusMetrics = fetchPrometheusMetrics();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User History</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <h1>User History</h1>

    <!-- Form to log a new user action -->
    <form method="POST">
        <input type="text" name="action" placeholder="Action" required>
        <input type="text" name="details" placeholder="Details" required>
        <button type="submit">Log Action</button>
    </form>

    <!-- Display user history from the database -->
    <h2>History</h2>
    <table border="1">
        <tr>
            <th>Action</th>
            <th>Time</th>
            <th>Details</th>
        </tr>
        <?php foreach ($history as $entry): ?>
        <tr>
            <td><?= htmlspecialchars($entry['action']) ?></td>
            <td><?= htmlspecialchars($entry['action_time']) ?></td>
            <td><?= htmlspecialchars($entry['details']) ?></td>
        </tr>
        <?php endforeach; ?>
    </table>

    <!-- Display Prometheus metrics -->
    <h2>Metrics from Prometheus</h2>
    <table border="1">
        <tr>
            <th>Action</th>
            <th>Count</th>
        </tr>
        <?php if (!empty($prometheusMetrics)): ?>
            <?php foreach ($prometheusMetrics as $metric): ?>
            <tr>
                <td><?= htmlspecialchars($metric['action']) ?></td>
                <td><?= htmlspecialchars($metric['count']) ?></td>
            </tr>
            <?php endforeach; ?>
        <?php else: ?>
            <tr>
                <td colspan="2">No metrics available</td>
            </tr>
        <?php endif; ?>
    </table>
</body>
</html>
