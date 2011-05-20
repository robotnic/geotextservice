

var path = "http://vs099.virtual.fhstp.ac.at/~dm101504/geotextservice/client/message/save/";

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

// var paths = new Array();

// function doSave() {
	// //add save paths
	// for (i=1;i<16;i++) {
		 // = "save.cgi?type=error&id="+i;
		// paths.push(path);
	// }
	// for (i=1;i<4;i++) {
		// path = "save.cgi?type=correct&id="+i;
		// paths.push(path);
	// }
// }


// function doAll() {
	// for(i=0;i<paths.length;i++) {
		// doAjax(paths[i],i);
	// }

// }

function doMessageSave()
{
  clearResults();
  
  // alle xmls f�r message/save registrieren
  xmllist = new Array();
  for (i=1;i<16;i++) {
		var xml = "save.cgi?type=error&id="+i;
		xmllist.push(xml);
	}
	for (i=1;i<4;i++) {
		var xml = "save.cgi?type=correct&id="+i;
		xmllist.push(xml);
	}
  
  
  for(i=0;i<xmllist.length;i++) {
		doAjax(xmllist[i],i);
	}
}

function doAjax(script,id) {
	//erstellen des requests
	var req = null;

	
	
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

/*			  var newRes = document.createElement("div");
					$(newRes).addClass("response");
					$("#results").append($(newRes));
					$(".result").html(req.responseText);
*/					
					var newRes = document.createElement("div");
					$(newRes).addClass("response");
					$(newRes).attr("id", id);
          
          // var newRes = htmlEncode($(newRes).text());
          
					// $("#results").append(newRes);
          
          var responseText = req.responseText.toString();
          
          responseText2 = responseText.replace(\<\g,"&lt;");
          
					$("#"+id).html("<pre>" + responseText + "</pre>");

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

function clearResults()
{
  $(".response").remove();
}

function htmlEncode(s)
{
  var el = document.createElement("div");
  el.innerText = el.textContent = s;
  s = el.innerHTML;
  delete el;
  return s;
}

