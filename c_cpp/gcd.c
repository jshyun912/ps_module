// 유클리드 

#define ll long long

ll GCD(ll a, ll b)
{
    ll temp;

    while (b > 0)
    {
        temp = a;
        a = b;
        b = temp % b;
    }

    return a;
}

int GCD(int a, int b)
{
    int temp;

    while (b > 0)
    {
        temp = a;
        a = b;
        b = temp % b;
    }

    return a;
}
