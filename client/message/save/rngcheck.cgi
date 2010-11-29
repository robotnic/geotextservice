#! /usr/bin/eruby -d
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>

<%

#startnew
require 'xml'

def errorHandler(no, message)
        xml="<error no='"+no.to_s+"'>"+message+"</error>"
        return xml
end


XML::Error.set_handler do |error|
        puts errorHandler(234, error.to_s)
        
end

# parse schema as xml document
relaxng_document = XML::Document.file('../../../interface/message/save/response.rng')

# prepare schema for validation
relaxng_schema = XML::RelaxNG.document(relaxng_document)
#endnew
begin
instance = XML::Document.file('responseerror1.xml')
rescue #keine ausgabe

end
# validate returns row error message and exits.
begin
    instance.validate_relaxng(relaxng_schema)
rescue Exception => e
    puts e.message
else
    puts "ok"
end



%>