def recommend_friends(network, user):
    recommend_friends = []
    direct_friends = list(network[user])
    for friend in direct_friends:
        friends_of_a_friend = network[friend]
        friends_of_a_friend = list(friends_of_a_friend)
        for friend1 in friends_of_a_friend:
            if not friend1 == user and not friend1 in recommend_friends:
                recommend_friends.append(friend1)
    return recommend_friends
            
social_graph = {
    "Alice": {"Bob", "Charlie", "David"},
    "Bob": {"Alice", "Eve", "Frank"},
    "Charlie": {"Alice", "Eve"},
    "David": {"Alice"},
    "Eve": {"Bob", "Charlie"},
    "Frank": {"Bob"}
}
print(recommend_friends(social_graph, "Alice"))