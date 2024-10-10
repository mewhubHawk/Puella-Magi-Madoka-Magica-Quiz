# 'quiz' is a list of dictionaries
# each dictionary contains the 'question' & 'answer' and the interaction with the user
quiz = [
  {'question': "what is Miki Sayaka's Witch name",
   'answer':"Oktavia von Seckendorff or ",
   'snarky':"I dont blame you for not knowing not many people know",
   'funfact':"all of the magical girls in the series have a witch name!! and by looking at their labrynth you can know all about their life and everything about them madoka magica has lots of depth 💗💗💗💗 you should look into it!!!"  
  },
  {'question':"what is the episode kyoko sakura confess to sayaka",
   'answer':"episode 9 or 9 or ep 9 or episode nine or ep nine or nine",
   'snarky':'how do you not know this it was MASSIVE!!',
   'funfact': "Yes!!! she said sayaka reminded her of why she became a magical girl; because she loved stories where love and courage prevail SAYING SHE LOVES MIKI SAYAKA!!!"
  },
  {'question': "is puella magi madoka magica lgbtq+",
   'answer': "yes or yes duh or ye or yeah or yup or yez or yuz or si or ya or yes ofc or ofc or duh or yes i have in fact watched it or YES!!! or yess!!",
   'snarky':'have you even watched it???',
  'funfact': "Puella Magi Madoka Magica is an angsty Magical Girl show with an Improbably Female Cast, has quite blatant homosexual implications \n some even call it 'Miserable Lesbians: The Anime'\n"
  },
  {'question': "how many episodes of the main series are there",
   'answer': "12 episodes or 12 or twelve or twelve episodes or 12 eps or twelve eps",
   'snarky':'',
  'funfact': "12 episodes of the main series then 3 films and the side series has 3 seasons, the side series has 25 episodes in total\n"
  },
  {'question': "how many books were there as of 2020 (2 yrs ago)",
   'answer': "11 or eleven or 11 books or eleven books",
   'snarky':'hmm this ones kind of hard so I dont blame you',
  'funfact': "There is the main Puella Magi Madoka Magica manga, which should be read first. It also takes the form of an anime and two movies. The two movies have the same content as the anime. \n Then there is the Rebellion manga, also a movie. I'd suggest watching the movie, though the manga is probably cheaper.\nThere also is a variety of spin-offs; I'll put them in the order of how relevant and good I think they are.\n-Tamura Magica (The only comedic one, with relatively good art and related to the main plot.)\n-Oriko Magica (Though it has the worst art, it has objectively the best plot and includes the original pmmm characters.)\n-Sadness Prayer (A spin-off of Oriko Magica, featuring the characters shown within and some others. It\'s a prequel.)\n-Oriko Magica: Extra Story (Another spin-off featuring the Oriko characters. It's quite good as well.)\n-Tart Magica (It features Jeanne D' Arc as a magical girl, and quite possibly has the best art.)\n-Suzune Magica (Honestly one of my favorites, but it does have a lot of flaws. Still, I think it's the closest to Pmmm in the idea.)\n-Kazumi Magica (There are so many characters that it becomes a bit confusing to keep track of them, but it's still good. It has the most fanservice.)\n\nBesides the adaptation of the TV series and Rebellion, there’s only three series that feature the original characters in prominent positions.\nThere’s Oriko, and it’s spinoffs, which the other comment already explained. The plot is known to be fairly good, but as stated, the art is bad enough that it turns some people off from the story entirely.\nThen there’s the Wraith Arc, which explains what happens in between the TV show and Rebellion. This means that Homura, Kyouko, and Mami are featured heavily. I would consider this actually pretty important to the overall story.\nIt unfortunately doesn’t have an official translation but you can find an unofficial one quite easily online.\nLast is the Different Story. This one is often considered to be the best of them. It starts with the story of how Kyouko and Mami once knew each other, and then turns into an alternate timeline where Mami survives Charlotte.\nAdds quite a bit of character development to the two characters with the least screen time. Also manages to play with your feelings just like the original series. Highly recommended.\nThe other comment talks about which spinoffs don’t have the original characters, so I won’t get into that.\n"
  },
  {'question': "when's film 4 of pmmm coming out?",
   'answer': "no release date currently or no one knows or idk or hasnt been confirmed",
   'snarky':'aaaaaaaaaaa why cant they give us a release date T-T\n',
  'funfact': "On 25th April 2021, during the 10th anniversary event of the Madoka Magica franchise, news of a sequel to the 2013 movie Rebellion was announced\n"
  },
   {'question': "what is kyubeys true name?",
   'answer': "Incubator",
   'snarky':'how did you manage to get it wrong??? have you watched it...\n',
  'funfact':"they came to earth and caused humans to evolve so they could collect humans emotional energy to stop entropy and staving off the heat death of the universe. He can grant any wish to a certain girl, on the condition that she become a magical girl and fight against witches. It is later revealed that their true identity is Incubator (インキュベーター, Inkyubētā) Kyubey is considered the main villain of the Puella Magi Madoka Magica series, as they tricked Madoka Kaname and the other protagonists in order to turn them into magical girls and, later on, into witches.\n"
  },
     {'question': "What is Madoka's witch name?",
   'answer': "Kriemhild Gretchen",
   'snarky':'not well known dw!\n',
  'funfact':"\n"
  }
]

score = 0

for quiz_question in quiz:
    response = input(f'{quiz_question["question"]} ?\n---> ').lower()
    answers = quiz_question["answer"].lower().split(" or ")
  
    if response not in answers:
        print(f'No, the answer to {quiz_question["question"]} is {answers[0]}')
        print(f'{quiz_question["snarky"]}\n')
    else:
        print("Correct!!!\n")
        score += 1
        print(f'{quiz_question["funfact"]}\n')

print(f'You got {score} out of {quiz.__len__()}!')