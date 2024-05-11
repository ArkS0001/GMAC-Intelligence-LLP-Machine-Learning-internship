def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    capitalized_sentence = " ".join(capitalized_words)
    return capitalized_sentence

# Example usage
input_sentence = "hello, world!"
capitalized_output = capitalize_sentence(input_sentence)
print("Original sentence:", input_sentence)
print("Capitalized sentence:", capitalized_output)
