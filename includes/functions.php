<?php

require("dbh.php");

function getUsersData($id){

		$array = array();
		$q = mysqli_query("SELECT * FROM 'individual_games' WHERE 'id'=".$id);
		while($row = mysqli_fetch_assoc($q)){
			$array['id'] = $row['id'];
			$array['title'] = $row['title'];
			$array['content'] = $row['content'];
			$array['descriptors'] = $row['descriptors'];
		}
		return $array;
}


?>