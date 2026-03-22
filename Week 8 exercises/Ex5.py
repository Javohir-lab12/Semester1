def parse_markdown(text):
    formatted_text = text.split()
    for i in range(len(formatted_text)):
        if "**" in formatted_text[i]:
            formatted_text[i] = formatted_text[i].replace("**","")
            formatted_text[i] = f"<b>{formatted_text[i]}</b>"
        if "_" in formatted_text[i]:
            formatted_text[i] = formatted_text[i].replace("**","")
            formatted_text[i] = f"<i>{formatted_text[i]}</i>"
    return " ".join(formatted_text)


print(parse_markdown("This is **bold** text."))
print(parse_markdown("Hello _world_."))
print(parse_markdown("Make **this** bold and _this_ italic."))
print(parse_markdown("No formatting here."))
print(parse_markdown("**Bold** at start."))