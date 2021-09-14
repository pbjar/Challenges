#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>

int r[8];
long prog_len;
char *prog;
int pc = 0;
int v[2];
int qv[262144];
int ql[262144];
int qr[262144];
int qsum = 0;
int nxtq = 51;
int pl = 50, pr = 49;
int qlen = 0;

void f00(){r[v[0]] = v[1];} // MOV reg0 val
void f01(){r[v[0]] = r[v[1]];} // MOV reg0 reg1
void f02(){pc = prog_len;} // EXIT
void f03(){}
void f04(){}
void f05(){}
void f06(){}
void f07(){}
void f08(){}
void f09(){}
void f0a(){}
void f0b(){}
void f0c(){}
void f0d(){}
void f0e(){}
void f0f(){}
void f10(){r[v[0]] += v[1];} // ADD reg0 val
void f11(){r[v[0]] += r[v[1]];} // ADD reg0 reg1
void f12(){r[v[0]] -= v[1];} // SUB reg0 val
void f13(){r[v[0]] -= r[v[1]];} // SUB reg0 reg1
void f14(){r[v[0]] *= v[1];} // MUL reg0 val
void f15(){r[v[0]] *= r[v[1]];} // MUL reg0 reg1
void f16(){r[v[0]] /= v[1];} // DIV reg0 val
void f17(){r[v[0]] /= r[v[1]];} // DIV reg0 reg1
void f18(){r[v[0]] %= v[1];} // MOD reg0 val
void f19(){r[v[0]] %= r[v[1]];} // MOD reg0 reg1
void f1a(){}
void f1b(){}
void f1c(){}
void f1d(){}
void f1e(){}
void f1f(){}
void f20(){r[v[0]] = ~r[v[0]];} // NOT reg0
void f21(){r[v[0]] &= v[1];} // AND reg0 val
void f22(){r[v[0]] &= r[v[1]];} // AND reg0 reg1
void f23(){r[v[0]] ^= v[1];} // XOR reg0 val
void f24(){r[v[0]] ^= r[v[1]];} // XOR reg0 reg1
void f25(){r[v[0]] |= v[1];} // OR reg0 val
void f26(){r[v[0]] |= r[v[1]];} // OR reg0 reg1
void f27(){}
void f28(){}
void f29(){}
void f2a(){}
void f2b(){}
void f2c(){}
void f2d(){}
void f2e(){}
void f2f(){}
void f30(){r[0] = (r[v[0]] == 0);} // EZ reg0
void f31(){r[0] = (r[v[0]] < 0);} // LZ reg0
void f32(){r[0] = (r[v[0]] > 0);} // GZ reg0
void f33(){}
void f34(){}
void f35(){}
void f36(){}
void f37(){}
void f38(){}
void f39(){}
void f3a(){}
void f3b(){}
void f3c(){}
void f3d(){}
void f3e(){}
void f3f(){}
void f40(){
    for(int i = 0; i < prog_len-1; i++){
        if(prog[i] == 0x60 && prog[i+1] == v[0]){
            pc = i;
            break;
        }
    }
} // JMP val
void f41(){v[0] = r[v[0]]; f40();} // JMP reg0
void f42(){if(r[0]) f40();} // JF val
void f43(){if(r[0]) f41();} // JF reg0
void f44(){}
void f45(){}
void f46(){}
void f47(){}
void f48(){}
void f49(){}
void f4a(){}
void f4b(){}
void f4c(){}
void f4d(){}
void f4e(){}
void f4f(){}
void f50(){
    qv[nxtq] = v[0];
    ql[nxtq] = pr;
    qr[nxtq] = qr[pr];
    ql[qr[pr]] = nxtq;
    qr[pr] = nxtq;
    qsum += qv[nxtq];
    if(!qlen) pl = nxtq;
    qlen++;
    pr = nxtq;
    nxtq++;
} // PUSH val
void f51(){v[0] = r[v[0]]; f50();} // PUSH reg0
void f52(){
    qsum -= qv[pl];
    r[v[0]] = qv[pl];
    qlen--;
    int curql = ql[pl];
    if(pl == pr){
        pr = curql;
    }
    pl = qr[pl];
    ql[pl] = curql;
    qr[curql] = pl;
} // POP reg0
void f53(){r[v[0]] = qv[pl];} // POPN reg0
void f54(){
    for(int i = 0; i < v[0]; i++){
        if(ql[ql[pl]] == -1){
            qv[nxtq] = 0;
            ql[ql[pl]] = nxtq;
            qr[nxtq] = ql[pl];
            nxtq++;
        }
        pl = ql[pl];
        qlen++;
        qsum += qv[pl];
    }
} // EXL val
void f55(){v[0] = r[v[0]]; f54();} // EXL reg0
void f56(){
    for(int i = 0; i < v[0]; i++){
        if(qr[qr[pr]] == -1){
            qv[nxtq] = 0;
            qr[qr[pr]] = nxtq;
            ql[nxtq] = qr[pr];
            nxtq++;
        }
        pr = qr[pr];
        qlen++;
        qsum += qv[pr];
    }
} // EXR val
void f57(){v[0] = r[v[0]]; f56();} // EXR reg0
void f58(){
    for(int i = 0; i < v[0]; i++){
        if(ql[ql[pl]] == -1){
            qv[nxtq] = 0;
            ql[ql[pl]] = nxtq;
            qr[nxtq] = ql[pl];
            nxtq++;
        }
        pl = ql[pl];
        qsum += qv[pl];
        qsum -= qv[pr];
        pr = ql[pr];
    }
} // MVL val
void f59(){v[0] = r[v[0]]; f58();} // MVL reg0
void f5a(){
    for(int i = 0; i < v[0]; i++){
        if(qr[qr[pr]] == -1){
            qv[nxtq] = 0;
            qr[qr[pr]] = nxtq;
            ql[nxtq] = qr[pr];
            nxtq++;
        }
        qsum -= qv[pl];
        pl = qr[pl];
        pr = qr[pr];
        qsum += qv[pr];
    }
} // MVR val
void f5b(){v[0] = r[v[0]]; f5a();} // MVR reg0
void f5c(){r[v[0]] = qlen;} // GLEN reg0
void f5d(){
    while(qlen < v[0]){
        if(qr[qr[pr]] == -1){
            qv[nxtq] = 0;
            qr[qr[pr]] = nxtq;
            ql[nxtq] = qr[pr];
            nxtq++;
        }
        pr = qr[pr];
        qsum += qv[pr];
        qlen++;
    }
    while(qlen > v[0]){
        qsum -= qv[pr];
        qlen--;
        pr = ql[pr];
    }
} // SLEN val
void f5e(){v[0] = r[v[0]]; f5d();} // SLEN reg0
void f5f(){r[v[0]] = qsum;} // QSUM reg0
void f60(){} // LBL val
void f61(){}
void f62(){}
void f63(){}
void f64(){}
void f65(){}
void f66(){}
void f67(){}
void f68(){}
void f69(){}
void f6a(){}
void f6b(){}
void f6c(){}
void f6d(){}
void f6e(){}
void f6f(){}
void f70(){
    char inp[128];
    scanf("%127s", inp);
    int i_len = strlen(inp);
    int s_r = v[0];
    for(int i = 0; i < i_len; i++){
        v[0] = inp[i];
        f50();
    }
    r[s_r] = i_len;
} // IN reg0
void f71(){
    int o_len = r[v[0]];
    for(int i = 0; i < o_len; i++){
        f52();
        printf("%c", r[v[0]]);
    }
} // OUT reg0

void (*f_lookup[])() = {
    f00, f01, f02, f03, f04, f05, f06, f07, f08, f09, f0a, f0b, f0c, f0d, f0e, f0f,
    f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f1a, f1b, f1c, f1d, f1e, f1f,
    f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f2a, f2b, f2c, f2d, f2e, f2f,
    f30, f31, f32, f33, f34, f35, f36, f37, f38, f39, f3a, f3b, f3c, f3d, f3e, f3f,
    f40, f41, f42, f43, f44, f45, f46, f47, f48, f49, f4a, f4b, f4c, f4d, f4e, f4f,
    f50, f51, f52, f53, f54, f55, f56, f57, f58, f59, f5a, f5b, f5c, f5d, f5e, f5f,
    f60, f61, f62, f63, f64, f65, f66, f67, f68, f69, f6a, f6b, f6c, f6d, f6e, f6f,
    f70, f71
};

int argn[] = {
    2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0,
    1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1
};

int main(int argc, char *argv[]){
    if(argc != 2){
        printf("USAGE: %s <file>\n", argv[0]);
        return 1;
    }
    FILE *pfile = fopen(argv[1], "rb");
    if(pfile == NULL){
        printf("Unable to find file: %s\n", argv[1]);
        return 1;
    }
    fseek(pfile, 0, SEEK_END);
    prog_len = ftell(pfile);
    fseek(pfile, 0, SEEK_SET);
    prog = malloc(prog_len+1);
    fread(prog, 1, prog_len, pfile);
    fclose(pfile);
    for(int i = 0; i < 262144; i++) qv[i] = 0, ql[i] = -1, qr[i] = -1;
    qr[pl] = pr;
    ql[pr] = pl;
    while(pc < prog_len){
        int ins = prog[pc++];
        if(ins > 0x71){
            continue;
        }
        for(int i = 0; i < argn[ins]; i++){
            v[i] = prog[pc++];
        }
        (*f_lookup[ins])();
    }
    free(prog);
}
