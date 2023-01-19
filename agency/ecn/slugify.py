NAME = 'slugify'


def words_to_slug(words):
    slug_dict = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
                 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
                 'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
                 'shch', '', 'y', '', 'e', 'yu', 'ya'
                 ]

    start_index = ord('а')
    slug = ''
    for w in words.lower():
        if 'а' <= w <= 'я':
            slug += slug_dict[ord(w) - start_index]
        elif w == 'ё':
            slug += 'yo'
        elif w in " !?;:.,":
            slug += '-'
        else:
            slug += w
    while slug.count('--'):
        slug = slug.replace('--', '-')
    return slug


