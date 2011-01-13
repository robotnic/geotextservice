<?php
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
					showxml( $name."/".$name2."/".$name3);	
				}
			}
		}
	}
}

function showxml($path){
	//@$dom=domDocument::load($path);
	$dom = new DOMDocument();
	$dom->preserveWhiteSpace = false;
	@$dom->load($path);
	echo "<div>";
	if($dom->documentElement){
		formatxml($dom->documentElement);
	}else{
		echo "<pre>";
		$xml=file_get_contents($path);
		echo htmlentities($xml,0);
		echo "</pre>";
	}
	echo "</div>";

}

function formatxml($el,$depth){
	$ind=$depth*10;
	echo "<div style='margin-left:{$ind};'>";
	if($el->nodeType==1){
		if($el->childNodes->length==0){
			echo "&lt;".$el->tagName;
			attrib($el);
			echo "/>";
		}else{
			echo "&lt;".$el->tagName;
			attrib($el);
			echo "><br/>";
			foreach($el->childNodes as $child){
				formatxml($child,$depth+1);
			}
			echo "&lt;/".$el->tagName.">";
		}
	}
	if($el->nodeType==3){
		echo "<span style='color:red'>".$el->nodeValue."</span><br/>";
	}
	echo "</div>";
}
function attrib($el){
	foreach($el->attributes as $attr){
	echo " <span style='color:blue'>".$attr->name."</span>=<span style='color:green'>'".$attr->value."</span>'";
	}
}




?>
