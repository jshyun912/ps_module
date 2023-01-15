long long GCD(long long num1, long long num2)
{
	if (num2 == 0)
		return num1;

	return GCD(num2, num1 % num2);
}

ll GCD(ll num1, ll num2)
{
	if (num2 == 0)
		return num1;

	return GCD(num2, num1 % num2);
}

int GCD(int num1, int num2)
{
	if (num2 == 0)
		return num1;

	return GCD(num2, num1 % num2);
}
