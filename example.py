from publish_lib_ghp import Greeting, Operations

def main():
    print("Testing greeting and operations from publish_lib_ghp")
    greeter = Greeting()
    print(greeter.say_hello("Gabriel"))

    ops = Operations()
    result = ops.add(5, 3)
    print(f"5 + 3 = {result}")

if __name__ == "__main__":
    main()