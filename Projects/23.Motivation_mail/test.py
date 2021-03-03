import random
with open("./quotes.docx") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
    print(quote.strip())