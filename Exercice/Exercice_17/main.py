from math import factorial as f

def list_position(word):
    r = 1

    for index in range(len(word)):
        w = word[index:]
        liste = sorted(list(set(w)))
        freq_letters = [w.count(letter) for letter in liste]

        devide = 1 
        for freq in freq_letters:
            if freq>1:
                devide *= f(freq)

        total_combinaison = f(len(w))//devide

        increment = [0] + [freq * total_combinaison // len(w) for freq in freq_letters[:-1]]
        increment = [sum(increment[:i + 1]) for i in range(len(increment))]

        r+= increment[liste.index(w[0])]
    return r

print(list_position("NPVLZKZRJLMOZYFDFHYSPSAJC"))
