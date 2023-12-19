# def make_pretty(func):
#     def inner():
#         print("i got decorated")
#         func
#     return inner
# def ordinary ():
#     print("i am ordinary")
# print("ordinary")
# pretty=make_pretty(ordinary)
# print(pretty())

# 2.
# def make_bold(func):
#     def inner(text):
#         result=func(text)
#         return f"<b>{result}<b>"
#     return inner
# @make_bold
# def greet(name):
#     return f"hello,{name}!"
# decorated_greet=greet("joe")
# print(decorated_greet)
