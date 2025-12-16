movies = {
    "Inception": ["Sci-Fi", "Action"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Shrek": ["Animation", "Comedy"],
    "Toy Story": ["Animation", "Family"],
    "Interstellar": ["Sci-Fi", "Drama"]
}
genre_index = {}
for name , genre_list in movies.items():
    for genre in genre_list:
        if genre in genre_index:
            genre_index[genre].append(name)
        else:
            genre_index[genre] = []
            genre_index[genre].append(name)
print(genre_index)