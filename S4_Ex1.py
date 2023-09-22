import re

email = str(input())
is_match = re.search(r'[A-Za-z0-9]*[A-Za-z]+[A-Za-z0-9]*\@[A-Za-z]+\.[A-Za-z]+', email)

if is_match is not None and is_match.group() == email:
    print('OK')
elif is_match is not None and is_match.group() != email:
    print('WRONG')
elif is_match is None:
    print('WRONG')
