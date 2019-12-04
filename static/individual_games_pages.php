<?php 
	include 'header.php';
?>

<?php

if(!isset($_POST['see_more']))
{ 
	
echo "It's not working... for some reason";
	
} else {
echo "<div class='container'>" . $_POST["title"] . "</br>" . $_POST["descriptors"] . "</br>" . $_POST["content"] . "</div>";
}

?>

<?php 
	include 'footer.php';
?>