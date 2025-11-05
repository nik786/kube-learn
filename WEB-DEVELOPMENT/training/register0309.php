<?php
$fn=$_POST["fname"];
$email=$_POST["email"];
$mobile=$_POST["mobile"];
$list=$_POST["list"];
include 'smtp/Send_Mail.php';
mail('sudipta1436@gmail.com',$fn.'---'.' has sent you a message','Email'.'...'.$email.'  '.'Services:'.'  '.$list.'   Phone:'.''.$mobile);
header("Location:contact2.html");
?>
