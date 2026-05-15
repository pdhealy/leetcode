from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    dummy_input = ["Hello","World"]
    encoded = solution.encode(dummy_input)
    decoded = solution.decode(encoded)
    print("Encoded:", encoded)
    print("Decoded:", decoded)

    # Example 2:
    
    dummy_input = [""]
    encoded = solution.encode(dummy_input)
    decoded = solution.decode(encoded)
    print("Encoded:", encoded)
    print("Decoded:", decoded)