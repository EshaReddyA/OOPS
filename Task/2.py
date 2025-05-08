# from multiprocessing import Process

# def cube(n):
#     print(f"The cube of {n} is {n ** 3}")

# if __name__ == "__main__":
#     processes = []

#     for i in range(1, 101):
#         p = Process(target=cube, args=(i,))
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()
# from multiprocessing import Pool

# def cube(n):
#     return f"The cube of {n} is {n ** 3}"

# if __name__ == "__main__":
#     with Pool() as p:
#         r = p.map(cube, range(1, 101))

#     for result in r:
#         print(result)
# from memory_profiler import profile

# @profile
# def cube():
#     for n in range(1, 101):
#         result = n ** 3
#         print(f"The cube of {n} is {result}")

# if __name__ == "__main__":
#     cube()


