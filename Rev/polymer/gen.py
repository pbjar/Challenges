with open("beescript.txt") as f:
    with open("nbs.txt", "w") as wf:
        lines = f.readlines()
        for l in lines:
            s = l.lower().split()
            for i in s:
                if i[:3] == "bee" or i[:5] == "honey" or i[:3] == "fly" or i[:5] == "barry" or i == "i" or i[:4] == "busy" or i[:7] == "vanessa" or i[:6] == "benson" or i[:4] == "adam" or i[:7] == "flayman" or i[:10] == "mooseblood" or i[:10] == "montgomery" or i[:3] == "ken":
                    wf.write("flag{n0t_th3_fl4g_l0l} ")
                else:
                    wf.write(i + " ")
            wf.write("\n")
