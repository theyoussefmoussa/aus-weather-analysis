def separator(title=None, length=50):
    """
    Separator Function to Separate Between Phases in Terminal Visually
    """
    if title:
        print(f"\n{'-' * 10} {title} {'-' * 10}")
    else:
        print('-' * length)