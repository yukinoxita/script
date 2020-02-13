<?php
    //sql connect ato;
    echo"<br>";
    $error = $_FILES['file']['error']; 
    $tmp_name = $_FILES['file']['tmp_name'];
    $name = $_FILES['file']['name'];
    $size = $_FILES['file']['size'];
    $type = $_FILES['file']['type'];
    if($error == UPLOAD_ERR_OK && $size > 0)
    {
        $fp = fopen($tmp_name,'r');
        $content = fread($fp,$size);
        fclose($fp);
        $content = addslashes($content);
	$sql = "";
        $conn->query($sql);
        echo "file stored";
    }
    else
    {
        echo "ERROR"; 
    }
    $conn->close();
?>
