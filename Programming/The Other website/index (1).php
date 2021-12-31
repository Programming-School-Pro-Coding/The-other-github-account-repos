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
        <label for="uname">User Name</label>
        <input type="email" name="uname" placeholder="User Name"><br>

        <label for="password">Password</label>
        <input type="password" name="password" placeholder="Password"><br>
        <label>Gender</label>
        <br>
        <label>male</label> 
        <input type="radio" name="Gender" placeholder="fmail" value="male"></input>
        <br>
        <label>female</label>
        <input type="radio" name="Gender" placeholder="w" value="female"></input>

        <label>Developers</label>
        <input type="checkbox" name="Developers" placeholder="Developers" value="Front End">Front End</input>
        <input type="checkbox" name="Developers" placeholder="Developers" value="Front End">Back End</input>
        <input type="checkbox" name="Developers" placeholder="Developers" value="Front End">Full Stack Developers</input>

        <button type="submit">Login</button>
        
     </form>
</body>
</html>
