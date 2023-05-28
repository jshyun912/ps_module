typedef struct
{
	int size, max_size, type;
	int* ary;
}vector;

void push_back_vec(vector* a, int b)
{
	if (a->size == a->max_size)
	{
		a->ary = (void*)realloc(a->ary, a->type * a->max_size * 2);
		a->max_size >>= 1;
	}

	a->ary[a->size++] = b;
}

void pop_vec(vector* a)
{
	a->size--;

	if (a->size * 2 == a->max_size)
	{
		a->ary = (void*)realloc(a->ary, a->type * a->max_size / 2);
		a->max_size <<= 1;
	}
}

void init_vec(vector* a, int b)
{
	a->size = 0; a->max_size = 1; a->type = b;
	a->ary = (int*)malloc(a->type);
}

void* top_vec(vector* a)
{
	return a->ary[a->size - 1];
}

void clear_vec(vector* a)
{
	free(a->ary);
}
