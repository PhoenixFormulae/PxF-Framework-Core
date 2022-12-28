# System imports

# Library imports

# External imports


def unpack_tuples(to_unpack):
    if not to_unpack:
        return []

    if not isinstance(to_unpack, tuple):
        return to_unpack

    result = []
    for key in to_unpack:
        if isinstance(key, tuple):
            for k in key:
                result.append(k)
        else:
            result.append(key)

    return result


def unpack_tuples_int(to_unpack):
    if not to_unpack:
        return []

    if not isinstance(to_unpack, tuple):
        return [to_unpack]

    result = []
    for key in to_unpack:
        if isinstance(key, tuple):
            for k in key:
                result.append(k)
        else:
            result.append(key)

    return result
