import spacy # https://spacy.io/usage
nlp = spacy.load("en_core_web_lg") # python -m spacy download en_core_web_lg
#nlp = spacy.load("en_core_web_md")
import nltk # https://www.nltk.org/install.html
nltk.download('punkt')
def break_into_verses(paragraph):
    verses = nltk.sent_tokenize(paragraph)
    return verses

#Setup
inputPar = "When your legs don't work like they used to before. And I can't sweep you off of your feet. Will your mouth still remember the taste of my love. Will your eyes still smile from your cheeks And darling I will be loving you 'til we're 70. And baby my heart could still fall as hard at 23. And I'm thinking 'bout how people fall in love in mysterious ways. Maybe just the touch of a hand. Oh me I fall in love with you every single day. And I just wanna tell you I am. So honey now. Take me into your loving arms. Kiss me under the light of a thousand stars. Place your head on my beating heart. I'm thinking out loud. Maybe we found love right where we are. When my hair's all but gone and my memory fades. And the crowds don't remember my name. When my hands don't play the strings the same way, mm. I know you will still love me the same. 'Cause honey your soul can never grow old, it's evergreen. Baby your smile's forever in my mind and memory. I'm thinking 'bout how people fall in love in mysterious ways. Maybe it's all part of a plan. I'll just keep on making the same mistakes. Hoping that you'll understand. But baby now. Take me into your loving arms. Kiss me under the light of a thousand stars. Place your head on my beating heart. I'm thinking out loud. That maybe we found love right where we are, oh. So baby now. Take me into your loving arms. Kiss me under the light of a thousand stars. Oh darling, place your head on my beating heart. I'm thinking out loud. That maybe we found love right where we are. Oh baby, we found love right where we are (maybe). And we found love right where we are."
verses = break_into_verses(inputPar)
comparisonVerses = "I've been really tryin', baby. Tryin' to hold back this feeling for so long. And if you feel like I feel, baby. Then, c'mon, oh, c'mon, whoa. Let's get it on. Ah, baby, let's get it on. Let's love, baby. Let's get it on, sugar. Let's get it on, woo hoo. We're all sensitive people. With so much to give. Understand me, sugar (ooh ooh). Since we've got to be here. Let's live. I love you. There's nothing wrong with me. Loving you, baby no no. And giving yourself to me can never be wrong. If the love is true, oh baby. Ooh don't you know how sweet and wonderful life can be ooh (let me love you). I'm asking you baby to get it on with me ooh ooh (let me love you). I ain't gonna worry (let me love you). I ain't gonna push, won't push you baby (let me love you). So c'mon, c'mon, c'mon, c'mon, c'mon, baby. Stop beatin' 'round the bush, hey. Let's get it on (ooh ooh). Let's get it on (ooh ooh). You know what I'm talkin' 'bout. C'mon, baby, hey, hey. Let your love come out. If you believe in love. Let's get it on, ooh. Let's get it on, baby. This minute, oh yeah. Let's get it on. Please, please get it on. I know and you know what I've been dreaming of, don't you baby? (ah, ah, ah, ah). My whole body makes that feelin' of love, I'm happy (my body wants ya, my body wants ya). I ain't gonna worry, no I ain't gonna push (ah). I won't push you baby, woo (ah ah). C'mon, c'mon, c'mon, c'mon, c'mon, darlin'. Stop beatin' 'round the bush. Oh, gonna get it on (ooh, ooh). Threatenin' you, baby (ooh, ooh). I wanna get it on (ooh, ooh). You don't have to worry that it's wrong (ooh, ooh). If the spirit moves ya (ooh, ooh). Let me groove ya good (ooh, ooh). Let your love come down (ooh, ooh). Oh, get it on. C'mon, baby (ooh, ooh). Do you know the meaning? (ooh, ooh). I've been sanctified (ooh, ooh), hey hey. Girl, you give me good feeling (ooh, ooh) (so good). So good, somethin' like sanctified (ooh, ooh). Oh dear I, baby (ooh, ooh). Nothing wrong with love (ooh, ooh). If you want to love me just let your self go (ooh, ooh). Oh baby, let's get it on (ooh, ooh)."
compVerses = break_into_verses(comparisonVerses)


i=0
numbering=1
while(i<=(len(verses)-1)):
    w3 = verses[i]
    w3=nlp(w3)
    j=0
    while(j<=(len(compVerses)-1)):
        w4 = compVerses[j]
        w4=nlp(w4)
        if((w3.similarity(w4))>=.90):
            print(numbering , ". ")
            print("Score: ", (w3.similarity(w4)*100))
            print(w3)
            print(w4)
            print("--------------------------------",'\n')
            numbering+=1
        j+=1
    i+=1
print("done")