#!/bin/awk -f

BEGIN { s = "" }

$1 ~ /^[a-f0-9]+:$/ \
{
    for (i = 2; i <= NF; i++)
    {
        ans = match($i, /^[a-f0-9]{2}$/)
        if (ans) { s = s "\\x" $i }
    }
}

END { print s }
