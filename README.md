# Disk Scheduler
Disk scheduling algorithms with corresponding graphs to visualize disk head movement.

## Overview

A disk scheduler is an operating system functionality that calculates the order that I/O requests need to be serviced as they come onto the disk. This Python program is designed to take in from 2 to 10 cylinder positions from 0 to 199 in order of I/O request as input, and calculate the order in which the requests will be serviced along with the total head movement.

<img src="/img/img1.png" width="400"> <img src="/img/img2.png" width="400">

Four algorithms are performed: First Come First Serve, which services the requests in the exact order as they came; Shortest Seek Time First, which always services the request nearest to the disk head; SCAN, or Elevator, which services requests as the head moves from the first cylinder position to one end, and then the other end; and C-SCAN, which performs as SCAN does, but the head jumps to the other end of the disk once it reaches one end.

The program then uses the turtle library to draw a graph that helps depict the movement of the disk head for each algorithm.

### Example 1

Input: 8 cylinders; positions 50, 82,170, 43, 140, 24, 16, 190

Shell output:

<img src="/img/img4.png" width="400"> 

Turtle output:

<img src="/img/img3.png" width="400">

### Example 2

Input: 10 cylinders; positions 65, 180, 101, 180, 24, 79, 0, 128, 22, 51

Shell output:

<img src="/img/img6.png" width="400">

Turtle output:

<img src="/img/img5.png" width="400">

## Summary

While this program calculates and displays disk head movement, this is not the only factor that matters when selecting a disk scheduling algorithm. Fairness is another issue to element to consider. For instance, Shortest Seek Time First strives for little disk head movement, but in many cases such as Example 2, requests with higher seek times are neglected, leading to starvation. C-SCAN may have larger disk head movement, but wait times for requests are more uniform.

There are other algorithms as well. LOOK and C-LOOK improve upon SCAN and C-SCAN respectively by eliminating the need for the head to travel to the ends of the disk. Random schedulers can in theory be the fairest or the least fair, and are mainly used for testing and analysis. Other algorithms like N-Step SCAN and F-SCAN use multiple buffers and/or queues to make sure newer requests are serviced once earlier ones are completed to avoid starvation.
