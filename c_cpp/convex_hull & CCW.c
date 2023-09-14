typedef struct
{
	int x, y;
}coord;

int ccw(coord a, coord b, coord c)
{
	return (b.x - a.x) * (c.y - b.y) - (b.y - a.y) * (c.x - b.x);
}

int compare(coord* a, coord* b)
{
	if (a->x > b->x)
		return 1;

	if (a->x == b->x)
	{
		if (a->y > b->y)
			return 1;

		if (a->y == b->y)
			return 0;
	}

	return -1;
}

coord* convex_hull(coord* input, int len)
{
	coord up[1005], down[1005];
	static coord output[1005];
	int up_size = 0, down_size = 0;

	qsort(input, len, sizeof(coord), compare);
	
	for (int i = 0; i < len; i++)
	{
		while (up_size >= 2 && ccw(up[up_size - 2], up[up_size - 1], input[i]) >= 0)
			up_size--;

		up[up_size++] = input[i];
	}

	for (int i = len - 1; i >= 0; i--)
	{
		while (down_size >= 2 && ccw(down[down_size - 2], down[down_size - 1], input[i]) >= 0)
			down_size--;

		down[down_size++] = input[i];
	}

	for (int i = 0; i < up_size - 1; i++)
		output[i] = up[i];

	for (int i = up_size - 1; i < up_size + down_size - 2; i++)
		output[i] = down[i - up_size + 1];

	output[up_size + down_size - 2] = (coord){ inf, inf };

	return output;
}
