#!/usr/bin/php
Content-type:text/html

<?php
header("Content-type:text/html");
ini_set('error_reporting', E_ALL);

$dir= new directoryIterator(".");
foreach($dir as $file){
	$name=$file->getFilename();
	if($file->isDot()) continue;
	if($file->isDir()){
		
		echo "<h2>".$name."</h2>";
		$dir2=new directoryIterator($name);
		foreach($dir2 as $file2){
			$name2= $file2->getFilename();
			if(!$file2->isDot()){
				echo "<h4 style='background-color:#ececec'>";
				echo $name."/".$name2;	
				echo "</h4>";
				$dir3=new directoryIterator($name."/".$name2);
				foreach($dir3 as $file3){
					if($file3->isDot()) continue;
					$name3= $file3->getFilename();
					echo "<h5 style='color:grey'>";
					echo $name3;
					echo "</h5>";
					
					if(substr($name3,-4)==".rng"){
						echo "<h4>RelaxNG Check</h4><br/>";
						validate( $name."/".$name2."/".$name3);	
					}
					if(substr($name3,-4)==".ng2"){
						echo "<h4>RelaxNG Check including data types</h4><br/>";
						validate( $name."/".$name2."/".$name3);	
					}
					showxml( $name."/".$name2."/".$name3);	
					
				}
			}
		}
	}
}

function validate($path){
	echo "<div style='border:1px solid gray;width:300px'>";
	echo $path."<br/>";
	$xml=substr($path,0,-4).".xml";
	echo $xml."<br/>";
	
	ob_start();
	$dom=domDocument::load($xml);
	$erfolg = $dom->relaxNGValidate($path);
	$fehler = ob_get_contents();
	ob_end_clean();
	if ($erfolg){
		 echo "<p style='color:green'>RelaxNG ok</p>";
	}else{
		echo "<h4>RelaxNG Fehler</h4>";
		echo "<pre>";
		print_r(error_get_last());
		echo "</pre>";
	}
	echo "</div><br/>";
}

function showxml($path){
	//@$dom=domDocument::load($path);
	$dom = new DOMDocument();
	$dom->preserveWhiteSpace = false;
	@$dom->load($path);
	echo "<div>";
	if($dom->documentElement){
		formatxml($dom->documentElement,0,null);
		if(substr($path,-4)==".xml"){
			echo "<h6>JSON</h6>";
			formatjson($dom);
		}
	}else{
		echo "<pre>";
		$xml=file_get_contents($path);
		echo htmlentities($xml,0);
		echo "</pre>";
	}
	echo "</div>";

}

function formatxml($el,$depth,$namespaceuri){
	$ns="";
//	echo $el->lookupnamespaceURI(NULL);

	if(!($namespaceuri==$el->lookupnamespaceURI(NULL))){
		$ns="<span style='color:purple'> xmlns</span>=<span style='color:red'> '".$el->lookupnamespaceURI(NULL)."'</span> ";
	}
	$namespaceuri=$el->lookupnamespaceURI(NULL);

	$ind=$depth*10;
	echo "<div style='margin-left:{$ind};' >";
	if($el->nodeType==1){
		if($el->childNodes->length==0){
			echo "&lt;".$el->tagName;
			attrib($el);
			echo "/>";
		}else{
			echo "&lt;".$el->tagName;
			echo $ns;
			attrib($el);
			echo "><br/>";
			foreach($el->childNodes as $child){
				formatxml($child,$depth+1,$namespaceuri);
			}
			echo "&lt;/".$el->tagName.">";
		}
	}
	if($el->nodeType==3){
		echo "<span style='color:red'>".$el->nodeValue."</span><br/>";
	}
	echo "</div>";
}


function formatjson($dom){
	$proc=new XSLTProcessor();
	$proc->importStyleSheet(domDocument::load("xml2json.xslt"));
	$json=$proc->transformToDoc($dom);
	echo "<pre>";
		echo $json->saveHTML();
	echo "</pre>";
}


/*
function formatjson($el,$depth){
	echo "<div style='margin-left:30px'>";
	echo "{";
	echo $el->tagName;
//	echo "<br/>";	
	foreach($el->childNodes as $node){
		if($node->nodeType==1){
			formatjson($node,$dipth++);
		}

	}
	echo "[";
	foreach($el->attributes as $node){
		echo "<div style='margin-left:20px'>";
		echo $node->name.":".$node->value;
		echo ",";
		echo "</div>";
	}
	echo "]";
	echo "}";
	echo "</div>";
}
*/

function attrib($el){
	foreach($el->attributes as $attr){
	echo " <span style='color:blue'>".$attr->name."</span>=<span style='color:green'>'".$attr->value."</span>'";
	}
}




?>
