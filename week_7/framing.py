def framing(message, frame_character, important):
    total = (len(message) + 4) * frame_character
    if important:
        total += '\n| ' + message.upper() + ' |'
    else:
        total += '\n| ' + message + ' |'
    total += '\n' + (len(message) + 4) * frame_character
    return total



print(framing('Hullo', '*', False))
print(framing('oi mate', '~', True))