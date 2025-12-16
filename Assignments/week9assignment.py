def parse_save_data(save_string, required_keys):
    result = []
    if save_string[-1] != "#":
        return "Error: Corrupt save file."
    for i in range(len(required_keys)):
        if required_keys[i] not in save_string:
            return f"Error: Missing save data: [{required_keys[i]}]"
    save_string = save_string.replace("#", "").split("&")
    for i in range(len(required_keys)):
        for c in save_string:
            if "=" in c:
                key, value = c.split("=")
                if key == required_keys[i]:
                    result.append(value)
    return result

# Test Case 1: Valid save with all fields
save1 = "PLAYER=Kratos&HP=100&XP=4500&MAP=Sparta#"
req1 = ["PLAYER", "HP", "MAP"]
print(parse_save_data(save1, req1))

# Test Case 2: Valid save but missing a key
save2 = "PLAYER=Mario&COINS=50#"
req2 = ["PLAYER", "HP", "COINS"]
print(parse_save_data(save2, req2))

# Test Case 3: Invalid format (missing hash)
save3 = "PLAYER=Link&HEARTS=3"
req3 = ["PLAYER"]
print(parse_save_data(save3, req3))

# Test Case 4: Different order
save4 = "SCORE=99&NAME=PacMan&LIVES=3#"
req4 = ["NAME", "LIVES", "SCORE"]
print(parse_save_data(save4, req4))