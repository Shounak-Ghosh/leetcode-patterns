def get_rolling_hashes(text, window_length, base=31, modulo=10**9 + 7):
    """
    Generates rolling hash values for all windows of a given length in the text.
    
    :param text: The input string.
    :param window_length: The length of the sliding window.
    :param base: The base (radix) for the polynomial hashing.
    :param modulo: The modulo for hash calculations.
    :return: A generator yielding the hash for each window.
    """
    n = len(text)
    if window_length <= 0 or window_length > n:
        return # No valid windows

    # 1. Pre-calculate the highest power of base: base^(window_length-1) % modulo
    # This is used to remove the contribution of the character leaving the window.
    highest_power = 1
    for _ in range(window_length - 1):
        highest_power = (highest_power * base) % modulo

    # 2. Calculate the hash for the first window
    current_hash = 0
    for i in range(window_length):
        char_val = ord(text[i]) # Get ASCII value
        current_hash = (current_hash * base + char_val) % modulo
    
    yield current_hash # Yield the hash of the first window

    # 3. Roll the hash for subsequent windows
    for i in range(1, n - window_length + 1):
        # Character leaving the window: text[i-1]
        # Character entering the window: text[i + window_length - 1]

        old_char_val = ord(text[i-1])
        new_char_val = ord(text[i + window_length - 1])

        # Remove the contribution of the old character
        # Add modulo to ensure positive result before final modulo, in case subtraction results in negative
        removed_contribution = (old_char_val * highest_power) % modulo
        current_hash = (current_hash - removed_contribution + modulo) % modulo

        # Shift the hash to the left (multiply by base)
        current_hash = (current_hash * base) % modulo

        # Add the contribution of the new character
        current_hash = (current_hash + new_char_val) % modulo
        
        yield current_hash # Yield the hash of the current window

# --- Example Usage ---
if __name__ == "__main__":
    text = "abracadabra"
    window_len = 3
    base = 31
    modulo = 10**9 + 7

    print(f"Text: '{text}', Window Length: {window_len}")
    print(f"Base: {base}, Modulo: {modulo}\n")

    print("Rolling hashes for windows:")
    # Expected hashes for "abr", "bra", "rac", etc.
    # Note: Hash values will depend on base and modulo.
    for i, h in enumerate(get_rolling_hashes(text, window_len, base, modulo)):
        window_start_index = i
        window_end_index = i + window_len
        window_string = text[window_start_index : window_end_index]
        print(f"Window '{window_string}' (index {window_start_index}): Hash = {h}")

    print("\n--- Another Example ---")
    text2 = "banana"
    window_len2 = 3
    print(f"Text: '{text2}', Window Length: {window_len2}")
    for i, h in enumerate(get_rolling_hashes(text2, window_len2)):
        window_string = text2[i : i + window_len2]
        print(f"Window '{window_string}' (index {i}): Hash = {h}")
    # Notice 'ana' (index 1) and 'ana' (index 3) will have the same hash