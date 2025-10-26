# def counter_of_pass(func):
#     count = 0
#     def wrapper():
#         result = func()
#         print(result)
#         nonlocal count
#         if result == "p":
#             count += 1
#             if count == 2:
#                 print("you need to move to tie_breaker. ")
#                 print(count)
#                 tie_breaker()
#         else:
#             count = 0
#     return wrapper

