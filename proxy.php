<?php
$n_threads = 100;
$threads = [];

function scrap() {
    try {
        $https = file_get_contents("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0");
        $http = file_get_contents("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0");
        $socks = file_get_contents("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=0");
    } catch (Exception $e) {
        echo $e;
        return false;
    }
    $f = fopen("proxies.txt", "w");
    fwrite($f, $https."\n".$http);
    fclose($f);
    $f = fopen("socks.txt", "w");
    fwrite($f, $socks);
    fclose($f);
}

function checker($proxy) {
    $proxies = [
        'http' => $proxy,
        'https' => $proxy
    ];
    try {
        // replace the view2 function with the actual code for checking the proxy
        view2($proxy);
    } catch (Exception $e) {
        return false;
    }
}

function start() {
    $s = scrap();
    if ($s === false) {
        return;
    }
    $list = file("proxies.txt");
    foreach ($list as $i) {
        $p = trim($i);
        if (empty($p)) {
            continue;
        }
        while (count($threads) > $n_threads) {
            usleep(1000);
        }
        $thread = new Thread("checker", $p);
        $threads[] = $thread;
        $thread->start();
    }
    $list = file("socks.txt");
    foreach ($list as $i) {
        $p = trim($i);
        if (empty($p)) {
            continue;
        }
        while (count($threads) > $n_threads) {
            usleep(1000);
        }
        $pr = "socks5://".$p;
        $thread = new Thread("checker", $pr);
        $threads[] = $thread;
        $thread->start();
    }
    return true;
}

function process($run_for_ever = false) {
    if ($run_for_ever) {
        while (true) {
            start();
        }
    } else {
        start();
    }
}

process(true);
