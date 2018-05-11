while True:
    sentence = input()
    if not sentence: break
    for i in '.,:;?!()\'"`':
        sentence = sentence.replace(i, '')
    max_len = max(len(word) for word in sentence.split())
    if max_len < 18:
        print('toktobolotov')
    else:
        print('не более 10 букв')
