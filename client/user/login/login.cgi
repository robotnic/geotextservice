#! /usr/bin/eruby -d
<?xml version="1.0"?>

<%

require "../../functions.rb"

getResponse('../../../interface/user/login/response.rng', 'http://vs099.virtual.fhstp.ac.at/~dm101507/geotextservice/API/user/login', 8, 1)

%>
