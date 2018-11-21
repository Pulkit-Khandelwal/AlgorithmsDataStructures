/*(
fork() cretaes a new process.
fork a new process. We cannot determine which
process will execute first. The code block executes for each of the
process.
The fork() therefore returns twice. If it returns zero then we are in the child process
else it is the parent process.

Usually it is the child process where we write a lot of our code.
getpid() returns the pid of the current process and
getppid() returns pid of the parent process.
*/

#include <unistd.h>
#include <stdio.h>


int main(int argc, char const *argv[]) {
  /* code */

  // PART 1
  int x = 25;
  if (fork() == 0)
  {// 0 is returned for child
    printf(" This is execued by the child process %d \n", ++x);
  }
  else
  {// a non-zeros value is returned for the parent. This non-zero value is the
    // PID of the child process
    printf(" This is execued by the parent process %d\n", --x);
  }
  printf("Exiting with x= %d", x);

  //PART 2
  


  return 0;
}
