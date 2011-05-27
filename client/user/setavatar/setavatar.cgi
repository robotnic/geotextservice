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

getResponse('../../../interface/user/setavatar/response.rng', 'http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/user/setavatar', 9, 1, key)

%>