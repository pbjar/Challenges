<?php
    unset($errormsg);

    if(isset($_POST['username']) && isset($_POST['password']))
    {
        if($_POST['username'] === 'admin' && $_POST['password'] === 'admin')
        {
            $errormsg = '<h4 class="text-center" style="color:red"> the admin must have put some additional security protections here</h4>';
        }
        else
        {
            $errormsg = '<h4 class="text-center" style="color:red">Incorrect username or password</h4>';
        }
    }
    if($_SERVER['REQUEST_METHOD'] === 'PUT')
    {
        $raw_data = file_get_contents("php://input");
        $logindata = explode('&', $raw_data);
        if($logindata[0] === 'username=admin' && $logindata[1] === 'password=admin')
        {
            $errormsg = '<h4 class="text-center" style="color:green">Ah so you must indeed be admin if you put through those protections! The flag is flag{HTTP_r3qu35t_m3th0d5_ftw}</h4>';
        }
        else
        {
            $errormsg = "<h4 class='text-center' style='color:red'>$raw_data</h4>";
        }
    }
?>

<html>
<head>
    <title> cOrL </title>

    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<div class="container">
<div class="jumbotron">
    <div class="login-form">
        <form role="form" action="index.php" method="post">
            <div class="form-group">
                <input type="text" name="username" id="password" class="form-control input-lg" placeholder="Username">
                <input type="password" name="password" id="password" class="form-control input-lg" placeholder="Password">
                <input type="submit" class="btn btn-lg btn-success btn-block" value="Login">
                <?php if (isset($errormsg)) echo $errormsg; ?>
            </div>
        </form>
    </div>
</div>
</div>
</html>