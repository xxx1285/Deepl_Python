import random
import nltk
from nltk.corpus import wordnet
from pattern.en import conjugate, lemma, PRESENT, PAST, PL, SINGULAR
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


title_url = "Kiev hospital"
key_game = "Aviator game"

"""
    Напиши 10 идей  на Английском языке, составленных комментариев с подстановкой темы статьи и ключевого слова {game DSA}. 
    Например:f"I just got through with {title_url}, and wow, it's as gripping as playing {key_game}. 
    The future is now, and both these things prove it!". Коментарии должны быть длинной от 350 до 400 символов на игровую тематику, 
    и на простом человеческом языке с использованием структуры реальных коментарии с Reddit. Используй ключевое слово перед указанием 
    темы статьи. Конечный результат запиши в переменну в виде f строк как например comments_prompt = 
    [f"I just got through with {title_url}, and wow, it's as gripping as playing {key_game}]
"""
comments_prompt = [
    "I just got through with {title_url}, and wow, it's as gripping as playing {key_game}. The future is now, and both these things prove it!",
    "After reading {title_url}, I'm awestruck. Kinda like the first time I played {key_game}. Both are super innovative and open up a whole new world of possibilities.",
    "Diving into {title_url} felt like a journey back in time. Kind of like when I revisit old levels in {key_game}. It's fascinating how much we've progressed!",
    "The article on {title_url} was as eye-opening as the plot twists in {key_game}. Both are so full of surprises, it's impossible to predict what's coming next.",
    "Reading {title_url} was like playing a level of {key_game} that's tough but rewarding. Both require focus and critical thinking, and boy do they keep you on your toes!",
    "Going through {title_url} was as thrilling as winning a tough round of {key_game}. Both are breakthroughs in their own right and it's exciting to see them unfold.",
    "The article {title_url} was as much of an adventure as a marathon session of {key_game}. The mysteries, the challenges – they both just draw you in!",
    "Reading about {title_url} got my brain buzzing, much like the strategic gameplay in {key_game}. Both are thought-provoking and make you look at things from a whole new perspective.",
    "{title_url} was an enlightening read. It's like {key_game} in the way it changes your outlook. They both make you think deeper and question the status quo.",
    "Engaging with {title_url} gave me a sense of thrill akin to when I'm playing {key_game}. Both require strategy, a keen mind, and quick decision-making. It's an adrenaline rush!",
    "{title_url} was such an engrossing read! It's like the joy I feel when I'm playing my favorite game, {key_game}. It's a great way to engage and learn new things, just like in the game!",
    "I just had to share how much I enjoyed reading {title_url}. It made me think about the strategies and decisions I make in {key_game}, just as much as it made me ponder the future of VR.",
    "Reading about {title_url} made me remember the excitement I had when I first played {key_game}. The thrill and competition - both are so addictive!",
    "{title_url} is as fascinating as each level in {key_game}. The ever-changing landscapes and challenges keep me coming back for more!",
    "I just got through with {title_url}, it felt just like mining for resources in {key_game} - intriguing and full of surprises.",
    "I found {title_url} as enlightening as understanding the mechanics of {key_game}. Both require an open mind and a willingness to adapt to new situations.",
    "I'm as drawn to {title_url} as I am to playing {key_game}. Both are complex yet fascinating, offering endless opportunities to learn and grow.",
    "Reading about {title_url}, I couldn't help but reminisce about the immersive universe of {key_game}. Both provide a refreshing escape from reality.",
    "Just like the satisfying achievement of a hard-fought victory in {key_game}, the exploration of {title_url} left me feeling accomplished, having gained new insights.",
    "The in-depth analysis in {title_url} kept me as engaged as the intricate strategies required in {key_game}. It's amazing how technology changes our perspective, be it business or gaming!",
    "Just like a nail-biting match in {key_game}, I found the article {title_url} equally exhilarating. It's fascinating to see how the game strategies can be related to real life scenarios.",
    "While playing {key_game}, I stumbled upon the article {title_url}. The similarity between the game's strategy and the article's insight left me intrigued. Both are so immersive and enlightening.",
    "I found the article {title_url} as engrossing as the gameplay in {key_game}. Both require critical thinking and strategy. It's truly fascinating to see the correlation.",
    "The thrill of playing {key_game} is only paralleled by the insight I gained from the article {title_url}. It's amazing how gaming can be as educational as a well-researched article.",
    "While playing {key_game}, I often find myself applying strategies I learned from articles like {title_url}. The parallels between gaming and real-life scenarios are astounding.",
    "I find the tactical aspect of {key_game} quite similar to the strategic insights from {title_url}. Both make me think and analyze before making decisions.",
    "The compelling strategies of {key_game} often remind me of the depth and complexity of articles like {title_url}. The more I delve into both, the more I learn.",
    "Immersed in {key_game}, I often see myself applying the insights I got from the article {title_url}. The similarities in strategic planning are quite astounding.",
    "The thought process in {key_game} and the insights from {title_url} are surprisingly similar. Both involve thinking ahead and adapting to new challenges.",
    "The strategizing I do while playing {key_game} is complemented by the insights I get from articles like {title_url}. It's a perfect blend of entertainment and learning."
]

# Визначаємо функцію, яка вибирає випадковий коментар та замінює дієслова на їхні синоніми
def replace_synonyms_verbs_in_comments(title_url: str, key_game: str, comments_prompt: list):
    # Вибір випадкового шаблону коментаря
    comment = random.choice(comments_prompt)

    # Заміна значень
    comment = comment.format(title_url=title_url, key_game=key_game)

    words = word_tokenize(comment)
    pos_tags = nltk.pos_tag(words)
    new_sentence = []

    for i, (word, pos) in enumerate(pos_tags):
        if 'V' in pos:  # Якщо це дієслова
            # Шукаємо синоніми дієсловаа
            verb_synonyms = [syn.lemmas()[0].name() for syn in wordnet.synsets(lemma(word), pos='v')]
            if verb_synonyms:
                # Заміна на синонім
                new_verb = random.choice(verb_synonyms)

                # Зберігаємо початковий час дієслова
                if pos == 'VBD':  # минулий час
                    new_verb = conjugate(new_verb, tense=PAST)
                elif pos == 'VBG':  # герундій
                    new_verb = conjugate(new_verb, tense=PRESENT) + "ing"
                elif pos == 'VBN':  # пасивний минулий час
                    new_verb = conjugate(new_verb, tense=PAST, aspect=PERFECTIVE)

                new_sentence.append(new_verb)
            else:
                new_sentence.append(word)
        else:
            new_sentence.append(word)

    return ' '.join(new_sentence)

rerr = replace_synonyms_verbs_in_comments(title_url, key_game, comments_prompt)
print(rerr)