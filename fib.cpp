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
