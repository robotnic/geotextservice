#! /usr/bin/eruby -d

<%
line = IO.readlines("blindtext.txt")

10.times{

blindtext =''

c = rand*line.length.to_i
zufallline =  line[c]

lat = rand(180)-90
long = rand(360)-180

require "uri"
require "net/http"

url = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101507/API/01/messages/save/')
request = Net::HTTP::Post.new(url.path)

text = "<gts key='EF988339EED5598DE8888776222EEAAA'><content lat='"+lat.to_s()+"' lon='"+long.to_s()+"'>"+zufallline+"</content><content lat='"+lat.to_s()+"' lon='"+long.to_s()+"' id='145'>"+zufallline+"</content></gts>"

request.body = text

response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}

response = response.body

response = response.gsub("<", "&lt;")
response = response.gsub(">", "&gt;")

puts "sending..."
puts "response" , response

}

%>


<form method="POST">
	URL: <input type="text" id="service_url" />
</form>