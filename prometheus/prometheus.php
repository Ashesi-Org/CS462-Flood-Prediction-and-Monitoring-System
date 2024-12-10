<?php
function trackUserAction($action)
{
    $url = 'http://localhost:9091/metrics/job/user_history_tracking';
    $data = "user_action_count{action=\"$action\"} 1\n";

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_exec($ch);
    curl_close($ch);
}
