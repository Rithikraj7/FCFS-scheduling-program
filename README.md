# FCFS-scheduling-program

First in, first out (FIFO)- The simplest scheduling algorithm is first come, first served (FCFS), often known as the golden rule. Processes are merely queued using FIFO in the order that they enter the ready queue.

Implementation:
* Input the processes along with their burst time (bt)
* Find waiting time(wt) for all other processes i.e. 
    for process i -> wt[i] = bt[i-1] + wt[i-1] .
* turnaround time = waiting_time + burst_time.
* average waiting time = total_waiting_time / no_of_processes.
*  average turnaround time = total_turn_around_time / no_of_processes.


