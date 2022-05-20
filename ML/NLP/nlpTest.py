from konlpy.tag import Okt
t = Okt()


print(t.nouns('자연어 처리 스타뚜~'))  # ['자연어', '처리', '스타', '뚜']
print(t.morphs('자연어 처리 스타뚜~'))  # ['자연어', '처리', '스타', '뚜', '~']
print(t.pos('자연어 처리 스타뚜~'))  # [('자연어', 'Noun'), ('처리', 'Noun'), ('스타', 'Noun'), ('뚜', 'Noun'), ('~', 'Punctuation')]
