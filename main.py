from agent import generate_code

def main():
    print("\n=========================================")
    print("KERNEL - Code Generator (CLI)")
    print("=========================================")
    
    user_prompt = input("What do you want to build today?\n> ")
    
    print("\nGenerating code... (Thinking......)\n")
    
    code_result = generate_code(user_prompt)
    
    print("=========================================")
    print("Generated Code:")
    print("=========================================")
    print(code_result)
    print("\n")


if __name__ == "__main__":
    main()