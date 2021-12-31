<?php 
session_start();

if (isset($_SESSION['id']) && isset($_SESSION['user_name'])) {

?>

<!DOCTYPE html>
<html lang="en">
<head>
<link rel="icon" type="image/ico" href="/favicon.ico"/>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
    <link rel="stylesheet" href="style1.css">
</head>
<body>
    <div class="top">
                    <a href="index.php"><img src="logo.jpg" alt="" class="logo"></a>
                    
                    <div>
                              <h1>Programing</h1>
                    </div>
                    
    </div>
    <div class="main">
        <h1>Profile</h1>
        <h2>Username</h2>
        <h3><?php $name ?></h3>
        <h2>Password</h2>
        <h3><?php $password ?></h3>

    </div>

    <div class="side">
                    <ul>
                              <li><a href="index (1).php" target="_blank">LOGIN</a></li>
                              <li><a href="About.html" target="_blank">About</a></li>
                              <li><a href="Contact Us.html" target="_blank">Contact us</a></li>
                              <li><a href="Videos.html" target="_blank">Videos</a></li>
                              <li><a href="Channels.html" target="_blank">Channels I learn from it</a></li>
                    </ul>
    </div>
</body>
</html>