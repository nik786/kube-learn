<?php
function Send_Mail($to,$subject,$body)
{
require 'class.phpmailer.php';
$from       = "admin@linuxconnector.in";
$mail       = new PHPMailer();
$mail->IsSMTP(true);            // use SMTP
$mail->IsHTML(true);
$mail->SMTPAuth   = true;                  // enable SMTP authentication
$mail->Host       = "tls://mail.linuxconnector.in"; // Amazon SES server, note "tls://" protocol
$mail->Port       =  465;                    // set the SMTP port
$mail->Username   = "admin@linuxconnector.in";  // SMTP  username
$mail->Password   = "Lm8at%-Ty~&P";  // SMTP password
$mail->SetFrom($from, 'Linuxconnector');
$mail->AddReplyTo($from,'From Name');
$mail->Subject    = $subject;
$mail->MsgHTML($body);
$address = $to;
$mail->AddAddress($address, $to);
$mail->Send();   
}
?>
