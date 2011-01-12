

$(document).ready(function() {
  var startTime = new Date().getMilliseconds();

  $.ajax({
    url: 'http://vs099.virtual.fhstp.ac.at/~dm101513/geotextservice/client/message/save/save.cgi?type=error&id=01',
    dataType: "html",
    success: function(xml) {
      // read RNG status
      var rng = "";
      rng = $(xml).find("RNG").text();
      alert("rng: " + rng);
      
      //alert("asdf" + rng);
      $('.result').html(xml);
      
      var totalTime = new Date().getMilliseconds() - startTime;
      //alert("Zeit: " + totalTime + "ms");
     
    }
  });

});