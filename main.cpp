#include "casadi_mem.h"
#include "gen.h"
#include <stdio.h>

int main() {
  casadi_mem *mem = casadi_alloc(f_functions());
  const double x_val = 1.0;
  const double y_val[4] = {1.0, 2.0, 3.0, 4.0};
  double res;

  mem->arg[0] = &x_val;
  mem->arg[1] = y_val;
  mem->res[0] = &res;

  casadi_eval(mem);

  printf("res = %f\n", res);

  casadi_free(mem);

  return 0;
}
