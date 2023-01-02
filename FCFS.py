import matplotlib.pyplot as plt
import numpy as np

fig, gnt = plt.subplots()
gnt.set_ylim(0, 40)
gnt.set_xlim(0, 60)
gnt.set_xlabel('seconds since start')
gnt.set_ylabel('Processor with different color')
# Setting ticks on y-axis
gnt.set_yticks([10])
# Labelling tickes of y-axis
gnt.set_yticklabels(['1'])
gnt.grid(True)


# Calculate the waiting time
def findWaitingTime(processes, n,bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

# Calculate turn_around time
def findTurnAroundTime(processes, n,bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n,bt, wt, tat)
    print("Processes Burst time " +
          " Waiting time " +
          " Turn around time")

    # Calculate total waiting time
    # and total turn around time
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
              str(bt[i]) + "\t " +
              str(wt[i]) + "\t\t " +
              str(tat[i]))
        for j in range(n):
            col = (np.random.random(), np.random.random(), np.random.random())
            total_wt = total_wt + wt[j]
            total_tat = total_tat + tat[j]
            gnt.broken_barh([(wt[j], (bt[j]))], (j, 9), facecolors=col)

    print("Average waiting time = " +
          str(total_wt / n))
    print("Average turn around time = " +
          str(total_tat / n))
    plt.show()


if __name__ == "__main__":
    processes = []
    burst_time = []
    m = int(input("enter the number of processes :"))

    for i in range(0,m):
        ele=int(input("enter the processes :"))
        processes.append(ele)
        ele1=int(input("enter the burst time :"))
        burst_time.append(ele1)

    n = len(processes)
    findavgTime(processes, n, burst_time)


