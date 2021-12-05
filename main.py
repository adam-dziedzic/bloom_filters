from bloom_filter import BloomFilter


def main():
    items_count = 20  # number of items to add
    fp_prob = 0.02  # false positive probability

    bloomfilter = BloomFilter(items_count=items_count, fp_prob=fp_prob)

    print(f"Size of bit array: {bloomfilter.size}.")
    print(f"False positive Probability: {bloomfilter.fp_prob}.")
    print(f"Number of hash functions: {bloomfilter.hash_count}.")

    # words to be added
    word_present = [
        'abound', 'abounds', 'abundance', 'abundant', 'adam',
        'bloom', 'blossom', 'bolster', 'bonny', 'bonus',
        'bonuses', 'coherent', 'cohesive', 'colorful', 'comely',
        'comfort', 'gems', 'generosity', 'generous', 'generously'
    ]

    # words not added
    word_absent = ['humanity', 'hurt', 'melbourne', 'gloomy', 'australia']

    for item in word_present:
        bloomfilter.add(item)

    test_words = word_present[:10] + word_absent
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
