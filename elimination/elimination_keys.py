def elimination(text, structure):
    text = text.lower()
    matches = []
    def value_check(i):
        if isinstance(i, dict):
            for x in i.values():
                value_check(x)
        elif isinstance(i, list):
            for y in i:
                if y.lower() in text:
                    matches.append(y)

    value_check(structure)
    return matches