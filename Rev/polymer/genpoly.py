with open("nbs.txt") as f:
    with open("polymer.c", "w") as c:
        c.write("#include <stdio.h>\n#include <unistd.h>\nint main(){\n")
        lines = f.readlines()
        for l in lines:
            c.write("printf(\"" + l[:-1].replace("\"", "\\\"") + "\\n\"); sleep(1);\n")
        c.write("}\n")
