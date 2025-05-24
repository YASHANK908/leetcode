/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 int containsChar(const char *word, char ch) {
    while (*word) {
        if (*word == ch) return 1;
        word++;
    }
    return 0;
}
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* result = (int*)malloc(sizeof(int) * wordsSize);   
    int count = 0;

    for (int i = 0; i < wordsSize; i++) {
        char* word = words[i];
        while (*word) {
            if (*word == x) {
                result[count++] = i;   
                break;
            }
            word++;
        }
    }

    *returnSize = count;
    return result;
}