#! /usr/bin/eruby -d
<?xml version="1.0" encoding="UTF-8"?>
<%

require "../../functions.rb"

getResponse('../../../interface/message/save/response.rng', 'http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/message/save', 15, 3)


#require "uri"
#require "net/http"
#require 'cgi'
#require "xml"

#cgi = CGI.new


	#################
	##LOAD RELAX NG##
	#################
	#parse schema as xml document
#	relaxng_document = XML::Document.file('../../../interface/message/save/response.rng')

	# prepare schema for validation
#	relaxng_schema = XML::RelaxNG.document(relaxng_document)


#type = cgi['type']
#if type == "" 
#	type = "error"
#end

#send_all = false
#id = cgi['id']
#if id == "" 
#	send_all = true
#end

#url = URI.parse('http://vs099.virtual.fhstp.ac.at/~dm101527/geotextservice/API/message/save')

#if(send_all == false)
#	begin
#		xml = IO.read(type.to_s() + id.to_s() + ".xml")
#	rescue
#		puts "fehler beim lesen von datei " + type.to_s() + id.to_s() + ".xml"
#		exit
#	end
	
#	request = Net::HTTP::Post.new(url.path)

#	request.body = xml
	#puts xml , "<br/>"

#	response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}

#	response = response.body
	#####################
	##VALIDATE RELAX NG##
	#####################
	# parse xml document to be validated
#	begin
#		instance = XML::Document.string(response)
#	rescue
#		puts "Fehler im Response (XML)", instance
#		exit
#	end

	# validate returns row error message and exits.
#	begin
#	  instance.validate_relaxng(relaxng_schema)
#	rescue Exception => e
#	  puts e.message
#	else
#	  puts "<RNG>ok</RNG>"
#	end

	# für response
	#response = response.gsub("<", "&lt;")
	#response = response.gsub(">", "&gt;")

#	if(response != "")
#		puts response
#	end
		
	
#else
	# loop durch alle errors
#	["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"].each { |the_id| 
		
#		begin
#			xml = IO.read("error" + the_id + ".xml")
			
#			request = Net::HTTP::Post.new(url.path)

#			request.body = xml
#			puts the_id , " - "
#			puts xml , "<br/>"

#			response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}
#			response = response.body

			#####################
			##VALIDATE RELAX NG##
			#####################
			# parse xml document to be validated
#			instance = XML::Document.string(response)

			# validate returns row error message and exits.
#			begin
#			  instance.validate_relaxng(relaxng_schema)
#			rescue Exception => e
#			  puts "<RNG>" + e.message + "</RNG>"
#			else
#			  puts "<RNG>ok</RNG>"
#			end

			# für response
			#response = response.gsub("<", "&lt;")
			#response = response.gsub(">", "&gt;")

#			puts "sending..."
#			if(response != "")
#				puts response
#			end
#		rescue
#			puts "fehler beim lesen von datei error" + the_id + ".xml"
#		end
#		puts "<br/>"
#		puts "<br/>"
#	} 


#end

	


%>
