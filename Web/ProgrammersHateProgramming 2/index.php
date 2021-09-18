<?php
session_start();
if(!isset($_SESSION["notes"]) && !isset($note_array))
{
    $note_array = array("note1.php", "note2.php");
    $_SESSION["notes"]=$note_array;
}
?>

<html>
<head>
    <title> Programmers Hate Programming 2 </title>

    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<div class="container">
<div class="jumbotron">
    <div class="login-form">
        <form role="form" action="addnote.php" method="post">
            <div class="form-group">
                <input type="text" name="notewrite" id="notewrite" class="form-control input-lg" placeholder="New Note">
                <input type="submit" class="btn btn-lg btn-success btn-block" value="Add Note">
            </div>
        </form>
    </div>
</div>
<div class="jumbotron">
    <?php
        foreach($_SESSION["notes"] as $key=>$value)
        {
            $notenum = $key + 1;
            echo "<a href=$value> Note $notenum </a>" . "<br>";
        }
    ?>
</div>
</div>
</html>

