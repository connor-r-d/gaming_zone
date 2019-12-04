<?php 
	include 'header.php';
?>

<div class="image_section">
	
</div>

<div class="input_section">
	
	<div class="search_bar">
		
	</div>
	
	<div class="filter_bar">
		
	</div>
	
	<div class="upload_bar">
		
	</div>
	
</div>

<form action="includes/uploading.php" method="POST">
	
	<input type="text" name="title" placeholder="Title">
	<br>
	<input type="text" name="content" placeholder="Content">
	<br>
	<input type="text" name="descriptors" placeholder="Descriptors">
	<br>
	<button type="submit" name="submit">Sign up</button>
	
</form>

<?php

function createPreview($text, $limit) {
	$text = preg_replace('/\[\/?(?:b|i|u|s|center|quote|url|ul|ol|list|li|\*|code|table|tr|th|td|youtube|gvideo|(?:(?:size|color|quote|name|url|img)[^\]]*))\]/', '', $text);
	
	if (strlen($text) > $limit) return substr($text, 0, $limit) . "...";
	return $text;
}

	$sql = "SELECT * FROM individual_games";
	$stmt = mysqli_stmt_init($conn);
	if (!mysqli_stmt_prepare($stmt, $sql)){
		echo "SQL statement failed";
	} else {
		mysqli_stmt_execute($stmt);
		$result = mysqli_stmt_get_result($stmt);
		
		while ($row = mysqli_fetch_assoc($result)){
			
		  echo "<form class='individual_games_container'>
				
					<div class='top_section'>
						<p class='title' name='title'>".$row['title']."</p>
						<p class='content' name='content'>".createPreview($row['content'], 250)."</p>
					</div>

					<div class='bottom_section'>
						<button type='submit' name='see_more' class='read_more'><a href='individual_games_pages.php'>See More</a></button>

						<div class='rating_system'>

							<i class='fa fa-thumbs-o-up'></i>
							<i class='fa fa-thumbs-o-down'></i>

						</div>

						<p class='descriptors' name='descriptors'>".$row['descriptors']."</p>
					</div>
				
				</form>";
			
		}
	}

?>


<?php 
	include 'footer.php';
?>