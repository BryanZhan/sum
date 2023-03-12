def pri_sum(sum1,sum2):
    result = sum1 + sum2 - sum1 * sum2;
    return result

a=1
b=2
c=3
d=4

e=pri_sum(a,b);
f=pri_sum(b,c);
h=pri_sum(c,d);

print(e,f,h);