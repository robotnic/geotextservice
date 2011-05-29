#! /usr/bin/eruby -d
<?xml version="1.0"?>

<%

require "uri"
require "net/http"
require 'cgi'
require "xml"


cgi = CGI.new

query = "bbox=0,0,20,20";

puts "<b>Query:</b>" , query

time = Time.now.to_i

begin
	url = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/message/loadnew')

	params = {'bbox'=>'0,0,10,10'}

	#xml = IO.read("load.xml")
	http = Net::HTTP.new(url.host, url.port) 

	request = Net::HTTP::Get.new(url.path)
	request.set_form_data( params )

	# instantiate a new Request object
	request = Net::HTTP::Get.new( url.path+ '?' + request.body )

	response = ""
	response = http.request(request)
	
	response = response.body
	
rescue
	puts "Get funktioniert nicht"
end

puts "<br/>"
puts "<b>Response:</b>" 
response2 = response.gsub("<", "&lt;")
		response2 = response2.gsub(">", "&gt;")
		puts "<pre>", response2 , "</pre>"


# parse schema as xml document
relaxng_document = XML::Document.file('../../../interface/message/load/response.rng')

# prepare schema for validation
relaxng_schema = XML::RelaxNG.document(relaxng_document)

# parse xml document to be validated
instance = XML::Document.string(response)

# validate returns row error message and exits.
begin
  instance.validate_relaxng(relaxng_schema)
rescue Exception => e
  puts "<br/><div class='error'>"
	puts e.message
	puts "</div>"
else
  puts "<br/><div class='ok'>RNG: ok</div>"
end






%>

