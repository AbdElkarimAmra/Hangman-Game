"""=========================================
Macalester Hangman Game
Authors: Aram Petrosyan and Karim Amra
"""

#-------------------
#IMPORT STATEMENTS
import tkinter as tk
import random
from imageTools import *
easy_dict1 = {"volleyball":["Sport with a net and a ball", "Bump, set, spike!", "Beach or indoor activity", "Six players on each side"],
             "soccer":["Global ball game", "Goalposts and a net", "No hands allowed!", "Played with eleven players on each side"],
             "basketball":["Dribbling and shooting", "Slam dunks and layups", "Hoops and a round ball", "Played with 5 players on each side"]}

easy_dict3 = {"volleyball":["Sport with a net and a ball", "Bump, set, spike!", "Beach or indoor activity", "Six players on each side"],
             "soccer":["Global ball game", "Goalposts and a net", "No hands allowed!", "Played with eleven players on each side"],
             "basketball":["Dribbling and shooting", "Slam dunks and layups", "Hoops and a round ball", "Played with 5 players on each side"]}
easy_dict4 = {"volleyball":["Sport with a net and a ball", "Bump, set, spike!", "Beach or indoor activity", "Six players on each side"],
             "soccer":["Global ball game", "Goalposts and a net", "No hands allowed!", "Played with eleven players on each side"],
             "basketball":["Dribbling and shooting", "Slam dunks and layups", "Hoops and a round ball", "Played with 5 players on each side"]}
easy_dict5 = {"volleyball":["Sport with a net and a ball", "Bump, set, spike!", "Beach or indoor activity", "Six players on each side"],
             "soccer":["Global ball game", "Goalposts and a net", "No hands allowed!", "Played with eleven players on each side"],
             "basketball":["Dribbling and shooting", "Slam dunks and layups", "Hoops and a round ball", "Played with 5 players on each side"]}

countries_dict = {
    'Botswana': [
        'Home to the Kalahari Desert.',
        'Famous for its wildlife and the Okavango Delta.',
        'Landlocked country in Southern Africa.',
        'Gained independence from British colonial rule in 1966.'
    ],
    'Burkina Faso': [
        'Formerly known as Upper Volta.',
        'Capital is Ouagadougou.',
        'Landlocked country in West Africa.',
        'Official language is French.'
    ],
    'Burundi': [
        'Located in the African Great Lakes region.',
        'Capital is Bujumbura.',
        'Official languages are Kirundi, French, and English.',
        'Experienced ethnic conflict in the past.'
    ],
    'Cameroon': [
        'Bilingual country (English and French).',
        'Hosted the 2019 Africa Cup of Nations.',
        'Diverse geography, including rainforests and savannas.',
        'Mount Cameroon is the highest point.'
    ],
    'Côte d’Ivoire': [
        'Formerly known as Ivory Coast.',
        'Largest producer of cocoa in the world.',
        'Political capital is Yamoussoukro.',
        'Economic capital is Abidjan.'
    ],
    'Eswatini': [
        'Formerly known as Swaziland.',
        'One of the last absolute monarchies in the world.',
        'Landlocked country in Southern Africa.',
        'Known for its cultural festivals and ceremonies.'
    ],
    'Ethiopia': [
        'The only African country that was never colonized.',
        'Capital is Addis Ababa.',
        'Home to the African Union headquarters.',
        'Cradle of humankind, with archaeological discoveries like Lucy.'
    ],
    'Ghana': [
        'First African country to gain independence from colonial rule.',
        'Known for its rich history and forts along the coast.',
        'Capital is Accra.',
        'Major exporter of gold and cocoa.'
    ],
    'Kenya': [
        'Home to the Maasai Mara National Reserve.',
        'Capital is Nairobi.',
        'The Great Rift Valley runs through the country.',
        'Known for its diverse wildlife, including the Big Five.'
    ],
    'Madagascar': [
        'Island nation in the Indian Ocean.',
        'Unique biodiversity, with many endemic species.',
        'Capital is Antananarivo.',
        'Known for the animated movie with the same name.'
    ],
    'Morocco': [
        'Located in North Africa.',
        'Famous for the city of Marrakech and the Atlas Mountains.',
        'Has a rich history influenced by Berber, Arab, and French cultures.',
        'Known for its vibrant markets and unique cuisine.'
    ],
    'Niger': [
        'Landlocked country in West Africa.',
        'Home to the largest protected area of giraffes in West Africa.',
        'Capital is Niamey.',
        'Economy heavily relies on agriculture and uranium mining.'
    ],
    'Senegal': [
        'Located on the west coast of Africa.',
        'Capital is Dakar.',
        'Known for its music, dance, and vibrant cultural scene.',
        'Former French colony gaining independence in 1960.'
    ],
    'South Africa': [
        'Southernmost country in Africa.',
        'Known for its diverse landscapes, including Table Mountain and Kruger National Park.',
        'Official languages include Afrikaans and English.',
        'Hosted the 2010 FIFA World Cup.'
    ],
    'South Sudan': [
        'Youngest country in the world, gaining independence in 2011.',
        'Capital is Juba.',
        'Experienced a prolonged civil war after independence.',
        'Landlocked country in East-Central Africa.'
    ],
    'Tanzania': [
        'Located in East Africa.',
        'Home to Mount Kilimanjaro, the highest peak in Africa.',
        'Capital is Dodoma, with Dar es Salaam being the largest city.',
        'Famous for its wildlife and the Serengeti National Park.'
    ],
    'Togo': [
        'Located in West Africa.',
        'Capital is Lomé.',
        'Former French colony gaining independence in 1960.',
        'Known for its palm-lined beaches and hilltop villages.'
    ],
    'Zambia': [
        'Landlocked country in Southern Africa.',
        'Home to Victoria Falls, one of the largest waterfalls in the world.',
        'Capital is Lusaka.',
        'Formerly known as Northern Rhodesia.'
    ],
'Zimbabwe': [
        'Landlocked country in Southern Africa.',
        'Capital is Harare.',
        'Formerly known as Rhodesia.',
        'Known for Victoria Falls and Hwange National Park.'
    ],
    'Bolivia': [
        'Landlocked country in South America.',
        'Capital is Sucre, while the seat of government is La Paz.',
        'Home to the Salar de Uyuni, the world’s largest salt flat.',
        "Named after Simón Bolívar, a leader in South America's independence movement."
    ],
    'Canada': [
        'Second-largest country in the world by land area.',
        'Capital is Ottawa.',
        'Official languages are English and French.',
        'Known for its diverse landscapes, including the Rocky Mountains and Niagara Falls.'
    ],
    'Chile': [
        'Long and narrow country in South America.',
        'Capital is Santiago.',
        'Home to the Atacama Desert, one of the driest places on Earth.',
        'Famous for Easter Island and the Andes Mountains.'
    ],
    'Colombia': [
        'Located in South America.',
        'Capital is Bogotá.',
        'Known for its diverse landscapes, including the Amazon rainforest.',
        'Famous for coffee production and the city of Medellín.'
    ],
    'Ecuador': [
        'Located on the equator in South America.',
        'Capital is Quito.',
        'Galápagos Islands, known for unique wildlife, are part of Ecuador.',
        'Official currency is the U.S. dollar.'
    ],
    'El Salvador': [
        'Smallest and most densely populated country in Central America.',
        'Capital is San Salvador.',
        'Official language is Spanish.',
        'Experienced a civil war from 1979 to 1992.'
    ],
    'Guatemala': [
        'Located in Central America.',
        'Capital is Guatemala City.',
        'Home to ancient Mayan ruins, including Tikal.',
        'Official language is Spanish.'
    ],
    'Honduras': [
        'Located in Central America.',
        'Capital is Tegucigalpa.',
        'Has a Caribbean and a Pacific coastline.',
        'Known for the Mayan archaeological site of Copán.'
    ],
'Mexico': [
        'Located in North America.',
        'Capital is Mexico City.',
        'Known for its rich cultural heritage, including ancient Mayan and Aztec civilizations.',
        'Famous for its cuisine, including tacos, guacamole, and tequila.'
    ],
    'Nicaragua': [
        'Located in Central America.',
        'Capital is Managua.',
        'Largest country in Central America.',
        'Known for its lakes, volcanoes, and diverse ecosystems.'
    ],
    'Paraguay': [
        'Landlocked country in South America.',
        'Capital is Asunción.',
        'Official languages are Spanish and Guaraní.',
        'Known for the Itaipu Dam and the Pantanal, the world’s largest tropical wetland area.'
    ],
    'Peru': [
        'Located in South America.',
        'Capital is Lima.',
        'Home to Machu Picchu, an ancient Incan city.',
        'The Amazon Rainforest extends into eastern Peru.'
    ],
    'Cambodia': [
        'Located in Southeast Asia.',
        'Capital is Phnom Penh.',
        'Home to the Angkor Wat temple complex.',
        'Official religion is Theravada Buddhism.'
    ],
    'China': [
        'The most populous country in the world.',
        'Capital is Beijing.',
        'Home to the Great Wall of China.',
        'Official language is Mandarin.'
    ],
    'Indonesia': [
        'Archipelago consisting of thousands of islands.',
        'Capital is Jakarta.',
        'Home to diverse cultures, languages, and landscapes.',
        'Known for Bali, Komodo dragons, and the Borobudur temple.'
    ],
    'Japan': [
        'Archipelago in East Asia.',
        'Capital is Tokyo.',
        'Known for its advanced technology and traditional arts.',
        'Home to Mount Fuji, an iconic volcano.'
    ],
    'Mongolia': [
        'Landlocked country in East Asia.',
        'Capital is Ulaanbaatar.',
        'Known for vast steppes, Gobi Desert, and nomadic culture.',
        'Historically led by the Mongol Empire under Genghis Khan.'
    ],
'Myanmar': [
        'Located in Southeast Asia.',
        'Capital is Naypyidaw.',
        'Formerly known as Burma.',
        'Home to the temples of Bagan and the Irrawaddy River.'
    ],
    'Philippines': [
        'Archipelago in Southeast Asia.',
        'Capital is Manila.',
        'Known for its beautiful beaches, rice terraces, and volcanoes.',
        'Official languages are Filipino and English.'
    ],
    'Republic of Korea': [
        'Located on the Korean Peninsula in East Asia.',
        'Capital is Seoul.',
        'Divided from North Korea along the 38th parallel.',
        'Home to K-pop, kimchi, and historical palaces.'
    ],
    'Singapore': [
        'City-state and island country in Southeast Asia.',
        'Capital is Singapore City.',
        'Known for its modern skyline and diverse cuisine.',
        "One of the world's major financial and economic hubs."
    ],
    'Taiwan': [
        'Island nation in East Asia.',
        'Capital is Taipei.',
        'Officially known as the Republic of China (ROC).',
        'Economically developed with a strong technology sector.'
    ],
    'Thailand': [
        'Located in Southeast Asia.',
        'Capital is Bangkok.',
        'Known for its vibrant culture, temples, and tropical beaches.',
        'Formerly known as Siam.'
    ],
    'Vietnam': [
        'Located in Southeast Asia.',
        'Capital is Hanoi.',
        'Known for the Vietnam War and the Cu Chi Tunnels.',
        'Home to the Ha Long Bay and vibrant street markets.'
    ],
'Afghanistan': [
        'Landlocked country in South Asia and Central Asia.',
        'Capital is Kabul.',
        'Known for its rugged mountainous terrain, including the Hindu Kush.',
        'Experienced conflicts, including the Soviet-Afghan War and the Taliban regime.'
    ],
    'India': [
        'Located in South Asia.',
        'Capital is New Delhi.',
        'The second-most populous country in the world.',
        'Home to diverse cultures, religions, and the Himalayan mountain range.'
    ],
    'Iran': [
        'Located in the Middle East and Western Asia.',
        'Capital is Tehran.',
        'Formerly known as Persia.',
        'Rich history, including the Persian Empire and the Islamic Revolution.'
    ],
    'Jordan': [
        'Located in the Middle East.',
        'Capital is Amman.',
        'Home to the ancient city of Petra and the Dead Sea.',
        'Official language is Arabic.'
    ],
    'Lebanon': [
        'Located in the Middle East.',
        'Capital is Beirut.',
        'Known for its diverse cultural influences and historical sites.',
        'Experienced a civil war from 1975 to 1990.'
    ],
    'Nepal': [
        'Landlocked country in South Asia.',
        'Capital is Kathmandu.',
        'Home to Mount Everest, the world’s highest peak.',
        'Officially known as the Federal Democratic Republic of Nepal.'
    ],
    'Pakistan': [
        'Located in South Asia.',
        'Capital is Islamabad.',
        'Formerly part of British India, gained independence in 1947.',
        'Home to the Indus Valley Civilization archaeological sites.'
    ],
    'Palestine': [
        'Region in the Middle East.',
        'Includes the West Bank and Gaza Strip.',
        'Subject to ongoing geopolitical conflicts.',
        'Jerusalem is a significant city in the region.'
    ],
    'Syria': [
        'Located in the Middle East.',
        'Capital is Damascus.',
        'Experienced a civil war starting in 2011.',
        'Home to historical sites like Palmyra and the ancient city of Aleppo.'
    ],
    'Yemen': [
        'Located in the Middle East.',
        'Capital is Sanaa.',
        'Experiencing ongoing conflicts and humanitarian crises.',
        'Historically known as the land of Sheba.'
    ],
'Albania': [
        'Located in Southeast Europe on the Balkan Peninsula.',
        'Capital is Tirana.',
        'Known for its Adriatic and Ionian coastline.',
        'Formerly a communist state, gained independence in 1912.'
    ],
    'Armenia': [
        'Landlocked country in the South Caucasus region of Eurasia.',
        'Capital is Yerevan.',
        "One of the world's oldest countries with a rich cultural heritage.",
        'Historically part of the Soviet Union, gained independence in 1991.'
    ],
    'Bosnia and Herzegovina': [
        'Located in Southeast Europe on the Balkan Peninsula.',
        'Capital is Sarajevo.',
        'Formerly part of Yugoslavia, gained independence in 1992.',
        'Complex ethnic and political history, including the Bosnian War.'
    ],
    'Bulgaria': [
        'Located in Southeast Europe on the Balkan Peninsula.',
        'Capital is Sofia.',
        'Famous for its historical sites, including the Rila Monastery.',
        'Joined the European Union in 2007.'
    ],
    'Croatia': [
        'Located in Southeast Europe on the Adriatic Sea.',
        'Capital is Zagreb.',
        'Known for its coastline, islands, and historic cities like Dubrovnik.',
        'Joined the European Union in 2013.'
    ],
    'France': [
        'Located in Western Europe.',
        'Capital is Paris.',
        'Known for its rich cultural history, cuisine, and landmarks like the Eiffel Tower.',
        'Member of the European Union.'
    ],
    'Germany': [
        'Located in Central Europe.',
        'Capital is Berlin.',
        'Largest economy in Europe.',
        'Known for its history, including the Berlin Wall and World War II.'
    ],
    'Greece': [
        "Located in Southeast Europe on the Balkan Peninsula.",
        'Capital is Athens.',
        'Historically known for ancient Greek civilization and mythology.',
        'Home to famous landmarks like the Acropolis and Parthenon.'
    ],
'Hungary': [
        'Located in Central Europe.',
        'Capital is Budapest.',
        'Famous for the thermal baths along the Danube River.',
        'Home to the historic Buda Castle.'
    ],
    'Italy': [
        'Located in Southern Europe on the Italian Peninsula.',
        'Capital is Rome.',
        'Known for its art, history, and cuisine.',
        'Home to landmarks like the Colosseum, Vatican City, and the Leaning Tower of Pisa.'
    ],
    'Kosovo': [
        'Located in Southeast Europe on the Balkan Peninsula.',
        'Capital is Pristina.',
        'Declared independence from Serbia in 2008.',
        'Subject to ongoing geopolitical discussions.'
    ],
    'Lithuania': [
        'Baltic state in Northeast Europe.',
        'Capital is Vilnius.',
        'Joined the European Union in 2004.',
        'Known for its historical sites, including Trakai Island Castle.'
    ],
    'Netherlands': [
        'Located in Northwestern Europe.',
        'Capital is Amsterdam.',
        'Known for its flat landscape, extensive canal systems, and windmills.',
        'Home to famous artists like Vincent van Gogh and Rembrandt.'
    ],
    'Norway': [
        'Located in Northern Europe on the Scandinavian Peninsula.',
        'Capital is Oslo.',
        'Known for its fjords, mountains, and the Northern Lights.',
        'One of the wealthiest and most developed countries in the world.'
    ],
    'Russia': [
        'Largest country in the world, spanning Eastern Europe and Northern Asia.',
        'Capital is Moscow.',
        'Formerly part of the Soviet Union.',
        'Rich cultural history, including literature, ballet, and classical music.'
    ],
    'Serbia': [
        'Located in Southeast Europe on the Balkan Peninsula.',
        'Capital is Belgrade.',
        'Formerly part of Yugoslavia.',
        'Known for its historical sites, including the Nikola Tesla Museum.'
    ],
    'Slovenia': [
        'Located in Central Europe on the Adriatic Sea.',
        'Capital is Ljubljana.',
        'Joined the European Union in 2004.',
        'Known for its picturesque landscapes, including Lake Bled.'
    ],
'Spain': [
        'Located in Southern Europe on the Iberian Peninsula.',
        'Capital is Madrid.',
        'Known for its diverse cultures, including Flamenco music and dance.',
        'Home to famous landmarks like the Sagrada Família and Alhambra.'
    ],
    'Sweden': [
        'Located in Northern Europe on the Scandinavian Peninsula.',
        'Capital is Stockholm.',
        'Known for its high standard of living and social welfare programs.',
        'Home to the Northern Lights and the archipelago of Stockholm.'
    ],
    'United Kingdom': [
        'Located in Northwestern Europe.',
        'Capital is London.',
        'Comprises four constituent countries: England, Scotland, Wales, and Northern Ireland.',
        'Known for its rich history, monarchy, and cultural contributions, including Shakespeare and The Beatles.'
    ]}

languages_dict = {
    'Arabic': [
        'Official language of many Middle Eastern countries',
        'Written from right to left',
        'Has 28 consonants and 3 vowels',
        'The Quran is written in this language'
    ],
    'Chinese': [
        'Most spoken language in the world',
        'Written using characters and logograms',
        'Tones play a crucial role in distinguishing meaning',
        'Mandarin is the official dialect of this language'
    ],
    'French': [
        'Official language of diplomacy and international organizations',
        'Romance language derived from Latin',
        'Known for its influence on art, philosophy, and science',
        'Has gendered nouns and a system of verb conjugation'
    ],
    'German': [
        'Part of the West Germanic language family',
        'Grammatical cases include nominative, accusative, and dative',
        'Famous for compound words',
        'Influential in literature, philosophy, and science'
    ],
    'Ancient Greek': [
        'Classical language of ancient Greece',
        'Used by philosophers like Aristotle and Plato',
        'Has different dialects, including Attic and Ionic',
        'Important in the development of Western literature and philosophy'
    ],
    'Hebrew': [
        'Ancient Semitic language with a script written right to left',
        'Language of the Hebrew Bible (Old Testament)',
        'Revived in the late 19th century as a spoken language',
        'Has a system of root-based word formation'
    ],
    'Japanese': [
        'Uses three scripts: Kanji, Hiragana, and Katakana',
        'Known for its honorifics and politeness levels',
        'Subject-object-verb word order',
        'Influenced by Chinese and has borrowed many words'
    ],
    'Latin': [
        'Classical language of ancient Rome',
        'Used in science, philosophy, and law during the Roman Empire',
        'Has influenced many modern languages, especially in academia',
        'Ecclesiastical Latin is still used in the Catholic Church'
    ],
    'Portuguese': [
        'Romance language derived from Latin',
        'Official language of Portugal and several countries in South America',
        'Shares similarities with Spanish but distinct in pronunciation',
        'Influenced by Moorish and indigenous languages'
    ],
    'Russian': [
        'Official language of Russia',
        'Uses the Cyrillic alphabet',
        'Has six cases in its grammatical system',
        'Important in literature, music, and space exploration'
    ],
    'Spanish': [
        'Second most spoken language in the world',
        'Romance language with Latin roots',
        'Official language in 21 countries',
        'Known for its regional variations, such as Castilian and Latin American Spanish'
    ]
}






#DATABASE of DICTIONARIES
sports_dict={"volleyball":["Sport with a net and a ball", "Bump, set, spike!", "Beach or indoor activity", "Six players on each side"],
             "soccer":["Global ball game", "Goalposts and a net", "No hands allowed!", "Played with eleven players on each side"],
             "basketball":["Dribbling and shooting", "Slam dunks and layups", "Hoops and a round ball", "Played with 5 players on each side"]}
sports_list=list(sports_dict.keys())

#The hangman itself, FOR NOW IT'S DONE WITH KEYBOARD CHARACTERS
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]




#Defining a class
class hangmanGUI:
    def __init__(self):
        # Initializing guessed letters
        self.guessed_letters = []
        # Initializing mistakes


        # Defining a function for randomly choosing a word
        def choosing_word():
            return random.choice(sports_list)

        self.word = choosing_word()
        self.word_blanks = "_" * len(self.word)

        self.mainWin=tk.Tk()
        self.mainWin.title("Macalester Hangman Game")

        #Label for the title
        titleLabel=tk.Label(self.mainWin,
                            text="Macalester Hangman Game",
                            font="Arial 30 bold",
                            relief=tk.SUNKEN,
                            bd=10)
        titleLabel.grid(row=0, column=0, columnspan=4)

        #Label for showing the hangman
        self.hangmanLabel=tk.Label(self.mainWin,
                              font="Arial 50",
                              text=hangman_art[0],
                              relief=tk.GROOVE,
                              bd=10)
        self.hangmanLabel.grid(row=1, column=0, rowspan=5)


        #Label for showing the word
        self.word_label=tk.Label(self.mainWin,
                            font = "Arial 24",
                            text=self.word_blanks)
        self.word_label.grid(row=1, column=1, columnspan=3)

        self.num_mistakes = 0
        self.updating_hangman(self.num_mistakes)

        #Label for showing description
        desc_label=tk.Label(self.mainWin,
                            font="Arial 16",
                            text="The word could be related to either the library, the campus center or the Olin-Rice building.")
        desc_label.grid(row=2, column=1, columnspan=3)

        #Entry widget
        self.guess_entry=tk.Entry(self.mainWin,
                              font="Arial 24")
        self.guess_entry.grid(row=3, column=1, columnspan=2)

        #Guess button
        self.guess_button = tk.Button(self.mainWin,
                                      text="GUESS",
                                      font="Arial 24",
                                      command=lambda event=None: self.checking(event))
        self.guess_button.grid(row=3, column=2)

        #Label for showing information
        info_label=tk.Label(self.mainWin,
                            font="Arial 16",
                            text="You're playing the game with medium difficulty.\nYou have only 1 attempt left for a mistake.\nYou have one opportunity for a hint.\nClick the button if needed.")
        info_label.grid(row=4, column=1, columnspan=2)

        #Button for the hint
        hint=tk.Button(self.mainWin,
                       font="Arial 24",
                       text="HINT")
        hint.grid(row=4, column=2)
        hint["command"] = self.hintFunction

        #Label for already inputted letters
        self.inputted_letters_label=tk.Label(self.mainWin,
                               font="Arial 16",
                               relief=tk.RIDGE,
                               text=("You have already inputted the following letters: "+str(self.guessed_letters)))
        self.inputted_letters_label.grid(row=5, column=1)

        #Label for validity
        self.validity_label=tk.Label(self.mainWin,
                                text="",
                                font="Arial 16 bold",
                                fg="red")
        self.validity_label.grid(row=6, column=1)

        #Label for result
        self.result_label=tk.Label(self.mainWin,
                                   font="Arial 40")
        self.result_label.grid(row=7, column=1)

        # Splash Screen Pieces
        self.splashScreen = tk.Toplevel(self.mainWin)
        self.splashScreen.title("Welcome to Macalester Hangman Game")
        self.splashScreen["bg"] = "red"

        splashLabel = tk.Label(self.splashScreen, text="Please input the game configuration and then start the game",
                               font="Arial 24 bold", padx=50, pady=50, bg="red")
        splashLabel.grid(row=0, column=0, columnspan=5)

        splashDiffLevel = tk.Label(self.splashScreen, text="Difficulty level:", font="Arial 24 bold", padx=25,
                                   pady=25, bg="red")
        splashDiffLevel.grid(row=1, column=0, rowspan=3)

        easyLevelButton = tk.Button(self.splashScreen, text="Easy", bg="red")
        mediumLevelButton = tk.Button(self.splashScreen, text="Medium", bg="red")
        hardLevelButton = tk.Button(self.splashScreen, text="Hard", bg="red")

        easyLevelButton.grid(row=1, column=1, rowspan=2)
        easyLevelButton["command"] = self.display_easy_level_screen
        mediumLevelButton.grid(row=1, column=2, rowspan=2)
        mediumLevelButton["command"] = self.display_medium_level_screen
        hardLevelButton.grid(row=1, column=3, rowspan=2)
        hardLevelButton["command"] = self.display_hard_level_screen


        #instructions button:

        instructions_button = tk.Button(self.splashScreen, bg="red", text="instructions", width=10)
        instructions_button.grid(row=4, column=4, columnspan=4)
        instructions_button["command"] = self.display_instructions

        manageDictionariesButton = tk.Button(self.splashScreen, bg="red",
                                             text="Click here to manage the dictionaries you will play with")
        manageDictionariesButton.grid(row=4, column=0, pady=10)

        self.selectedDictionaries = ""

        self.displayDictsLabel = tk.Label(self.splashScreen, text="Selected dictionaries: " + self.selectedDictionaries,
                                          font="Arial 24 bold", padx=25, pady=25, bg="red")
        self.displayDictsLabel.grid(row=4, column=1, columnspan=4, pady=(20, 0))

        playButton = tk.Button(self.splashScreen, text="Play Game", width=8, height=4, bg="red")
        playButton["command"] = self.startResponse
        playButton.grid(row=1, column=4, padx=(10, 0), rowspan=2)

        self.mainWin.withdraw()

    # ... (Your existin
    def startResponse(self):
        """Takes no inputs.  Shows the mainWin and hides the splash screen"""
        self.mainWin.deiconify()
        self.splashScreen.withdraw()


    def hintFunction(self, dictionary):
        hints = dictionary[str(self.word)]
        random_hint = random.choice(hints)


    def display_instructions(self):
        instructions_window = tk.Toplevel(self.splashScreen)
        instructions_window.title("Instructions")

        instructions_label = tk.Label(instructions_window, text= """
                                        Instructions:
                                        \n
                                        1. Guess the word by entering one letter at a time.
                                        \n
                                        2. You have a limited number of incorrect guesses before the hangman is complete.
                                        \n
                                        3. Pay attention to the hints provided for each word.
                                       \n
                                        4. You can only input one character at a time.
                                        \n
                                        5. Once you've guessed all the letters, you win the game!
                                        \n
                                        6. Be cautious – too many incorrect guesses will result in a loss.
                                        \n
                                        Hint: Click the HINT button during the game for additional clues.
                                        """
                                                                                       ,font="Arial 16")
        instructions_label.grid(row=0, column=0)

    def display_easy_level_screen(self):
        easy_level_window = tk.Toplevel(self.splashScreen)
        easy_level_window.title("Medium Level Dictionaries")

        sports_dict_button = tk.Button(easy_level_window, text="Sports at Macalester", command=self.add_sports_dictionary)
        sports_dict_button.grid(row=0, column=0)

        countries_dict_button = tk.Button(easy_level_window, text="Countries represented at Macalester",
                                          command=self.add_countries_dictionary)
        countries_dict_button.grid(row=0, column=1)

        sports_dict_button = tk.Button(easy_level_window, text="languages offered at Macalester",
                                       command=self.add_languages_dictionary)
        sports_dict_button.grid(row=0, column=2)

        done_button = tk.Button(easy_level_window, text="Done", command=easy_level_window.destroy)
        done_button.grid(row=1, column=0, columnspan=2, pady=10)

    def display_medium_level_screen(self):
        medium_level_window = tk.Toplevel(self.splashScreen)
        medium_level_window.title("Medium Level Dictionaries")

        sports_dict_button = tk.Button(medium_level_window, text="Sports at Macalester",
                                       command=self.add_sports_dictionary)
        sports_dict_button.grid(row=0, column=0)

        countries_dict_button = tk.Button(medium_level_window, text="Countries represented at Macalester",
                                          command=self.add_countries_dictionary)
        countries_dict_button.grid(row=0, column=1)

        languages_dict_button = tk.Button(medium_level_window, text="Languages offered at Macalester",
                                          command=self.add_languages_dictionary)
        languages_dict_button.grid(row=0, column=2)



        done_button = tk.Button(medium_level_window, text="Done", command=medium_level_window.destroy)
        done_button.grid(row=1, column=0, columnspan=2, pady=10)

    def display_hard_level_screen(self):
        hard_level_window = tk.Toplevel(self.splashScreen)
        hard_level_window.title("Hard Level Dictionaries")

        sports_dict_button = tk.Button(hard_level_window, text="Sports at Macalester",
                                       command=self.add_sports_dictionary)
        sports_dict_button.grid(row=0, column=0)

        countries_dict_button = tk.Button(hard_level_window, text="Countries represented at Macalester",
                                          command=self.add_countries_dictionary)
        countries_dict_button.grid(row=0, column=1)

        languages_dict_button = tk.Button(hard_level_window, text="Languages offered at Macalester",
                                          command=self.add_languages_dictionary)
        languages_dict_button.grid(row=0, column=2)

        done_button = tk.Button(hard_level_window, text="Done", command=hard_level_window.destroy)
        done_button.grid(row=1, column=0, columnspan=2, pady=10)

    def add_sports_dictionary(self):
        self.selectedDictionaries += "Sports at Macalester, "
        self.displayDictsLabel.config(text="Selected dictionaries: " + self.selectedDictionaries)

    def add_countries_dictionary(self):
        self.selectedDictionaries += "Countries represented at Macalester, "
        self.displayDictsLabel.config(text="Selected dictionaries: " + self.selectedDictionaries)

    def add_languages_dictionary(self):
        self.selectedDictionaries += "languages offered at Macalester, "
        self.displayDictsLabel.config(text="Selected dictionaries: " + self.selectedDictionaries)

    #Defining a function to update the hangman display
    def updating_hangman(self, mistakes):
        self.hangmanLabel.config(text=hangman_art[mistakes])


    #Creating a function to check the validity of the user's input
    def validInput(self):
        if len(self.guess_entry.get())>1:
            respond_text="You can only input one character!"
            self.validity_label.config(text=respond_text)
            self.guess_entry.delete(0, tk.END)
            vallid=False
        elif self.guess_entry.get()=="":
            respond_text = "You haven't inputted anything! Input something before clicking the button"
            self.validity_label.config(text=respond_text)
            self.guess_entry.delete(0, tk.END)
            vallid = False
        elif self.guess_entry.get() in self.guessed_letters:
            respond_text = "You have already tried this letter. Try something else!"
            self.validity_label.config(text=respond_text)
            self.guess_entry.delete(0, tk.END)
            vallid = False
        else:
            vallid=True
            self.validity_label.config(text="")
            self.guess_entry.delete(0, tk.END)
        return vallid

    #Defining a function to check if the letter is in the word or not
    def checking(self, event):
        guess = self.guess_entry.get().lower()
        assert self.validInput() == True
        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    word_blanks = word_blanks[:i] + guess + word_blanks[i + 1:]
            self.word_label.config(text=word_blanks)
            self.guessed_letters.append(guess)
            self.inputted_letters_label.config(text="You have already inputted the following letters" + str(self.guessed_letters))
            if "_" not in word_blanks:
                self.ending("Win")
        else:
            self.guessed_letters.append(guess)
            self.inputted_letters_label.config(text="You have already inputted the following letters" + str(self.guessed_letters))
            global num_mistakes
            num_mistakes += 1
            self.updating_hangman(num_mistakes)
            if num_mistakes == 6:
                self.ending("lose")



    #Defining an ending function
    def ending(self, result):
        if result == "Win":
            result_text="You win the game!"
        else:
            result_text="You lost the game and the word was"+self.word
        self.result_label.config(text=result_text)
        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")


    def go(self):
        """Runs the whole class whenever .go() is called"""
        self.mainWin.mainloop()


#SCRIPT
# if __name__ == '__main__':
#     game=hangmanGUI()
#     game.go()
app = hangmanGUI()
app.go()
