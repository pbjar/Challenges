<?php
    $dir = 'sandbox/' . $_SERVER['REMOTE_ADDR'];
    if ( !file_exists($dir) )
        mkdir($dir);
    chdir($dir);

    $arghes = $_GET['args'];
    for ( $i=0; $i<count($arghes); $i++ ){
        if ( !preg_match('/^\w+$/', $arghes[$i]) )
            exit();
    }
    exec("echo " . implode(" ", $arghes));
?>

<html>
<head>
    <title> omgsosmolhowhacc </title>

    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<div class="container">
<div class="jumbotron">
    <div class="login-form">
        <h6> Oops no flag... forgot to put it here for you ¯\_(ツ)_/¯ It's somewhere on the server I think. </h6>
    </div>
</div>
</div>
</html>
