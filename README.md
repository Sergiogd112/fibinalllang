# Fibonachi in all Languages

Fibonchay implementation in as many languages as posible

## Done in
- [CPP](fib.cpp)

<<<<<<< HEAD
```cpp
#include <iostream>

using namespace std;

int main()
{
    int n = 40;
    long long int fib[n];
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i < n; i++)
    {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    cout << "Fibonachi of " << n ;
    cout << " with c++ is " << fib[n-1] << endl;
}

```
- [Java](fib.java)

```java
/**
 * fib
 */
public class fib {

    public static void main(String[] args) {
        int n=80;
        long[] fibarr=new long[n];
        fibarr[0]=0;
        fibarr[1]=1;
        for(int i =2;i<n;i++){
            fibarr[i]=fibarr[i-1]+fibarr[i-2];
        }
        System.out.println(fibarr[n-1]);
    }
}
```
- [PHP](fib.php)

```php
<?php
$n=40;
$fib = array(0,1,1);
for($i=3;$i<$n;$i++){
    $fib[$i]=$fib[$i-1]+$fib[$i-2];
}
$out=$fib[$n-1];
echo "$out" . "\n";

```
- [Python](fib.py)

```python
n = 40
print("Fibonachi of", n," with python is ",end='')
fib = [0, 1]
[fib.append(fib[x - 1] + fib[x - 2]) for x in range(2, n)]
print(fib[n-1])
```
- [TypeScript](fib.ts)

```typescript
function fib(n:number): number{
    let fibarr=[0,1];
    for(let i=2;i<n;i++){
        fibarr[i]=fibarr[i-1]+fibarr[i-2];
    }
    return fibarr[n-1]
}
console.log(fib(40));
```

## Missing

- [Bash](fib.h)
- [C](fib.c)
- [Haskell](fib.hs)
- [Scala](fib.scala)
=======
* [C++](fib.cpp)
* [Java](fib.java)
* [PHP](fib.php)
* [Python](fib.py)
* [TypeScript](fib.ts)

## Missing

* [Haskell](fib.hs)
* [Scala]()
* [Lua](fib.lua)
* [Ruby](fib.ru)
* [SQL](fib.sql)
* [Bash](fib.sh)
>>>>>>> 0c9e73475dfe360f06bed7d1f085a021ec24a69b
