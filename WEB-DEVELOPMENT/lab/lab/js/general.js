$(document).ready(function(){

	$(".tab:not(:first)").hide();
	//to fix u know who
	$(".tab:first").show();
	$(".htabs a").click(function(){
		 $('.htabs li').removeClass('current');
		stringref = $(this).attr("href").split('#')[1];
		$(this).parent('li').addClass('current');
		$('.tab:not(#'+stringref+')').hide();
		if ($.browser.msie && $.browser.version.substr(0,3) == "6.0") {
			$('.tab#' + stringref).show();
		}
		else 
			$('.tab#' + stringref).fadeIn();
		return false;
	});
	
	
	
	
	
	
	
});

$(document).ready(function(){  	
	$(".read_plus").click(function(){	
	$(this).toggleClass('plus_icon');		
	$(".read_toogle").slideToggle(1000);
	});
});
