#! /usr/bin/eruby -d

<%

require "uri"
require "net/http"
require 'xml'

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
puts key


# selektiere Key
# zurück kommt <gts query="user/login"><success username="Kerstin" key="23434543534"/></gts>

#
#responseLogin = responseLogin.gsub("<", "&lt;")
#responseLogin = responseLogin.gsub(">", "&gt;")

#puts responseLogin

line = IO.readlines("blindtext.txt")

1.times{

blindtext =''

c = rand*line.length.to_i
zufallline = line[c]

lat = rand(180)-90
long = rand(360)-180

url = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/message/save/')
request = Net::HTTP::Post.new(url.path)

text = "<gts key='"+key.to_s()+"'><content lat='"+lat.to_s()+"' lon='"+long.to_s()+"'>"+zufallline+"</content><content lat='"+lat.to_s()+"' lon='"+long.to_s()+"' id='145'>"+zufallline+"</content></gts>"

request.body = text

response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}

response = response.body

#response = response.gsub("<", "&lt;")
#response = response.gsub(">", "&gt;")
#
#puts "sending..."
puts "response:"
puts response

}
puts "fertig"
%>
