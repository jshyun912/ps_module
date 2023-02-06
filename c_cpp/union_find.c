// 분리 집합

int N, link[1 << 20], sz[1 << 20];

void reset()
{
	for (int i = 0; i <= N; i++)
	{
		link[i] = i; sz[i] = 1;
	}
}

// 경로 압축

int find(int x)
{
	if (x == link[x])
		return x;

	return link[x] = find(link[x]);
}

// 경로 압축 없음

int find(int x)
{
  while (x != link[x]) x = link[x];
  return x;
}

bool same(int a, int b)
{
	return find(a) == find(b);
}

void united(int a, int b)
{
	a = find(a); b = find(b);
	if (sz[a] < sz[b]) swap(a, b);
	sz[a] += sz[b]; link[b] = a;
}
