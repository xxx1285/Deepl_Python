<?php
// Предотвращаем встраивание страницы в рамки (фреймы) для защиты от кликджекинга
header('X-Frame-Options: DENY');
// Включаем встроенные средства браузера для защиты от XSS атак
header('X-XSS-Protection: 1; mode=block');
// Запрещаем браузеру "угадывать" MIME-тип содержимого
header('X-Content-Type-Options: nosniff');

$user_agent = $_SERVER['HTTP_USER_AGENT'];

// Проверяем, является ли user-agent поисковым ботом
if (preg_match('/bot|crawl|slurp|spider|googlebot|bingbot|yahoo|yandex|baidu|duckduckbot/i', $user_agent)) {
    // 301
    header("HTTP/1.1 301 Moved Permanently");
    header("Location: index.html");
    exit();
} else {
    // Устанавливаем политику отправки заголовка Referer
    header('Referrer-Policy: no-referrer-when-downgrade');
    // 301
    header("HTTP/1.1 301 Moved Permanently");
    header("Location: example.php");
    exit();
}
?>