from casadi import SX, Function, log1p, sum1, diag, CodeGenerator

from fire import Fire


def main(mem: bool = True, verbose: bool = True):
    x = SX.sym("x")
    y = SX.sym("y", 2, 2)
    f = Function("f", [x, y], [log1p(x) + sum1(diag(y))])

    opts = {
        "main": False,
        "mex": False,
        "with_mem": mem,
        "verbose": verbose,
        "with_header": True,
        "indent": 4,
    }
    C = CodeGenerator("gen", opts)
    C.add(f)
    C.generate()


if __name__ == "__main__":
    Fire(main)
