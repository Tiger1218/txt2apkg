import genanki

PATH_BOOK = "F:\\Project\\Books"
import os


def dir_walk(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            pass
            # print("PATH : " + os.path.join(root , dir))
        for file in files:
            # print(dir)
            # print("FILE : " + os.path.join(root , file))
            with open(os.path.join(root, file), 'r', errors="ignore") as f:
            # with open(os.path.join(root, file), 'r') as f:
                print(file + "PROCESS START")
                content = f.read()
                # print(content)
                anki_proc(file , dir , content)
                # print(content)
                print(file + "PROCESS FINISH")


def anki_proc(file_name, dir_name, book_content):
    my_model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': file_name,
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])
    my_note = genanki.Note(
        model=my_model,
        fields=[file_name, book_content])
    my_deck = genanki.Deck(
        2059400110,
        dir_name)

    my_deck.add_note(my_note)
    genanki.Package(my_deck).write_to_file(file_name + ".apkg")


dir_walk(PATH_BOOK)
'''
with open('1985-宇宙坍缩.txt','r',encoding='utf-8') as f:
  content = f.read()
my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': '宇宙坍缩',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])
my_note = genanki.Note(
  model=my_model,
  fields=['宇宙坍缩',content])
my_deck = genanki.Deck(
  2059400110,
  '刘慈欣作品集')

my_deck.add_note(my_note)
genanki.Package(my_deck).write_to_file('宇宙坍缩.apkg')
'''
