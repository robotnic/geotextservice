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
textMsgSave = "<gts key='"+key+"'><content lat='48.3' lon='-23.6' id='1'>Vogel Quax zwickt Johnys Pferd Bim</content></gts>"

urlMsgSave = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/message/save')
requestMsgSave.body = textMsgSave
responseMsgSave = Net::HTTP.start(urlMsgSave.host, urlMsgSave.port){|http| http.request(requestMsgSave)}

responseMsgSave = responseMsgSave.body
#puts responseLogin
xml = XML::Document.string(responseMsgSave)
id1=xml.find("/gts/content/@id").first.value

#Message2 vorher schreiben
textMsgSave = "<gts key='"+key+"'><content lat='50.1' lon='15.6' id='1'>Text 3 Vogel Quax zwickt Johnys Pferd Bim</content></gts>"

urlMsgSave = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/message/save')
requestMsgSave.body = textMsgSave
responseMsgSave = Net::HTTP.start(urlMsgSave.host, urlMsgSave.port){|http| http.request(requestMsgSave)}

responseMsgSave = responseMsgSave.body
#puts responseLogin
xml = XML::Document.string(responseMsgSave)
id2=xml.find("/gts/content/@id").first.value

getResponse('../../../interface/message/delete/response.rng', 'http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/message/delete', 15, 3, key, id1, id2)

%>
