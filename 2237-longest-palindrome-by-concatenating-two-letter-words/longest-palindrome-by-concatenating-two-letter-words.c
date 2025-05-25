#define MAX 676
int longestPalindrome(char** words, int wordsSize) {
    int res=0,freq[MAX],center=0,i;
    int index(char *word){
        return (word[0]-'a')*26 +(word[1]-'a');
    }

    for(int i=0;i<wordsSize;i++){
        int id=index(words[i]);
        freq[id]++;
    }
    for(int i=0;i<MAX;i++){
        int a=i/26;
        int b=i%26;
        int revid=b*26+a;
        if(a==b){
            int pairs=freq[i]/2;
            res+=pairs*4;
            if(freq[i]%2==1) center=1;
        }
        else if(i<revid){
            int pairs=freq[i]<freq[revid]?freq[i]:freq[revid];
            res+=pairs*4;
        }
    }
    if(center) res+=2;
    return res;
}