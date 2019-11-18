import re  # regex module from standard library.


def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        # Checks if the current item matches the regex.
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]


if __name__ == '__main__':
    collection = [
        'django_migrations.py',
        'django_admin_log.py',
        'main_generator.py',
        'migrations.py',
        'api_user.doc',
        'user_group.doc',
        'accounts.txt',
    ]

    print(fuzzyfinder('mig', collection))
