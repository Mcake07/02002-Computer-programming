def popularity(social_network, person_name):
    outgoing = social_network[person_name]
    incoming = []
    mutual = []
    for name, friends in social_network.items():
        for i in range(len(friends)):
            if friends[i] == person_name:
                incoming.append(name)
    for i in range(len(incoming)):
        if incoming[i] in outgoing:
            mutual.append(incoming[i])
    for name in mutual: 
        outgoing.remove(name)
        incoming.remove(name)
    return len(mutual), len(outgoing), len(incoming), mutual, outgoing, incoming


social_network = {
    "Alice": ["Josefine", "Charlie", "Jakob"],
    "Morten": ["Charlie", "David", "Josefine"],
    "Josefine": ["Alice", "David", "Jakob"],
    "Charlie": ["Alice", "Jakob", "David"],
    "David": ["Josefine"],
    "Jakob": ["Charlie", "Alice", "Josefine", "David"]
}

print(popularity(social_network, 'Charlie'))