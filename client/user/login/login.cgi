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

#type = cgi['type']

url = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/user/register')

xml = IO.read("register.xml")

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

%>
</body>
</html>