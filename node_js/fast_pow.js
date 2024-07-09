let pow = function (a, b, mod) {
    let res = BigInt(1);

    while (b > 0)
    {
        if (b & BigInt(1)) res = (res * a) % mod;

        b >>= BigInt(1);
        a = (a * a) % mod;
    }

    return res;
};
