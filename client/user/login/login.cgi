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
require "xml"

cgi = CGI.new

#type = cgi['type']

url = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/user/login')

xml = IO.read("login.xml")

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

# parse schema as xml document
relaxng_document = XML::Document.file('../../../interface/user/login/response.rng')

# prepare schema for validation
relaxng_schema = XML::RelaxNG.document(relaxng_document)

# parse xml document to be validated
instance = XML::Document.string(response)

# validate returns row error message and exits.
begin
  instance.validate_relaxng(relaxng_schema)
rescue Exception => e
  puts e.message
else
  puts "<br/>relax ok"
end

%>
</body>
</html>
