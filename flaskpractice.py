# [ ] Print each word in the quote on a new line
quote = "they stumble who run fast"
start = 0
space_index = quote.find(" ")

while space_index != -1:
    print(quote[start:space_index])
    start = space_index + 1
    space_index = quote.find(" ", space_index + 1)
