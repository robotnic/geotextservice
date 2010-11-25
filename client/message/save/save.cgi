#! /usr/bin/eruby -d
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>

<%

require "uri"
require "net/http"
require 'cgi'

cgi = CGI.new

type = cgi['type']
if type == "" 
	type = "error"
end

send_all = false
id = cgi['id']
if id == "" 
	send_all = true
end

url = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/message/save')

if(send_all == false)

	xml = IO.read(type.to_s() + id.to_s() + ".xml")
	
	request = Net::HTTP::Post.new(url.path)

	request.body = xml
	puts xml , "<br/>"

	response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}

	response = response.body


	# für response
	response = response.gsub("<", "&lt;")
	response = response.gsub(">", "&gt;")

	puts "sending..."
	if(response != "")
		puts "response " , response
	end
	
else
	# loop durch alle errors
	["01", "02", "03", "04"].each { |the_id| 
	
		xml = IO.read("error" + the_id + ".xml")

		request = Net::HTTP::Post.new(url.path)

		request.body = xml
		puts xml , "<br/>"

		response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}

		response = response.body


		# für response
		response = response.gsub("<", "&lt;")
		response = response.gsub(">", "&gt;")

		puts "sending..."
		if(response != "")
			puts "response " , response
		end
		puts "<br/>"
		puts "<br/>"

	} 


end

	


%>
</body>
</html>