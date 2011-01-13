

$(document).ready(function() {
  var startTime = new Date().getMilliseconds();

  // $.ajax({
    // url: 'http://vs099.virtual.fhstp.ac.at/~dm101513/geotextservice/client/message/save/save.cgi?type=error&id=01',
    // dataType: "html",
    // success: function(xml) {
      // read RNG status
      // var rng = "";
      // rng = $(xml).find("RNG").text();
      // alert("rng: " + rng);
      
      // alert("asdf" + rng);
      // $('.result').html(xml);
      
      // var totalTime = new Date().getMilliseconds() - startTime;
      // alert("Zeit: " + totalTime + "ms");
     
    // }
  // });

});


function doAll() {

	var paths = new Array(
						"save.cgi?type=error&id=01"
						
						);
	
	for(i=0;i<paths.length;i++) {
		doAjax(paths[i]);
	}

}

function doAjax(script) {
	//erstellen des requests
	var req = null;

	var path = "http://vs099.virtual.fhstp.ac.at/~dm101513/geotextservice/client/message/save/";
	
	try{
		req = new XMLHttpRequest();
	}
	catch (ms){
		try{
			req = new ActiveXObject("Msxml2.XMLHTTP");
		} 
		catch (nonms){
			try{
				req = new ActiveXObject("Microsoft.XMLHTTP");
			} 
			catch (failed){
				req = null;
			}
		}  
	}

	if (req == null)
		  alert("Error creating request object!");
	  
    //anfrage erstellen (GET, url ist localhost,
    //request ist asynchron      
    req.open("GET", path+script, true);
	
	req.onreadystatechange = function(){            
		switch(req.readyState) {
			case 4:
				if(req.status!=200) {
					alert("Fehler:"+req.status); 
				}else{    
					//schreibe die antwort in den div container mit der class result
					var newRes = document.createElement("div");
					$(newRes).addClass("response");
					$("#results").append($(newRes));
					$(".result").html(req.responseText);
				}
				break;
			default:
				return false;
				break;     
		}
	};

	  req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	req.send(null);
}