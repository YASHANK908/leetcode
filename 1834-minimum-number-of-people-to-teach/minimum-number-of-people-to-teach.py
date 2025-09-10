from collections import Counter

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        person_languages = [set(langs) for langs in languages]
        no_common = set()
        
        for u, v in friendships:
            if person_languages[u - 1].isdisjoint(person_languages[v - 1]):
                no_common.add(u - 1)
                no_common.add(v - 1)
        
        lang_counter = Counter()
        for person in no_common:
            for lang in person_languages[person]:
                lang_counter[lang] += 1
        
        if lang_counter:
            max_known = max(lang_counter.values())
        else:
            max_known = 0
        
        return len(no_common) - max_known
