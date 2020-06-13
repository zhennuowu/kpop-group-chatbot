"""A collection of function for doing my project."""

#! pip install wikipedia
import wikipedia
import random

answer_group_in = ["don't", 'not']
answer_group_out = 'Well, let me help you to get familiar with one group!'
goodbye_out = ['Bye!', 'See you!', "I'll miss you."]
ending_msg = "Sorry, those are all I know about this group. Come to me when you need \
info about K-pop next time!"

group_and_songs = {'Clazziquai Project':'Blessed', 'The Jadu': 'Ok!Love', 'We Girls': 'We Like', 
                   'KISS.': 'dreams come true', 'M.I.L.K':'With Freshness', 'D1CE': 'Wake up', 
                   'jtL': 'One Night Love', '2NB': 'The First', 'Ariaz': 'Grand Opera',
                   'CB Mass': 'gentleman quality', 'Papaya': 'supergirl', 'UN': 'luna',
                   'TRAX': 'strisce pedonali', 'Chakra': 'Tomato', '5tion': 'Deep Slow',
                   'Jewelry': 'DISCOVERY ONE', 'Epik High': "Don't Hate Me", 'F-iV': 'Girl',
                   'Black Beat': 'Night Fever', 'Isak N Jiyeon': 'Tell Me Baby', 'CIX':'THE SHOW', 
                   'V.O.S': 'beautiful life', 'Leessang': 'ballerino', 'LUV': 'Orange Girl',
                   'MC the Max': 'Pathos Tour Live Album', 'Noel': 'New Beginning',
                   'Shinvi': 'To My Friend', 'Sugar' : 'secrect', 'Big Mama': "It's unique",
                   'Dynamic Duo': 'BAAAM', 'Brown Eyed Soul': 'Brown Eyed Girl', 
                   'Buzz': 'Memorize', 'Paran': 'White love', 'Kara': 'Pandora',
                   'TVXQ': 'OH～Holy Night', 'Take': '1story', 'SG Wannabe': 'My Friend', 
                   'SS501': 'Destination', 'LPG': 'Lucky Girl', "K'Pop": 'Memories',
                   'The Grace': 'One More Chance', '4Minute': 'Hot Issue', 'Verivery': 'VERI-US', 
                   'Gavy NJ': 'The Very First', 'Super Junior': 'Sorry, Sorry', 
                   'SeeYa': 'To My Lover', 'Brown Eyed Girls': 'Abracadabra', 'H&D': 'SOULMATE',
                   'Untouchable': 'Take Out', 'U-KISS': 'New Generation', '1the9': 'Domino', 
                   'Super Junior-K.R.Y.': 'The Night Chicago Died', 'MCND': 'TOP GANG', 
                   'DickPunks': 'VIVA PRIMAVERA', 'Eluphant': 'Hello My Dear', 
                   'Big Bang': 'Fantastic Baby', 'Wonder Girls': 'Tell Me', 'Oneus': 'LAST SONG', 
                   '8eight': 'The Bridge', 'F.T. Island': 'Cheerful Sensibility', 
                   "Girls' Generation": "GIRLS' GENERATION", 'Sunny Hill': 'Love Letter', 
                   'Supernova': '1st Single', 'Tritops': 'Boorish Love', 'Uni.T': 'LINE', 
                   'Super Junior-T': 'ROCK&GO', 'Baby Vox Re.V': 'Never say goodbye', 
                   'T-max': 'Lion Heart', 'Black Pearl': 'Blue Moon', 'Davichi': 'Amaranth', 
                   'Mighty Mouth': 'Mighty Fresh', 'Miss $': 'love shot', '1Team': 'HELLO!', 
                   'Shinee': 'SHINee World', 'Super Junior-M': 'Break Down', 
                   'Super Junior-H': 'Victory Korea', '2AM': 'Time for Confession', 
                   '2PM': 'Hottest Time Of The Day‘, ‘2NE1‘:‘Fir', 'ToHeart': 'Delicious',
                   'After School': 'New Schoolgirl', 'Beast': 'Beast Is The B2ST', 
                   'CNBLUE': 'Blueming', 'f(x)': 'Pink Tape', 'JQT': 'I Fell For You', 
                   'MBLAQ': 'Just BLAQ', 'Rainbow': 'Gossip Girl', 'Spica': 'secret time',
                   'Secret': 'I Want You Back', 'SHU-I': 'BOMB BOMB BOMB', 
                   'T-ara': 'Bo Peep Bo Peep', 'Urban Zakapa': 'Rainbow Ride', 
                   'December': 'Honesty', 'Coed School': 'Too Late', 'Speed': 'Too Late', 
                   'DMTN': 'State Of Emergency', 'F.Cuz': 'Hello Again', 'BTS': 'DNA',
                   "Girl's Day": 'Something', 'GD & TOP': 'Oh Yeah', 'Tiny-G': 'Tiny-G',
                   'GP Basic': 'Pika Brunjuck', 'Homme': 'Moment', 'The SeeYa': 'Tell me',
                   'Infinite': 'First Invasion', 'JYJ': 'The Beginning', 'C-Clown': 'solo', 
                   'Crayon Pop': 'Dancing Queen', 'Cross Gene': 'New Days', 
                   'EvoL': 'Green Light', 'D-Unit': "I’m Missin’ You", 'EXID': 'Holla', 
                   'Exo': 'MAMA', 'Fiestar': 'Vista', 'Gangkiz': 'We became gang', 
                   'Glam': 'Party', "Girls' Generation-TTS": 'Twinkle', 
                   'Hello Venus': 'Venus', 'Honey G': 'Fluttering Heart', 
                   'JJ Project': 'Bounce', 'Lunafly': 'YEOWOOYA', "She'z": 'My way',
                   'Mr. Mr.': 'Who’s That Girl', 'Skarf': 'Oh! Dance',
                   "NU'EST": 'Happily Ever After', 'Phantom': 'Phantom City', 
                   'Puretty': 'Shuwa Shuwa Baby',  'Sunny Days': 'Glory Korea',
                   'Tahiti': 'Hasta Luego', 'Tasty': 'Spectacular', 'Got7': 'Got it?', 
                   'Two X': 'Double Up', 'VIXX': 'Super Hero', '2Yoon': 'Harvest Moon',  
                   'Wonder Boyz': "It's Exciting", '2Eyes': 'Shooting Star', 
                   '5urprise': 'From My Heart', 'AlphaBat': 'AB CITY', 'AOA Black': 'Elvis', 
                   'Bestie': 'Hot Baby', 'Boys Republic': 'Real Talk',  
                   'GI': 'Beatles', 'History': 'Blue Spring', 'Infinite H': 'Crying', 
                   "Ladies' Code": 'Bad Girl', 'LC9': 'MaMa Beat', 'M.Pire': 'New Born', 
                   'QBS': 'Like A Wind', 'Royal Pirates': 'Disappear', 'AB6IX': 'B:COMPLETE',
                   'T-ara N4': 'M! Countdown', '2000 Won': 'Beautiful', 'Enoi': 'Cheeky',
                   'Topp Dogg': 'Say It', 'Wassup': 'Hotter Than A Summe', 
                   '4L': 'Move', '4Ten': 'Tornado', 'Akdong Musician': 'Crescendo', 
                   'Almeng': 'Yes I Do', 'B.I.G': 'Greatest Hits', 'Badkiz': 'Ready to Die', 
                   'Be.A': 'Good to Go', 'Beatwin': 'illusion', 'Berry Good': 'LOVE LETTER', 
                   'Bigflo': 'oblivate', 'Bob Girls': 'No Way', 'Bursters': 'barriers', 
                   'D.Holic': "I DON'T KNOW", 'GD X Taeyang': 'GOOD BOY', 
                   'Halo': 'FEVER', 'HeartB': 'Remember', 'Hi Suhyun': "I'M DIFFERENT", 
                   'JJCC': 'JJCC 1ST MINI ALBUM', 'Laboum': 'Two Of Us', 
                   'Lip Service': 'Upgrade', 'Lovelyz': 'A New Trilogy‬', 
                   'Madtown': 'New World', 'Mamamoo': 'Melting', 'One Way':'one way',
                   'Melody Day': 'SPEED UP', 'Minx': 'Love Shake', 'Nine Muses': 'Give me',
                   'Play the Siren': 'Dream Drive', 'Miss A': 'CODA', 'WJMK': 'STRONG',  
                   'Red Velvet': 'Ice Cream Cake', 'Sonamoo': 'Deja Vu', 
                   'Strawberry Milk': 'Feels So Good', 'The Barberettes': "Stranger's Love", 
                   'The Legend': 'SHADOW', 'Led Apple': 'LEDApple', 'Itzy': 'DALLA DALLA',  
                   'Orange Caramel': 'Catallena', 'Rooftop Moonlight': 'Each Other', 
                   'Rhythm Power': 'Rhythm Power', 'Standing Egg': 'Moment', 
                   'Sistar': 'Push Push', 'Teen Top': 'Clap', 'Touch': 'Touch', 
                   'The Boss': 'AWAKE', 'ZE： A': 'illusion', 'AA': 'Love Back', 
                   'Apeace': 'Carry On', 'Apink': 'Snow Pin', 'B1A4': "Let's Fly", 
                   'Blady': 'Bring Bring', 'BlockB': 'Do U Wanna B?', 'I.B.I': 'quietly',
                   'Boyfriend': 'WITCH', 'Brave Girls': 'Do You Know', 'KNK': 'KNOCK', 
                   'C-REAL': 'Love Diary', 'Chocolat': 'Syndrome', 'Winner': '2014 S/S',
                   'Clover': 'Classic Over', 'Dal Shabet': 'Supa Dupa Diva', 
                   'F-ve Dolls': 'First Love', 'Geeks': 'Officially Missing You', 
                   'M&D': 'Close Ur Mouth', 'M.I.B': 'MEN IN BLACK', 'April': 'Dreaming',
                   'Myname': 'Hello & Goodbye', 'N-Sonic': 'Crazy', 'Wings': 'hair short',
                   'N-Train': 'One Last Cry', 'Rania': 'Demonstrate', 'MASC': 'Strange', 
                   'Sistar19': 'MY BOY', 'Stellar': '‘Rocket Girl', 'Exo-CBX': 'hey mama!', 
                   'Super Junior-D&E': 'Present', 'Trouble Maker': 'Trouble Maker', 
                   'Ulala Session': 'Happy Day', 'Troy': 'Green Light', 'Uniq': 'My Dream', 
                   'Year 7 Class 1': 'white windy', '1Punch': 'The Anthem',  
                   'Bastarz': 'Make It Rain', 'Big Brain': 'sick', 'CLC': 'First Love', 
                   'Day6': 'he Day', 'DIA': 'NEWTRO', 'GFriend': 'Season of Glass', 
                   'iKon': 'LOVE SCENARIO', 'MAP6': 'MOMENTUM', 'MAS': 'The Unit', 
                   'Monsta X': 'Trespass', 'MyB': 'MY OH MY', 'N.Flying': 'Lonely', 
                   'Oh My Girl': 'OH MY GIRL', 'Playback': 'Playback', 'Jus2': 'FOCUS', 
                   'Spectrum': 'Light it up Official', 'Woo!ah!': 'EXCLAMATION',
                   'Pretty Brown': 'elvin jones', 'Seventeen': '17 CARAT',   
                   'Romeo': 'The ROMEO', 'Rubber Soul': 'Drive My Car', 'SF9': 'Fanfare',
                   'Snuper': 'Shall We', 'Twice': 'THE STORY BEGINS', 'I.O.I': 'Crush', 
                   'Unicorn': 'Once Upon A Time', 'UP10TION': 'Summer Go!', 
                   'VAV': 'Under the moonlight', 'VIXX LR': 'Beautiful Liar', 
                   'WANNA.B': 'Attention', 'AOA Cream': "I'm Jelly Baby", 'Red Square': 'PREQUEL', 
                   'Astro':'All Light', 'Blackpink': 'SQUARE ONE', 'MOBB': 'The MOBB', 
                   'Bolbbalgan4': 'To My Youth', 'Boys24': 'Unit Yellow Ver', 
                   'CocoSori': 'DarkCircle', 'Cosmic Girls': 'MoMoMo', 'Duetto': 'DUETTO', 
                   'Double S 301': 'U R Man', 'Gugudan': 'A Girl Like Me',  
                   'Imfact': 'LOLLIPOP', 'Momoland': 'Show Me', 'NCT': 'Chewing Gum', 
                   'Nine Muses A': 'Lip 2 Lip', 'Pentagon': 'Five Senses', 
                   'The East Light': 'six senses', 'Unnies': 'BUTTERFLY', 'Exo-SC': 'What a life', 
                   'Victon': 'Voice To New World', 'Vromance': 'THE ACTION', 
                   '14U': 'N.E.W.S', '3RACHA': '3RACHA', 'A.C.E': '5TAR', 'Onewe': 'ONE',
                   'Be.A': 'Good to Go', 'Busters': 'Grapes', 'Favorite': 'LOCA', 
                   'Dreamcatcher': 'Alone In The City', 'Elris': 'WE, first', 
                   'Good Day': 'ALL DAY GOOD DAY', 'GreatGuys': 'Rolly', 'Target': 'Awake', 
                   'Hash Tag': 'The girl next door', 'Honeyst': 'TEASER', 
                   'TXT': 'The Dream Chapter: STAR', 'Honey Popcorn': 'Bibidi Babidi Boo',
                   'Highlight': 'CAN YOU FEEL IT?', 'Hyeongseop X Euiwoong': 'Love Tint', 
                   'IN2IT': 'In2ition', 'IZ': 'All You Want', 'JBJ': 'NEW MOON', 
                   'Kard': 'RED MOON', 'Longguo & Shihyun': 'the.the.the', 'Stray Kids': 'Mixtape', 
                   'M.O.N.T': 'Going up', 'Mind U': 'What Was That', 'MVP': 'Take It', 
                   'MXM': 'UNMIX', 'Myteen': 'MYTEEN GO！', "NU'EST W": 'W, HERE', 
                   'ONF': 'ON/OFF', 'P.O.P': 'Bad Girl', 'Pristin': 'Hi！PRISTIN', 
                   'Rainz': 'SUNSHINE', 'S.I.S': 'My Dear', "Seven O'Clock": 'ECHO', 
                   'The Boyz': 'The First', 'The Rose': 'Sorry', 'TST': 'show time', 
                   'TRCNG': 'NEW GENERATION', 'Triple H': '365 FRESH', 'UNB': 'BOYHOOD', 
                   'Wooseok x Kuanlin': "I’M A STAR", 'Cherry Bullet': "Let’s Play Cherry Bullet",
                   'Varsity': 'Hole In One', 'Wanna One': 'Energetic', 'Weki Meki': 'WEME', 
                   'Ateez': 'All To Zero', 'A Train To Autumn': 'Farewell Again', 'D-Crunch': '0806', 
                   'Dongkiz': 'NOM', 'Dream Note': 'Dreamlike', 'Fromis 9': 'To Heart', 
                   '(G)I-dle': 'I made', 'Gugudan SeMiNa': 'SEMINA', 'Iz*One': 'COLOR*IZ',
                   'GWSN': 'THE PARK IN THE NIGHT（Part One）', 'JBJ95': 'HOME', 
                   'Loona': 'favOriTe', 'Maywish': 'hello', 'Nature': 'I’m So Pretty', 
                   'Noir': "Twenty's Noir", 'NTB': 'DRAMATIC', 'NeonPunch': 'MOONLIGHT', 
                   'Oh!GG': "Lil' Touch", 'Pristin V': 'Like a V', 'Saturday': 'WiFi', 
                   'SuperM': 'SuperM', 'Argon': 'MASTER KEY', 'BDC': 'BOYS DA CAPO', 
                   'Bvndit': 'BVNDIT, BE AMBITIOUS!', 'Everglow': 'ARRIVAL OF EVERGLOW', 
                   'Fanatics': 'THE SIX', 'Hinapia': 'NEW START', 'Newkidd': 'BOY BOY BOY',  
                   'OnlyOneOf': 'dot point jump', 'Purplebeck': 'I I YO', 'Rocket Punch': 'PINK PUNCH', 
                   'Teen Teen': 'It’s on you', 'Vanner': 'VANNER 1ST DEBUT ALBUM [V]', 
                   'We in the Zone': 'LET’S GET LOUD', 'X1': 'FLASH', 'B.O.Y': 'Blurry', 
                   'Cravity': 'Break all the Rules', 'DKB': 'WANNABE',  'TOO': 'REASON FOR BEING', 
                   'UNVS': 'Timeless Official'}

group_and_gender = {'Orange Caramel': 'girl', 'Rooftop Moonlight': 'girl', 'Rhythm Power': 'boy', 
                    'Standing Egg': 'mixed', 'Sistar': 'girl', 'Teen Top': 'boy', 'Touch': 'boy', 
                    'The Boss': 'boy', 'ZE： A': 'boy', 'AA': 'boy', 'Apeace': 'boy', 
                    'Apink': 'girl', 'B1A4': 'boy', 'Blady': 'girl', 'BlockB': 'boy', 
                    'Boyfriend': 'boy', 'Brave Girls': 'girl', 'C-REAL': 'girl', 'Chocolat': 'girl', 
                    'Clover': 'mixed', 'Dal Shabet': 'girl', 'F-ve Dolls': 'girl', 'Geeks': 'boy', 
                    'M&D': 'boy', 'M.I.B': 'boy', 'Myname': 'boy', 'N-Sonic': 'boy', 'N-Train': 'boy', 
                    'Rania': 'girl', 'Sistar19': 'girl', 'Stellar': 'girl', 'Super Junior-D&E': 'boy', 
                    'Trouble Maker': 'mixed', 'Ulala Session': 'boy', 'Troy': 'boy', 'Uniq': 'boy', 
                    'Wings': 'girl', 'Winner': 'boy','Year 7 Class 1': 'girl', '1Punch': 'boy', 
                    'April': 'girl', 'Bastarz': 'boy', 'Big Brain': 'boy', 'CLC': 'girl', 'Day6': 'boy', 
                    'DIA': 'girl', 'GFriend': 'girl', 'iKon': 'boy', 'MAP6': 'boy', 'MAS': 'boy', 
                    'Monsta X': 'boy', 'MyB': 'girl', 'N.Flying': 'boy', 'Oh My Girl': 'girl', 
                    'Playback': 'girl', 'Pretty Brown': 'boy', 'Romeo': 'boy', 'Rubber Soul': 'girl', 
                    'Seventeen': 'boy', 'Snuper': 'boy', 'Twice': 'girl', 'Unicorn': 'girl', 
                    'UP10TION': 'boy', 'VAV': 'boy', 'VIXX LR': 'boy', 'WANNA.B': 'girl', 
                    'AOA Cream': 'girl', 'Astro':'boy', 'Blackpink': 'girl', 'Bolbbalgan4': 'girl', 
                    'Boys24': 'boy', 'CocoSori': 'girl', 'Cosmic Girls': 'girl', 'Double S 301': 'boy', 
                    'Exo-CBX': 'boy', 'Gugudan': 'girl', 'I.B.I': 'girl', 'I.O.I': 'girl', 
                    'Imfact': 'boy', 'KNK': 'boy', 'MASC': 'boy', 'MOBB': 'boy', 'Momoland': 'girl', 
                    'NCT': 'boy', 'Nine Muses A': 'girl', 'Pentagon': 'boy', 'SF9': 'boy', 
                    'The East Light': 'boy', 'Unnies': 'girl', 'Victon': 'boy', 'Vromance': 'boy', 
                    '14U': 'boy', '3RACHA': 'boy', 'A.C.E': 'boy','Be.A': 'boy', 'Busters': 'girl', 
                    'Dreamcatcher': 'girl', 'Duetto': 'boy', 'Elris': 'girl', 'Favorite': 'girl', 
                    'Good Day': 'girl', 'GreatGuys': 'boy', 'Hash Tag': 'girl', 'Honeyst': 'boy', 
                    'Highlight': 'boy?', 'Hyeongseop X Euiwoong': 'boy', 'IN2IT': 'boy', 'IZ': 'boy', 
                    'JBJ': 'boy', 'Kard': 'mixed', 'Longguo & Shihyun': 'boy', 'M.O.N.T': 'boy', 
                    'Mind U': 'boy', 'MVP': 'boy', 'MXM': 'boy', 'Myteen': 'boy', "NU'EST W": 'boy', 
                    'ONF': 'boy', 'P.O.P': 'girl', 'Pristin': 'girl', 'Rainz': 'boy', 'S.I.S': 'girl', 
                    "Seven O'Clock": 'boy', 'The Boyz': 'boy', 'The Rose': 'boy', 'TST': 'boy', 
                    'TRCNG': 'boy', 'Triple H': 'mixed', 'Varsity': 'boy', 'Wanna One': 'boy', 
                    'Weki Meki': 'girl', 'Ateez': 'boy', 'A Train To Autumn': 'girl', 'D-Crunch': 'boy', 
                    'Dongkiz': 'boy', 'Dream Note': 'girl', 'Fromis 9': 'girl', '(G)I-dle': 'girl', 
                    'Gugudan SeMiNa': 'girl', 'GWSN': 'girl', 'Honey Popcorn': 'girl', 'Iz*One': 'girl', 
                    'JBJ95': 'boy', 'Loona': 'girl', 'Maywish': 'girl', 'Nature': 'girl', 
                    'NeonPunch': 'girl', 'Noir': 'boy', 'NTB': 'boy', 'Oh!GG': "girl", 
                    'Pristin V': 'girl', 'Saturday': 'girl', 'Spectrum': 'boy', 'Stray Kids': 'boy', 
                    'Target': 'boy', 'UNB': 'boy', 'Uni.T': 'girl', 'We Girls': 'girl', 'WJMK': 'girl',  
                    '1Team': 'boy', '1the9': 'boy', 'AB6IX': 'boy', 'Ariaz': 'girl', 'Argon': 'boy', 
                    'BDC': 'boy', 'Bvndit': 'girl', 'Cherry Bullet': 'girl', 'CIX': 'boy', 'D1CE': 'boy', 
                    'Enoi': 'boy', 'Everglow': 'girl', 'Exo-SC': 'boy', 'Fanatics': 'girl', 
                    'Hinapia': 'girl', 'Itzy': 'girl', 'Jus2': 'boy', 'Newkidd': 'boy', 'Oneus': 'boy', 
                    'Onewe': 'boy', 'OnlyOneOf': 'boy', 'Purplebeck': 'girl', 'Rocket Punch': 'girl', 
                    'SuperM': 'boy', 'Teen Teen': 'boy', 'TXT': 'boy', 'Vanner': 'boy', 
                    'Verivery': 'boy', 'ToHeart': 'boy', 'Led Apple': 'boy', 'Miss A': 'girl',
                    'We in the Zone': 'boy', 'Wooseok x Kuanlin': 'boy', 'X1': 'boy', 'B.O.Y': 'boy', 
                    'Cravity': 'boy', 'DKB': 'boy', 'H&D': 'boy', 'MCND': 'boy', 'Red Square': 'girl', 
                    'TOO': 'boy', 'UNVS': 'boy', 'Woo!ah!': 'girl', 'Clazziquai Project':'mixed', 
                    'The Jadu': 'mixed', "K'Pop": 'boy','KISS.': 'girl', 'M.I.L.K':'girl', 'jtL': 'boy', 
                    'CB Mass': 'boy', 'Papaya': 'girl', 'UN': 'boy','TRAX': 'boy', 'Chakra': 'girl', 
                    '5tion': 'boy', 'Jewelry': 'girl', 'Epik High': 'boy', 'F-iV': 'boy',
                    'Black Beat': 'boy', 'Isak N Jiyeon': 'girl', 'V.O.S': 'boy', 'Leessang': 'boy', 
                    'LUV': 'girl', 'MC the Max': 'boy', 'Noel': 'boy', 'Shinvi': 'girl', 
                    'Sugar' : 'girl', 'The Barberettes': 'girl', 'The Legend': 'boy', 
                    'Big Mama': 'girl', 'Dynamic Duo': 'boy', 'Brown Eyed Soul': 'boy', 'Buzz': 'boy',
                    'TVXQ': 'boy', 'Take': 'boy', 'SG Wannabe': 'boy', 'SS501': 'boy', 'LPG': 'girl',
                    'The Grace': 'girl', 'Gavy NJ': 'girl', 'Super Junior': 'boy', 'Paran': 'boy',
                    'SeeYa': 'girl', 'Brown Eyed Girls': 'girl', '2NB': 'girl', 'Untouchable': 'boy', 
                    'Super Junior-K.R.Y.': 'boy', 'DickPunks': 'boy', 'Eluphant': 'boy', 'Kara': 'girl',
                    'Big Bang': 'boy', 'Wonder Girls': 'girl', '8eight': 'mixed', 'F.T. Island': 'boy', 
                    "Girls' Generation": 'girl', 'Sunny Hill': 'mixed', 'Supernova': 'boy', 
                    'Tritops': 'boy', 'Super Junior-T': 'boy', 'Baby Vox Re.V': 'girl', 'T-max': 'boy', 
                    'Black Pearl': 'girl', 'Davichi': 'girl', 'Mighty Mouth': 'boy', 'Miss $': 'girl', 
                    'Shinee': 'boy', 'Super Junior-M': 'boy', 'Super Junior-H': 'boy', '2AM': 'boy', 
                    '2PM': 'boy', '2NE1': 'girl', 'U-KISS': 'boy', '4Minute': 'girl', 
                    'After School': 'girl', 'Beast': 'boy', 'CNBLUE': 'boy', 'f(x)': 'girl', 
                    'JQT': 'girl', 'MBLAQ': 'boy', 'Rainbow': 'girl', 'Secret': 'girl', 'SHU-I': 'boy', 
                    'T-ara': 'girl', 'Urban Zakapa': 'mixed', 'December': 'boy', 'Coed School': 'mixed', 
                    'DMTN': 'boy', 'F.Cuz': 'boy', "Girl's Day": 'girl', 'GD & TOP': 'boy', 
                    'GP Basic': 'girl', 'Homme': 'boy', 'Infinite': 'boy', 'JYJ': 'boy', 
                    'C-Clown': 'boy', 'Melody Day': 'girl', 'Minx': 'girl', 
                    'Crayon Pop': 'girl', 'Cross Gene': 'boy', 'EvoL': 'girl', 'D-Unit': 'girl', 
                    'EXID': 'girl', 'Exo': 'boy', 'Fiestar': 'girl', 'Gangkiz': 'girl', 'Glam': 'girl', 
                    "Girls' Generation-TTS": 'girl', 'Hello Venus': 'girl', 'Honey G': 'boy', 
                    'JJ Project': 'boy', 'Lunafly': 'boy', 'Mr. Mr.': 'boy', 'Skarf': 'girl',
                    "NU'EST": 'boy', 'Phantom': 'boy', "She'z": 'girl','Puretty': 'girl', 
                    'Spica': 'girl', 'D.Holic': 'girl', 'GD X Taeyang': 'boy', 'Got7': 'boy', 
                    'Sunny Days': 'girl', 'Tahiti': 'girl', 'Tasty': 'boy', 'The SeeYa': 'girl', 
                    'Tiny-G': 'girl', 'Two X': 'girl', 'VIXX': 'boy', 'Speed': 'boy',  
                    'Wonder Boyz': 'boy', '2Eyes': 'girl', '2Yoon': 'girl', '5urprise': 'boy', 
                    'AlphaBat': 'boy', 'AOA Black': 'girl', 'Bestie': 'girl', 'Boys Republic': 'boy', 
                    'BTS': 'boy', 'GI': 'girl', 'History': 'boy', 'Infinite H': 'boy', 
                    "Ladies' Code": 'girl', 'LC9': 'boy', 'M.Pire': 'boy', 'QBS': 'girl', 
                    'Royal Pirates': 'boy', 'T-ara N4': 'girl', 'Topp Dogg': 'boy', 'Wassup': 'girl', 
                    '2000 Won': 'boy', '4L': 'girl', '4Ten': 'girl', 'Akdong Musician': 'mixed', 
                    'Almeng': 'boy', 'B.I.G': 'boy', 'Badkiz': 'girl', 'Beatwin': 'boy', 
                    'Berry Good': 'girl', 'Bigflo': 'boy', 'Bob Girls': 'girl', 'Bursters': 'boy', 
                    'Halo': 'boy', 'HeartB': 'boy', 'Hi Suhyun': 'girl', 'JJCC': 'boy', 'Laboum': 'girl', 
                    'Lip Service': 'girl', 'Lovelyz': 'girl‬', 'Madtown': 'boy', 'Mamamoo': 'girl', 
                    'Play the Siren': 'mixed', 'Red Velvet': 'girl', 'Sonamoo': 'girl', 'One Way':'boy',
                    'Strawberry Milk': 'girl', 'Nine Muses': 'girl'}

group_and_year = {'Orange Caramel': '2010', 'Rooftop Moonlight': '2010', 'Rhythm Power': '2013', 
                  'Standing Egg': '2010', 'Sistar': '2010', 'Teen Top': '2010', 'Touch': '2010', 
                  'The Boss': '2010', 'ZE： A': '2010', 'AA': '2011', 'Apeace': '2011', 'Apink': '2011', 
                  'B1A4': '2011', 'Blady': '2011', 'BlockB': '2011', 'Boyfriend': '2011', 
                  'Brave Girls': '2011', 'Myname': '2011', 'Stellar': '2011', 'Troy': '2014', 
                  'C-REAL': '2011', 'Chocolat': '2011', 'Clover': '2011', 'Dal Shabet': '2011', 
                  'F-ve Dolls': '2013', 'Geeks': '2011', 'M&D': '2011', 'M.I.B': '2011', 
                  'N-Sonic': '2011', 'N-Train': '2011', 'Rania': '2011', 'Sistar19': '2011', 
                  'Super Junior-D&E': '2011', 'Trouble Maker': '2011', 'Ulala Session': '2012', 
                  'Uniq': '2014', 'Wings': '2014', 'Winner': '2014','Year 7 Class 1': '2014', 
                  'April': '2015', 'Bastarz': '2015', 'Big Brain': '2015', 'CLC': '2015', 'Day6': '2015', 
                  'DIA': '2015', 'GFriend': '2015', 'iKon': '2015', 'MAP6': '2015', 'MAS': '2016', 
                  'Monsta X': '2015', 'MyB': '2015', 'N.Flying': '2013', 'Oh My Girl': '2015', 
                  'Playback': '2015', 'Pretty Brown': '2015', 'Romeo': '2015', 'Rubber Soul': '2015', 
                  'Seventeen': '2015', 'Snuper': '2015', 'Twice': '2015', 'Unicorn': '2015', 
                  'VAV': '2015', 'VIXX LR': '2015', 'WANNA.B': '2015', 'AOA Cream':'2016',  '1Punch':                       '2015', 'UP10TION': '2015', 'Astro':'2016', 'Pentagon': '2016',  
                  'Blackpink': '2016', 'Bolbbalgan4': '2016', 'Boys24': '2016', 'CocoSori': '2016', 
                  'Cosmic Girls': '2016', 'Double S 301': '2016', 'Exo-CBX': '2016', 'Gugudan': '2016', 
                  'I.B.I': '2016', 'I.O.I': '2016', 'Imfact': '2016', 'KNK': '2016', 'MASC': '2016', 
                  'MOBB': '2016', 'Momoland': '2016', 'NCT': '2016', 'Nine Muses A': '2016', 
                  'SF9': '2016', 'The East Light': '2017', 'Unnies': '2016', 'Victon': '2016',
                  'Vromance': '2016', 'Mind U': '2017', 'Weki Meki': '2017', 'Loona': '2018', 
                  '14U': '2017', '3RACHA': '2017', 'A.C.E': '2017','Be.A': '2017', 'Busters': '2017', 
                  'Dreamcatcher': '2017', 'Duetto': '2017', 'Elris': '2017', 'Favorite': '2017', 
                  'Good Day': '2017', 'GreatGuys': '2017', 'Hash Tag': '2017', 'Honeyst': '2016', 
                  'Highlight': '2017', 'Hyeongseop X Euiwoong': '2017', 'IN2IT': '2017', 'IZ': '2017', 
                  'JBJ': '2017', 'Kard': '2016', 'Longguo & Shihyun': '2017', 'M.O.N.T': '2017', 
                  'MVP': '2017', 'MXM': '2017', 'Myteen': '2017', "NU'EST W": '2017', 'ONF': '2017', 
                  'P.O.P': '2017', 'Pristin': '2017', 'Rainz': '2017', 'S.I.S': '2017', 
                  "Seven O'Clock": '2017', 'The Boyz': '2017', 'The Rose': '2017', 'TST': 'show time', 
                  'TRCNG': '2017', 'Triple H': '2017', 'Varsity': '2017', 'Wanna One': '2017', 
                  'Ateez': '2018', 'A Train To Autumn': '2018', 'D-Crunch': '2018', 'Dongkiz': '2019', 
                  'Dream Note': '2018', 'Fromis 9': '2017', '(G)I-dle': '2018', 'Gugudan SeMiNa': '2018', 
                  'GWSN': '2018', 'Honey Popcorn': '2018', 'Iz*One': '2018', 'JBJ95': '2018', 
                  'Maywish': '2018', 'Nature': '2018', 'NeonPunch': '2018', 'Noir': '2018', 
                  'Oh!GG': "2018", 'Pristin V': '2018', 'Saturday': '2018', 'Spectrum': '2018', 
                  'Stray Kids': '2018', 'Target': '2018', 'UNB': '2018', 'Uni.T': '2018', 
                  'We Girls': '2018', 'NTB': '2018', 'CIX':'2019', 'Fanatics': '2019', 
                  'WJMK': '2018',  '1Team': '2019', '1the9': '2019', 'AB6IX': '2019', 'Ariaz': '2019', 
                  'Argon': '2019', 'BDC': '2019', 'Bvndit': '2019', 'Cherry Bullet': '2019', 
                  'D1CE': '2019', 'Enoi': '2019', 'Everglow': '2019', 'Exo-SC': '2019', 
                  'Hinapia': '2019', 'Itzy': '2019', 'Jus2': '2019', 'Newkidd': '2019', 'Oneus': '2019', 
                  'Onewe': '2019', 'OnlyOneOf': '2019', 'Purplebeck': '2019', 'Rocket Punch': '2019', 
                  'SuperM': '2019', 'Teen Teen': '2019', 'TXT': '2019', 'Vanner': '2019', 
                  'We in the Zone': '2019', 'Wooseok x Kuanlin': '2019', 'X1': '2019', 'B.O.Y': '2019', 
                  'Cravity': '2020', 'DKB': '2020', 'H&D': '2020', 'MCND': '2020', 'Red Square': '2020', 
                  'TOO': '2020', 'UNVS': '2020', 'Woo!ah!': '2020', 'Clazziquai Project':'2004', 
                  'The Jadu': '2001', "K'Pop": '2001', 'KISS.': '2008', 'M.I.L.K':'2002', 'jtL': '2001', 
                  'CB Mass': '2000', 'Papaya': '2000', 'UN': '2000','TRAX': '2004', 'Chakra': '2000', 
                  '5tion': '2001', 'Jewelry': '2001', 'Epik High': '2003', 'F-iV': '2000',
                  'Black Beat': '2002', 'Verivery': '2019', 'Big Mama': '2003', 
                  'Isak N Jiyeon': '2002', 'V.O.S': '2007', 'Leessang': '2002', 'LUV': 'girl',
                  'MC the Max': '2000', 'Noel': '2002', 'Shinvi': '2001', 'Sugar' : '2001', 
                  'Dynamic Duo': '2004', 'Brown Eyed Soul': '2003', 'Buzz': '2003', 'TVXQ': '2003', 
                  'Take': '2003', 'Super Junior': '2005', 'Supernova': '2007', 
                  'SG Wannabe': '2004', 'DickPunks': '2006', 'Eluphant': '2006', 'Kara': '2007',
                  'SS501': '2005', 'LPG': '2009','The Grace': '2005', 'Gavy NJ': '2005', 
                  'Paran': '2005', 'SeeYa': '2006', 'Brown Eyed Girls': '2006', '2NB': '2006', 
                  'Untouchable': '2008', 'Super Junior-K.R.Y.': '2006', 'Big Bang': '2006', 
                  'Wonder Girls': '2007', '8eight': '2007', 'Nine Muses': '2010', 'One Way': '2010',
                  'F.T. Island': '2007', "Girls' Generation": '2007', 'Sunny Hill': '2007', 
                  'Tritops': '2007', 'Super Junior-T': '2007', 'Baby Vox Re.V': '2007', 'T-max': '2007', 
                  'Black Pearl': '2007', 'Davichi': '2008', 'Mighty Mouth': '2008', 'Miss $': '2008', 
                  'Shinee': '2008', 'Super Junior-M': '2007', 'Super Junior-H': '2007', '2AM': '2008', 
                  '2PM': '2008‘, ‘2NE1‘:‘2009', 'U-KISS': '2008', '4Minute': '2009', 
                  'After School': '2009', 'C-Clown': '2012', 'Urban Zakapa': '2009', 
                  'Beast': '2009', 'CNBLUE': '2009', 'f(x)': '2009', 'JQT': '2009', 'MBLAQ': '2009', 
                  'Rainbow': '2009', 'Secret': '2009', 'SHU-I': '2009', 'T-ara': '2009', 
                  'December': '2009', 'Coed School': '2009', 'Infinite': '2010', 'JYJ': '2010',           
                  'DMTN': '2010', 'F.Cuz': '2010', "Girl's Day": '2010', 'GD & TOP': '2010', 
                  'GP Basic': '2010', 'D-Unit': '2012', 'JJ Project': '2012', 'Phantom': '2012', 
                  'Homme': '2010', 'Crayon Pop': '2012', 'Cross Gene': '2012', 'EvoL': '2012', 
                  'EXID': '2012', 'Exo': '2012', 'Fiestar': '2012', 'Gangkiz': '2012', 'Glam': '2012', 
                  "Girls' Generation-TTS": '2012', 'Hello Venus': '2012', 'Honey G': '2012', 
                  'Lunafly': '2012', 'Mr. Mr.': '2012', 'Skarf': '2012', "NU'EST": '2012', 
                  "She'z": '2012', 'Puretty': '2012', 'Spica': '2012', 'Sunny Days': '2012', 
                  'Tahiti': '2012', '2Yoon': '2013', 'Infinite H': '2013', 'Royal Pirates': '2004', 
                  'Tasty': '2012', 'The SeeYa': '2012', 'Tiny-G': '2012', 'Two X': '2012', 
                  'VIXX': '2012', 'Speed': '2013',  'Wonder Boyz': '2012', '2Eyes': '2013', 
                  '5urprise': '2013', 'AlphaBat': '2013', 'AOA Black': '2012', 'Bestie': '2013', 
                  'Boys Republic': '2013', 'BTS': '2013', 'GI': '2013', 'History': '2013', 
                  "Ladies' Code": '2013', 'LC9': '2013', 'M.Pire': '2013', 'QBS': '2013', 
                  'T-ara N4': '2013', 'Topp Dogg': '2013', 'Wassup': '2013', '2000 Won': '2014', 
                  '4L': '2014', 'Badkiz': '2014', 
                  '4Ten': '2014', 'Akdong Musician': '2014', 'Almeng': '2014', 'B.I.G': '2014', 
                  'Beatwin': '2014', 'Berry Good': '2014', 'Bigflo': '2014', 'Bob Girls': '2014', 
                  'Bursters': '2014', 'D.Holic': '2014', 'GD X Taeyang': '2014', 'Got7': '2014', 
                  'Halo': '2014', 'Lip Service': '2014', 'Minx': '2014', 'Strawberry Milk': '2014', 
                  'HeartB': '2014', 'Hi Suhyun': '2014', 'JJCC': '2014', 'Laboum': '2014', 
                  'Lovelyz': '2014‬', 'Madtown': '2014', 'Mamamoo': '2014', 'Melody Day': '2014', 
                  'Play the Siren': '2014', 'Red Velvet': '2014', 'Sonamoo': '2014', 
                  'The Barberettes': '2014', 'The Legend': '2014', 'ToHeart': '2014', 
                  'Led Apple': '2010', 'Miss A': '2010'}

def greeting_chat(starting_msg):
    """print a message to start a conversation.
    
    Parameters
    ----------
    starting_msg: bool
        If true, the function starts
    
        Returns    
        ----------
        string
            string containing a greeting message
    """
    
    # When the condition is fulfilled, start a conversation by 
    # printing a welcome message.
    if starting_msg == True:
        
        return "hi! I can help you to know more about K-pop."
    
def ask_gender(input_bool, answer_of_group):
    """print a respond based on the input about gender
    
    parameters
    ----------
    input_bool: bool
        If true, the function starts
    
    answer_of_group: str
        Contains the global variable of which group the user is talking about
    
    """
    
    if input_bool == True:
        
        # find if important words are in user import and use that to decide the respond
        # to them
        answer_of_gender = input('Well, do you know if they are a boy band or a girl band? ')
        answer_yes = answer_of_gender.find('yes')
        answer_no = answer_of_gender.find('no')
        gender = group_and_gender[answer_of_group]
        
        # use a while loop so it will keep asking for the right input until it gets it
        while answer_yes < 0 and answer_no < 0:
            
            answer_of_gender = input("please tell me either 'yes' or 'no'. ")
            answer_yes = answer_of_gender.find('yes')
            answer_no = answer_of_gender.find('no')
            gender = group_and_gender[answer_of_group]
            
        if answer_yes >= 0:
            
            # use customized tring to respond to the user.
            print("Wow! you really know a lot. I also know that they are\
a " + gender + " group. What's your favorite song by them?")
        
        elif answer_no >= 0:
            
            print("It's totally fine. No worries I got you. They are \
a " + gender + " group. Do you know any song by them?")
            

def ask_song(input_bool, answer_of_group):
    """print a respond based on the input about song
    
    parameters
    ----------
    input_bool: bool
        If true, the function starts
    
    answer_of_group: str
        Contains the global variable of which group the user is talking about
   
   """
    
    if input_bool == True:
 
        # find if important words are in user import and use that to decide the respond
        # to them
        answer_song = input()
        answer_yes = answer_song.find('yes')
        answer_no = answer_song.find('no')
        fav_song = group_and_songs[answer_of_group]
        
        # use conditions to respond differently based on user's input about 
        # their knowledge of song
        if answer_yes < 0 and answer_no < 0:
            
            if answer_song in group_and_songs.values():
                
                print(answer_song + ' is your favorite song? \
    Mine is the same! We have the same taste! Also, do you know what year they came out?')
            
            else:
                print("I will get check it out. My favorite song is " + fav_song + '.\
' + 'Also, do you know what year they came out?')
    
        if answer_yes >= 0:
            
            input('Cool! What is it? My favorite some by them is ' + fav_song)
            print('Great song! I love it! Also, do you know what year they came out?')
        
        elif answer_no >= 0:
            print('I love ' + fav_song + '. You should check it out! Also, do \
you know what year they came out?')  


def ask_of_year(input_bool, answer_of_group, answer_of_year):
    """print a message about year to user when condition meets
    
    parameters
    ----------
    input_bool: bool
        If true, the message get printed
        
    answer_of_group: str
        Contains the global variable of which group the user is talking about
        
    answer_of_year: str
        Contains the user input of the year
                
                returns
                ----------
                string
                    string that is specific to the input about year
    """
    
    if input_bool == True:
        
        # use find method to detect if there is key word that needs attention since it makes the 
        # output different
        answer_of_yes = answer_of_year.find('yes')
        answer_of_no = answer_of_year.find('no')
        year_of_group = group_and_year[answer_of_group]
        
        # use conditions to respond differently based on user's knowledge about the year
        # when the group came out
        if answer_of_yes < 0 and answer_of_no < 0:
            
            if answer_of_year in group_and_year.values():
                
                return 'OMG! You are really a fan! '
            
            else:
                
                return "Ops, you got it wrong. They actually came out in " + year_of_group
    
        if answer_of_yes >= 0:
            
            return 'Cool! I also know that they came out in ' + year_of_group
        
        elif answer_of_no >= 0:
            
            return "It's okay. Not everyone is as crazy as me for K-pop. They came out \
in " + year_of_group
            

def more_info(input_bool, answer_of_group):
    """print a message with more info to user when condition meets
    
    parameters
    ----------
    input_bool: bool
        If true, the message get printed
        
   answer_of_group: str
        Contains the global variable of which group the user is talking about
    
    """
    
    
    if input_bool == True:
        
        input('I actually know a lot about them! Let me tell you more! But it will take \
probably a long time.')
        
        # use external api to give user more information
        input(wikipedia.summary(answer_of_group + ' Korean'))

