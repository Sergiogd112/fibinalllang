<?php
$n=40;
$fib = array(0,1,1);
for($i=3;$i<$n;$i++){
    $fib[$i]=$fib[$i-1]+$fib[$i-2];
}
$out=$fib[$n-1];
echo "$out" . "\n";
