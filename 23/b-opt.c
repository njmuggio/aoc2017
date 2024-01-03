#include <stdio.h>

long a, b, c, d, e, f, g, h;

#define new

void loop8()
{
#ifndef new
  do
  {
    g = d;
    g *= e;
    g -= b;

    if (g == 0)
    {
      printf("SET F\n");
      f = 0;
    }
    e += 1;
    g = e;
    g -= b;
  } while (g != 0); // jnz g -8
#else
  if (b % d == 0)
  {
    // printf("SET F\n");
    f = 0;
  }
  e = b;
  g = 0;
#endif
}

int main()
{
  a = 1;
  b, c, d, e, f, g, h;
  b = c = d = e = f = g = h = 0;

  b = 79;
  c = b;
  b *= 100;
  b += 100000;
  c = b;
  c += 17000;

  do
  {
    f = 1;
    d = 2;

    do
    {
      e = 2;

      loop8();

      // printf("b=%ld\td=%ld\te=%ld\tf=%ld\tg=%ld\n", b, d, e, f, g);

      d += 1;
      g = d;
      g -= b;
#ifndef new
    // } while (g != 0); // jnz g -13
#else
    } while (g != 0 && f == 1); // jnz g -13
#endif

    // return 0;

    if (f == 0)
    {
      h += 1;
    }

    g = b;
    g -= c;
    if (g == 0)
    {
      break;
    }

    b += 17;
  } while (1); // jnz 1 -23

  printf("%ld\n", h);
}
