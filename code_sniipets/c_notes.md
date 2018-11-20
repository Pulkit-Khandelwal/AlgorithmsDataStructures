Declare several times but defines just once
Use # include guards to avoid calling several declarations of the same function
Memory allocation for pointers to pointers: using calloc() and malloc()
Storage classes: extern, static, register and auto
Memory leaks can be checked using the Valgrind tool
Always free the dynamically allocated memory to avoid memory leaks
Dynamic memory is allocated during runtime in the heap segment
Volatile variable doesn’t do compiler optimizations



Bo Qing Advanced C++ Videos


Static variables
Within function: retained for entire lifetime LIFETIME
At function level: SCOPE
Static global variable: only inside the file
Static function: function visible only within the file
Static variable only gets initialised once
Extern keyword is used to indicate that the variable is externally defined or initialized


Arrays in C:
Arrays are not first class citizens in C
Arrays cannot be returned from a function
Once arrays are declared they cannot be modified as they are not modifiable lvalue

Structs and Unions
Syntax
Structs can have multiple fields whereas unions cannot have; they have just one field at a time at a specified memory location

Memory layout of C/C++ program:
Text: a.out executable lives here
(Un) initialised variables
Stack: static memory allocation
Heap: dynamic memory allocation
Command line arguments
