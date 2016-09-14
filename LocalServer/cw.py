"""Count words."""
from operator import itemgetter
def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s
    words = s.split()
    wc = {}
    for w in words:
        if wc.has_key(w):
            wc[w] += 1
        else:
            wc[w] = 1
    wt = [(k,v) for (k,v) in wc.iteritems()]
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    wt = sorted(wt, key = itemgetter(0))
    wt = sorted(wt, key = itemgetter(1), reverse = True)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = [wt[i][0] for i in range(n)]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()

