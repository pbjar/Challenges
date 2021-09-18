1326D  
Rythm

The codeforces grind continues for rainchad. He decided to try a random problem from a global contest, and he was able to pass the system tests. He removed the leaking debug method, but I think his code is still vulnerable. Can you pwn it?

You can find the problem at https://codeforces.com/contest/1326/problem/D2 and his code at https://codeforces.com/contest/1326/submission/128300375. However, because of the long time to send data over netcat, the binary provided will have mxn set to 500 instead of 1000100.

Connect with "nc 143.198.127.103 42003".

Warning: You may need to increase your local stack size limit to run. Also, this may take several minutes to run remotely.

Provided: 1326D, libc-2.31.so, ld-2.31.so
