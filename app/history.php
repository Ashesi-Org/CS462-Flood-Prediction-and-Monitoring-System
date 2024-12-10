<?php
require_once '../config.php';
require_once '../prometheus/prometheus.php';

function logUserAction($userId, $action, $details)
{
    global $pdo;

    // Insert user action into the database
    $stmt = $pdo->prepare("INSERT INTO UserHistory (user_id, action, details) VALUES (:user_id, :action, :details)");
    $stmt->execute([
        'user_id' => $userId,
        'action' => $action,
        'details' => $details
    ]);

    // Send metrics to Prometheus
    trackUserAction($action);
}

function getUserHistory()
{
    global $pdo;

    // Fetch user history from the database
    $stmt = $pdo->query("SELECT * FROM UserHistory ORDER BY action_time DESC");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function fetchPrometheusMetrics()
{
    // Prometheus API endpoint for querying metrics
    $prometheusUrl = "http://localhost:9090/api/v1/query?query=user_action_count";

    // Fetch metrics using file_get_contents
    $response = @file_get_contents($prometheusUrl);

    // Handle errors
    if ($response === false) {
        return []; // Return an empty array if Prometheus is not reachable
    }

    $data = json_decode($response, true);

    // Extract metrics data
    $metrics = [];
    if (isset($data['data']['result'])) {
        foreach ($data['data']['result'] as $metric) {
            $metrics[] = [
                'action' => $metric['metric']['action'] ?? 'Unknown',
                'count' => $metric['value'][1] ?? 0,
            ];
        }
    }

    return $metrics;
}

// Fetch user history from the database
$historyData = getUserHistory();

// Fetch Prometheus metrics
$prometheusMetrics = fetchPrometheusMetrics();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User History</title>
    <link rel="stylesheet" href="../public/css/styles.css">
</head>
<body>
    <h1>User History</h1>

    <!-- Table for displaying user history from the database -->
    <h2>History Log</h2>
    <table border="1">
        <tr>
            <th>Action</th>
            <th>Action Time</th>
            <th>Details</th>
        </tr>
        <?php foreach ($historyData as $history): ?>
        <tr>
            <td><?= htmlspecialchars($history['action']) ?></td>
            <td><?= htmlspecialchars($history['action_time']) ?></td>
            <td><?= htmlspecialchars($history['details']) ?></td>
        </tr>
        <?php endforeach; ?>
    </table>

    <!-- Table for displaying Prometheus metrics -->
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
