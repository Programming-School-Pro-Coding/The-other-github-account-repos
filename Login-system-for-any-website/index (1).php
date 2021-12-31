<!DOCTYPE html>
<html>
<head>
    <link rel="icon" type="image/ico" href="/favicon.ico"/>
    <meta charset="UTF-8">
	<title>LOGIN</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
     <form action="index.php" method="post">
        <h2>LOGIN</h2>
        <?php if (isset($_GET['error'])) { ?>
          <p class="error"><?php echo $_GET['error']; ?></p>
        <?php } ?>
        <label>User Name</label>
        <input type="email" name="uname" placeholder="User Name"><br>

        <label>User Name</label>
        <input type="password" name="password" placeholder="Password"><br>

        <button type="submit">Login</button>
     </form>
</body>
</html> 