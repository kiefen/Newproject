def word_frequency(text):
    # Normalize text to lowercase
    text = text.lower()

    # Split the text into words
    words = text.split()

    # Count word frequencies
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0 ) + 1

        # Sort by frequency in descending order
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        # Print the results
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")

# Example Usage
input_text = "Hello world hello Python world Python Python"
word_frequency(input_text)