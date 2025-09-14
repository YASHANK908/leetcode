class Solution(object):
    def spellchecker(self, wordlist, queries):
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word.lower())

        word_set = set(wordlist)
        case_insensitive_map = {}
        vowel_error_map = {}

        
        for word in wordlist:
            lower_word = word.lower()
            case_insensitive_map.setdefault(lower_word, word)
            vowel_error_map.setdefault(devowel(word), word)

        result = []
        for query in queries:
            if query in word_set:
                result.append(query)
            elif query.lower() in case_insensitive_map:
                result.append(case_insensitive_map[query.lower()])
            elif devowel(query) in vowel_error_map:
                result.append(vowel_error_map[devowel(query)])
            else:
                result.append("")

        return result

        