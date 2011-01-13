require "uri"
require "net/http"
require 'cgi'
require "xml"

def getResponse(relaxDocument, requestUrl, erroranzahl, correctanzahl)

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
			xml = IO.read("errors/"+x)
		rescue
			puts "fehler beim lesen von datei " + type.to_s() + id.to_s() + ".xml"
			exit
		end
	
		request = Net::HTTP::Post.new(url.path)

		request.body = xml
		puts x
		puts xml , "<br/>"

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

		# für response
		response = response.gsub("<", "&lt;")
		response = response.gsub(">", "&gt;")
	
		if(response != "")
			puts "response " , response
		end
	else
		# alle Dateien aus Directory
		d = Dir.new("errors")
		# loop durch alle files / Check auf .xml
		d.each  {
			|x|
			if x.match('.xml')
				begin
					xml = IO.read('errors/'+x)

					request = Net::HTTP::Post.new(url.path)

					request.body = xml
					puts x , " - "
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
					instance = XML::Document.string(response)

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
				rescue
					puts "fehler1 beim lesen von datei " + x
				end
				puts "<br/>"
				puts "<br/>"
			end
		} 
	end
end
