// JavaScript Document

$(document).ready(function(){
	'use strict';
		$('.upload').click(function() {
				$('.page_overlay').css('display', 'block');
				$('.overlay').css('display', 'block');
		});

		$('.cross').click(function() {
				$('.page_overlay').css('display', 'none');
				$('.overlay').css('display', 'none');
		});
});
