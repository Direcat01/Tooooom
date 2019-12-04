from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

laps = 0

if rank == 0:
    laps = input("input the number of laps:")
    laps = int(laps)
    token = 0
    
for i in range(laps):
    if rank == 0:
        print("Lap number {} and token is {}".format(i+1, token))
        token += 100
        comm.send(token, dest=1)
        token = comm.recv(source=size-1)
        printf("Token after lap number {} is  {}".format(i+1, token));
    else:
        token = -888
        token = comm.recv(source=rank-1)
        token += 100
        comm.send(token, dest=(rank+1)%size)
        
        

