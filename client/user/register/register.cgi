#! /usr/bin/eruby -d
<?xml version="1.0"?>

<%

require "uri"
require "net/http"
require 'cgi'
require "xml"
require "../../functions.rb"

getResponse('../../../interface/user/register/response.rng', 'http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/user/register', 8, 1)



#cgi = CGI.new

#type = cgi['type']

#url = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/user/register')

#xml = IO.read("register.xml")

#request = Net::HTTP::Post.new(url.path)

#request.body = xml
#puts "<b>Request:</b>" , xml

#response = ""
#response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}
#response = response.body
#puts "<br/>"
#puts "<b>Response:</b>" , response


# parse schema as xml document
#relaxng_document = XML::Document.file('../../../interface/user/register/response.rng')

# prepare schema for validation
#relaxng_schema = XML::RelaxNG.document(relaxng_document)

# parse xml document to be validated
#instance = XML::Document.string(response)

# validate returns row error message and exits.
#begin
#  instance.validate_relaxng(relaxng_schema)
#rescue Exception => e
#  puts e.message
#else
#  puts "<br/><b>RNG:</b> ok"
#end




%>
