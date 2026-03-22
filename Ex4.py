def analyze_trends(tweets, banned_tags):
    temp_dict = {}
    temp_list = []
    hashed_words = []
    for tweet in tweets:
        words = tweet.split()
        hashed_words.append([word for word in words if "#" in word])
# [['#Python', '#coding', '#Life'], ['#coding', '#PYTHON'], ['#life', '#coding'], ['#viral', '#FYP']]
    for words in hashed_words:
        for word in words:
            word = word.lower()
            if word in banned:
                continue
            else:
                if word in temp_dict:
                    temp_dict[word] += 1
                else:
                    temp_dict[word] = 1
    for item, count in temp_dict.items():
        temp_list.append((item, count))
    temp_list.sort()
    return temp_list

tweets = [
    "I love coding! #Python #coding #Life",
    "Just learned #coding and lists in #PYTHON",
    "#life is good but #coding is better",
    "Ignore this #viral #FYP post"
]
banned = {"#viral", "#fyp"}
print(analyze_trends(tweets, banned))