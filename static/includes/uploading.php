<?php 
	include_once 'dbh.php';

	$title = mysqli_real_escape_string($conn, $_POST['title']);
	$content = mysqli_real_escape_string($conn, $_POST['content']);
	$descriptors = mysqli_real_escape_string($conn, $_POST['descriptors']);

	$sql = "INSERT INTO individual_games (title, content, descriptors) VALUES (?, ?, ?);";
	$stmt = mysqli_stmt_init($conn);
	if (!mysqli_stmt_prepare($stmt, $sql)){
		echo "SQL error";
	} else {
		mysqli_stmt_bind_param($stmt, "sss", $title, $content, $descriptors);
		mysqli_stmt_execute($stmt);
	}

	header("Location: ../individual_games.php?upload=successful");
?>