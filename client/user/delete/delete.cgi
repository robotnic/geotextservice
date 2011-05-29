#! /usr/bin/eruby -d
<?xml version="1.0"?>

<%

require "../../functions.rb"

#User vorher einloggen
user = "Kerstin"
pw = "1234"

urlLogin = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/user/login')
requestLogin = Net::HTTP::Post.new(urlLogin.path)

textLogin = "<gts><username>"+user+"</username><password>"+pw+"</password></gts>"

requestLogin.body = textLogin

responseLogin = Net::HTTP.start(urlLogin.host, urlLogin.port){|http| http.request(requestLogin)}

responseLogin = responseLogin.body
#puts responseLogin
xml = XML::Document.string(responseLogin)
key=xml.find("/gts/success/@key").first.value

#User anlegen
registerUser= "<gts><username>deleteme</username><password>1234</password></gts>"

urlRegisterUser = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/user/register')

begin
    puts "<br>starting input 1"
	begin
		requestRegisterUser = Net::HTTP::Post.new(urlRegisterUser.path)
		requestRegisterUser.body = registerUser
		puts registerUser
	rescue
		puts "Request 1 geht schief"
	end
	puts "<br>getting response 1"
	begin
		responseRegisterUser = Net::HTTP.start(urlRegisterUser.host, urlRegisterUser.port){|http| http.request(requestRegisterUser)}
		responseRegisterUser = responseRegisterUser.body
		puts "<br>response: "
		puts responseRegisterUser
	rescue
		puts "Response 1 passt nicht"
	end
    puts "<br>END of INSERTING DATA"
rescue
	puts "Save geht nicht"
	exit
end


#User anlegen
registerUser= "<gts><username>deleteme2</username><password>1234</password></gts>"

urlRegisterUser = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/user/register')

begin
    puts "<br>starting input 2"
	begin
		requestRegisterUser = Net::HTTP::Post.new(urlRegisterUser.path)
		requestRegisterUser.body = registerUser
		puts registerUser
	rescue
		puts "Request 2 geht schief"
	end
	puts "<br>getting response 2"
	begin
		responseRegisterUser = Net::HTTP.start(urlRegisterUser.host, urlRegisterUser.port){|http| http.request(requestRegisterUser)}
		responseRegisterUser = responseRegisterUser.body
		puts "<br>response: "
		puts responseRegisterUser
	rescue
		puts "Response 2 passt nicht"
	end
    puts "<br>END of INSERTING DATA"
rescue
	puts "Save2 geht nicht"
	exit
end


getResponse('../../../interface/user/delete/response.rng', 'http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/user/delete', 7, 2, key)

#require "uri"
#require "net/http"
#require 'cgi'
#require "xml"


#cgi = CGI.new

#type = cgi['type']

#url = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/user/delete')

#xml = IO.read("delete.xml")

#request = Net::HTTP::Post.new(url.path)

#request.body = xml
#puts "<b>Request:</b>" , xml

#response = ""
#response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}
#response = response.body
#puts "<br/>"
#puts "<b>Response:</b>" , response


# parse schema as xml document
#relaxng_document = XML::Document.file('../../../interface/user/delete/response.rng')

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

