#! /usr/bin/eruby -d
<?xml version="1.0" encoding="UTF-8"?>
<%

require "../../functions.rb"

require "uri"
require "net/http"
require 'xml'


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
#key=xml.find("/error/@no").first.value
#puts key


#Message vorher schreiben
textMsgSave = "<gts key='"+key+"'><content lat='48.3' lon='-23.6'>Hallo Welt 1</content></gts>"

urlMsgSave = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/message/save')

begin
	begin
		requestMsgSave = Net::HTTP::Post.new(urlMsgSave.path)
		requestMsgSave.body = textMsgSave
		puts textMsgSave
	rescue
		puts "Request 1 geht schief"
	end
	
	begin
		responseMsgSave = Net::HTTP.start(urlMsgSave.host, urlMsgSave.port){|http| http.request(requestMsgSave)}
		responseMsgSave = responseMsgSave.body
		puts "response: "
		puts responseMsgSave
	rescue
		puts "Response 1 passt nicht"
	end
	
	begin
		xml = XML::Document.string(responseMsgSave)
		id1=xml.find("/gts/content/@id").first.value
		puts id1
	rescue
		puts "Finde id1 geht schief"
	end

	#Message2 vorher schreiben
	textMsgSave2 = "<gts key='"+key+"'><content lat='50.1' lon='15.6'>Text 3 2</content></gts>"

	urlMsgSave2 = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/message/save')
	
	begin
		requestMsgSave2 = Net::HTTP::Post.new(urlMsgSave2.path)
		requestMsgSave2.body = textMsgSave2
		puts textMsgSave2
	rescue
		puts "Request 2 geht schief"
	end

	begin
		responseMsgSave2 = Net::HTTP.start(urlMsgSave2.host, urlMsgSave2.port){|http| http.request(requestMsgSave2)}
		responseMsgSave2 = responseMsgSave2.body
		puts "response: "
		puts responseMsgSave2
	rescue
		puts "Response 2 passt nicht"
	end
	
	begin
		xml = XML::Document.string(responseMsgSave2)
		id2=xml.find("/gts/content/@id").first.value
		puts id2
	rescue
		puts "Finde id2 geht schief"
	end
rescue
	puts "Save geht nicht"
	exit
end

getResponse('../../../interface/message/delete/response.rng', 'http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/message/delete', 6, 2, key, id1, id2)

%>
