# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks,
    # create the output pairs
    # Pirmais elements sākas nekavējoties
    threads = [(0, i) for i in range(n)]
    for i in range(m):
        # Izveido mainīgo "mazākais_thread", lai tas tiktu pievienots kā pirmais sarakstā
        mazākais_thread = threads[0]
        # Ja ir pieejams īsāks laiks, tad to pievieno thread
        for thread in threads:
            if thread[0] < mazākais_thread[0]:
                mazākais_thread = thread
        output.append((mazākais_thread[0], mazākais_thread[1]))
        threads.remove(mazākais_thread)
        laiks = mazākais_thread[0] + data[i]
        threads.append((laiks, mazākais_thread[1]))
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count
    # m - job count
    n, m = map(int, input().split())
    # second line - data
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()