<?php 
session_start();

if (isset($_SESSION['id']) && isset($_SESSION['user_name'])) {

 ?>
<!DOCTYPE html>
<html>
<head>
<link rel="icon" type="image/ico" href="/favicon.ico"/>

	<title>Your Profile</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
     <div class="top">
          <img src="/channels4_profile.jpg" alt="">
          <div>
               <h1>Programing</h1>
          </div>
          </div>
     <div class="main">
          <h1>Hello, <?php echo $_SESSION['name']; ?></h1>
     </div>

     <div class="side">
               <ul>
                    <li><a href="pages/About.html" target="_blank">About</a></li>
                    <li><a href="pages/Contact us.html" target="_blank">Contact us</a></li>
                    <li><a href="pages/Videos.html" target="_blank">Videos</a></li>
               </ul>
     </div>
</body>
</html>

<?php 
}else{
     header("Location: index.php");
     exit();
}
 ?> 