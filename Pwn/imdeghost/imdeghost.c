#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>

#include <unistd.h>
#include <seccomp.h>
#include <sys/types.h>


char *stk, *exe;
char code[] = "I\x89\xffH1\xc0H1\xdbH1\xc9H1\xd2H1\xffH1\xf6H1\xedM1\xc0M1\xc9M1\xd2M1\xdbM1\xe4M1\xedM1\xf6H\xbc\x00\x00\x00\x00i\x00\x00\x00I\xc7\xc6\x03\x00\x00\x00I\xff\xceL\x89\xf7H\xc7\xc0\x03\x00\x00\x00\x0f\x05M\x85\xf6u\xecL\x89\xf8\xc3";

void security(){
        scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_ALLOW);

	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(mmap), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(mprotect), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(mmap), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(remap_file_pages), 0);
	seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(pkey_mprotect), 0);

        seccomp_load(ctx);
}


int main(){
	setbuf(stdout, 0x0);
        setbuf(stderr, 0x0);
	
	puts("You only see a ghost for a second, what was once there disappears in an instant, like a quick breeze in a still autumn forest.");
	puts("Many people will say it was never there, but cherish your encounter, for you will not be seeing it again.");

	stk = mmap((void *)0x6900000000, 0x1000, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0x0);
	exe = mmap((void *)0x133700000000, 0x1000, PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0x0);

	int x = read(0x0, stk, 0x1000) & 0xff;

	memcpy(exe, code, sizeof(code));
	mprotect(exe, 0x1000, PROT_EXEC);

	security();

	puts("Boo.");

	((void (*)())exe)(x);	
	
	return 0;	
}
