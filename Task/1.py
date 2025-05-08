# from multiprocessing import Process  
# def square(n):
#     print(f"The square of {n} is {n * n}")

# if __name__ == "__main__":
#     processes = []  

#     for i in range(1, 101):
#         p = Process(target=square, args=(i,))
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()

# from multiprocessing import Pool

# def square(n):
#     return f"The square of {n} is {n * n}"

# if __name__ == "__main__":
#     with Pool() as p:
#         r = p.map(square, range(1, 101))

#     for result in r:
#         print(result)
# from memory_profiler import profile

# @profile
# def square():
#     for n in range(1, 101):
#         square = n * n
#         print(f"The square of {n} is {square}")

# if __name__ == "__main__":
#     square()







