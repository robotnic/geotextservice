require "uri"
require "net/http"
require 'cgi'
require "xml"

def getResponse(relaxDocument, requestUrl, erroranzahl, correctanzahl, key=0, id1=0, id2=0)
	#if(key!=0)
	#	puts key
	#end

	cgi = CGI.new

	#################
	##LOAD RELAX NG##
	#################
	#parse schema as xml document
	relaxng_document = XML::Document.file(relaxDocument)

	# prepare schema for validation
	relaxng_schema = XML::RelaxNG.document(relaxng_document)


	type = cgi['type']
	if type == "" 
		type = "error"
	end

	send_all = false
	id = cgi['id']
	if id == "" 
		send_all = true
	end

	url = URI.parse(requestUrl)

	if(send_all == false)
			x = type.to_s() + id.to_s()+".xml"
		begin
			xml = IO.read("error/"+x)
		rescue
			puts "fehler beim lesen von datei " + type.to_s() + id.to_s() + ".xml"
			exit
		end
		
		request = Net::HTTP::Post.new(url.path)

		request.body = xml
		
		begin
			if(key!=0)
				if (xml.match('[key]'))
					xml["[key]"]= key
				end
			end
		rescue
			#puts "Fehler: key ersetzen"
		end
		begin
			if(id1!=0)
				if (xml.match('[id1]'))
					xml["[id1]"]= id1
				end
			end
		rescue
			#puts "Fehler: id1 ersetzen"
		end
		begin
			if(id2!=0)
				if (xml.match('[id2]'))
					xml["[id2]"]= id2
				end
			end
		rescue
			#puts "Fehler: id2 ersetzen"
		end
		
		puts x , ":<br/>"

                # fuer request output
		xml2 = xml.gsub("<", "&lt;")
		xml2 = xml2.gsub(">", "&gt;")
		puts "<pre>", xml2 , "</pre>"

		begin
			response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}
		rescue
			puts "Fehler: Schick Request"
		end
		response = response.body

		#####################
		##VALIDATE RELAX NG##
		#####################
		# parse xml document to be validated
		begin
			instance = XML::Document.string(response)
		rescue
			puts "Fehler im Response (XML)"
			exit
		end

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

		# f�r response
		response = response.gsub("<", "&lt;")
		response = response.gsub(">", "&gt;")
	
		if(response != "")
			puts "<br/>Response: <pre>" , response , "</pre>"
		end
	else
		# alle Dateien aus Directory
		d = Dir.new("error")
		# loop durch alle files / Check auf .xml
		d.each  {
			|x|
			if x.match('.xml')
				begin
					xml = IO.read('error/'+x)
				rescue
					puts "2: fehler beim lesen von datei " + x
					
				end
					request = Net::HTTP::Post.new(url.path)

					request.body = xml
					
					begin
						if(key!=0)
							if (xml.match('[key]'))
								xml["[key]"]= key
							end
						end
					rescue
						#puts "Fehler: key ersetzen<br/>"
					end
					begin
						if(id1!=0)
							if (xml.match('[id1]'))
								xml["[id1]"]= id1
							end
						end
					rescue
						#puts "Fehler: id1 ersetzen"
					end
					begin
						if(id2!=0)
							if (xml.match('[id2]'))
								xml["[id2]"]= id2
							end
						end
					rescue
						#puts "Fehler: id2 ersetzen"
					end
					
					puts x
					puts xml , "<br/>"

					begin
						response = Net::HTTP.start(url.host, url.port) {|http| http.request(request)}
					rescue
						puts "Fehler: Schick Request"
					end
					response = response.body
					puts "Response:"
					puts response

					#####################
					##VALIDATE RELAX NG##
					#####################
					# parse xml document to be validated
					begin
						instance = XML::Document.string(response)
					rescue
						puts "Fehler im Response (XML)"
					end
					# validate returns row error message and exits.
					begin
						instance.validate_relaxng(relaxng_schema)
					rescue Exception => e
						puts "<div class='error'>"
						puts e.message
						puts "</div>"
					else
						puts "<div class='ok'><b>RNG:</b> ok</div>"
					end

					# fuer response
					response = response.gsub("<", "&lt;")
					response = response.gsub(">", "&gt;")

					puts "sending..."
					if(response != "")
						puts "response " , response
					end
				
				puts "<br/>"
				puts "<br/>"
			end
		} 
	end
end
