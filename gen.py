from casadi import SX, Function, log1p, sum1, diag, CodeGenerator

from fire import Fire


def main(filename: str = "gen", mem: bool = True, verbose: bool = True):
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
    C = CodeGenerator(filename, opts)
    C.add(f)
    C.generate()

    # find all occurences of "#include \"casadi/mem.h\"" in files filename+".c" and filename+".h" and replace them with "#include \"casadi_mem.h\""
    for ext in {".c", ".h"}:
        with open(filename + ext, "r") as f:
            lines = f.readlines()
        with open(filename + ext, "w") as f:
            for line in lines:
                if "casadi/mem.h" in line:
                    line = line.replace("casadi/mem.h", "casadi_mem.h")
                f.write(line)


if __name__ == "__main__":
    Fire(main)
