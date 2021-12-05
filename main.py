from bloom_filter import BloomFilter
from random import shuffle


def main():
    n = 20  # number of items to add
    p = 0.02  # false positive probability

    bloomfilter = BloomFilter(n, p)
    print(f"Size of bit array:{bloomfilter.size}.")
    print(f"False positive Probability:{bloomfilter.fp_prob}.")
    print(f"Number of hash functions:{bloomfilter.hash_count}.")

    # words to be added
    word_present = [
        'abound', 'abounds', 'abundance', 'abundant', 'adam',
        'bloom', 'blossom', 'bolster', 'bonny', 'bonus',
        'bonuses', 'coherent', 'cohesive', 'colorful', 'comely',
        'comfort', 'gems', 'generosity', 'generous', 'generously'
    ]

    # words not added
    word_absent = ['bluff', 'cheater', 'hate', 'war', 'humanity',
                   'racism', 'hurt', 'nuke', 'gloomy', 'facebook',
                   'geeksforgeeks', 'twitter']

    for item in word_present:
        bloomfilter.add(item)

    shuffle(word_present)
    shuffle(word_absent)

    test_words = word_present[:10] + word_absent
    shuffle(test_words)
    for word in test_words:
        if bloomfilter.check(word):
            if word in word_absent:
                print(f"'{word}' is a false positive!")
            else:
                print(f"'{word}' is probably present!")
        else:
            print(f"'{word}' is definitely not present!")


if __name__ == "__main__":
    main()
