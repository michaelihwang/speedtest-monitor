def restartable(func):
    def wrapper(*args, **kwargs):
        answer = "y"
        while answer == "y":
            func(*args, **kwargs)
            while True:
                answer = input("Restart?\ty/n:")
                if answer in ("y", "n"):
                    break
                else:
                    print("invalid answer")
    return wrapper
