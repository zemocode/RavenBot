import pickle

with open("joke_file1.pk1", "rb") as f:
    jokes = pickle.load(f)
with open("joke_title1.txt", "r") as f:
    data = f.readlines()
for joke in data:
    jokes.append(joke.replace("\n", ""))
with open("joke_file1.pk1", "wb") as f:
    pickle.dump(jokes, f)
