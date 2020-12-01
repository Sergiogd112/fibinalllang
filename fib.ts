function fib(n:number): number{
    let fibarr=[0,1];
    for(let i=2;i<n;i++){
        fibarr[i]=fibarr[i-1]+fibarr[i-2];
    }
    return fibarr[n-1]
}
console.log(fib(40));