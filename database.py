import sqlite3

c = sqlite3.connect("movie.db")

"""c.execute('''create table register(
            cust_name TEXT NOT NULL,
            cust_phone INT PRIMARY KEY NOT NULL,
            cust_email TEXT NOT NULL,
            cust_password TEXT NOT NULL);''')"""

"""c.execute('''create table movie(
            mov_id INT PRIMARY KEY NOT NULL,
            mov_name TEXT NOT NULL,
            mov_lang TEXT NOT NULL,
            mov_des TEXT NOT NULL,
            price INT NOT NULL);''')"""
"""c.execute('''alter table movie 
ADD url TEXT''')"""

"""c.execute('''insert into movie(mov_id, mov_name,mov_lang,mov_des,price,url)
            values(100, "KGF-2", "Kannada","The blood-soaked land of Kolar Gold Fields (KGF) has a new overlord now - Rocky, whose name strikes fear in the heart of his foes. His allies look up to Rocky as their saviour, the government sees him as a threat to law and order; enemies are clamouring for revenge and conspiring for his downfall. Bloodier battles and darker days await as Rocky continues on his quest for unchallenged supremacy.",350,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/kgf-chapter-2-et00098647-08-04-2022-11-33-32.jpg"),
                (101, "Beast","Tamil" ,"Veera Raghavan, a former raw agent, is tasked to deal with an International Terrorist organization who have hijacked a mall demanding the release of their leader. Can Veera rescue all the hostages in time?",250,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/beast-et00311733-13-04-2022-01-25-10.jpg"),
                (102, "RRR", "Telugu", "RRR is a period drama set in India during the 1920s, revolving around the inspiring journey of two of India`s freedom fighters - Alluri Sitarama Raju and Komaram Bheem.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/rrr-et00094579-29-03-2022-03-23-44.jpg"),
                (103,"Doctor Strange: In The Multiverse Of Madness","English","Doctor Strange in the Multiverse of Madness - a thrilling ride through the Multiverse with Doctor Strange, his trusted friend Wong and Wanda Maximoff, aka Scarlet Witch.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/doctor-strange-in-the-multiverse-of-madness-et00310791-07-04-2022-05-54-25.jpg"),
                (104,"James","Kannada","Santhosh Kumar, who goes by the name James, runs a security agency and has been commissioned to take care of a family that owns a drug cartel. But is there more to who Santhosh really is?",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/james-et00312373-16-03-2022-09-14-19.jpg");''')
c.commit()"""
"""data = c.execute("select * from movie")
for i in data:
    print(i[0], i[1], i[2], i[3], i[4], i[5])

with sqlite3.connect("movie.db") as c:
    count = c.execute("select count(mov_id) from movie")

for i in count:
    print(i[0])"""

"""c.execute('''create table ticket(
            ticket_id INT PRIMARY KEY NOT NULL,
            Count_of_Ticket INT NOT NULL,
            cust_id INT NOT NULL);''')"""

"""c.execute('''insert into movie(mov_id, mov_name,mov_lang,mov_des,price,url)
            values(105,"The Kashmir Files","Hindi","The Kashmir Files is a true story, based on video interviews of the first generation victims of the Genocide of Kashmiri Pandit Community In 1990.",300,"https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:oi-discovery-catalog@@icons@@heart_202006300400.png,ox-24,oy-617,ow-29:ote-OTElICA1NzZrIHZvdGVz,ots-29,otc-FFFFFF,oy-612,ox-70:q-80/et00110845-glzddsanvj-portrait.jpg"),
                  (106,"The Batman","English","The caped crusader, Bruce Wayne joins hands with unlikely allies to unmask a sadistic serial killer who`s leaving bodies across Gotham city.",300,"https://assets-in.bmscdn.com/iedb/movies/images/extra/vertical_logo/mobile/thumbnail/xxlarge/the-batman-et00129624-18-04-2022-03-25-49.jpg"), 
                  (107," Fantastic Beasts: The Secrets Of Dumbledore","English","Professor Albus Dumbledore (Jude Law) knows that the powerful Dark wizard Gellert Grindelwald (Mads Mikkelsen) is moving to seize control of the wizarding world. Unable to stop him alone, he entrusts Magizoologist Newt Scamander (Eddie Redmayne) to lead an intrepid team of wizards, witches and one brave Muggle baker on a dangerous mission, where they encounter old and new beasts and clash with Grindelwald`s growing legion of followers. But with the stakes so high, how long can Dumbledore remain on the sidelines?",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/fantastic-beasts-the-secrets-of-dumbledore-et00319643-06-04-2022-02-24-42.jpg"),
                  (108,"Desert Coaster & Trike Coaster (7D)","English","Desert Coaster & Trike Coaster is an English, 7D, virtual reality show, which will take you on the adventure of a lifetime! Get ready to leave reality behind and dive into an exciting and thrilling journey.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/desert-coaster-and-trike-coaster-7d-et00326402-12-04-2022-09-24-17.jpg"),
                  (109,"Aasha","Gujarati","Deepak is deeply in love with Aasha but gets punished for loving her. What is his fault? What does Aasha get for her supreme sacrifice?",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/aasha-et00326370-08-04-2022-06-02-40.jpg"),
                  (110,"#MUTE","Kannada","A lone divorcee sets the race against time to search for the person that shattered her life.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/-mute-et00321183-18-04-2022-05-59-06.jpg"),
                  (111,"Main Te Bapu","Punjabi","Main Te Bapu is a Punjabi movie featuring Parmish Verma, Satish Verma and Sanjeeda Shaikh in lead roles.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/main-te-bapu-et00314861-28-02-2022-01-37-47.jpg"),
                  (112,"No Way Out","Malayalam","No Way Out is an unconventional survival thriller that traverses through the life of an NRI returnee David, and how his life turns upside down when he ventures into an outlandish business.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/no-way-out-et00325854-06-04-2022-01-16-18.jpg"),
                  (113,"Krishna Vrinda Vihari","Telugu","Krishna Vrinda Vihari is a Telugu movie starring Naga Shaurya, Shirley Setia in prominent roles. It is a romantic comedy directed by Anish Krishna. Usha Mulpuri and Naga Shaurya has co produced, forming part of the crew.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/krishna-vrinda-vihari-et00321670-06-04-2022-01-44-24.jpg"),
                  (114,"Jersey","English","An ex-cricketer struggling to make ends meet, wants to fulfill his child`s wish of getting a Jersey but in the process comes face to face with his heroic past and is forced to decide if he will rise to the occasion or continue to live a life as a loser?",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/jersey-et00118049-11-04-2022-12-53-49.jpg"),
                  (115,"Operation Romeo","Hindi","Operation Romeo is a drama film directed by Shashant Shah, featuring Sidhant Gupta and Vedika Pinto in prominent roles.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/operation-romeo-et00325828-01-04-2022-05-27-53.jpg"),
                  (116,"Raavan","Bengali","Raavan revolves around a man who is seen fighting against an evil person who does bad deeds.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/raavan-et00324935-21-03-2022-02-08-53.jpg"),
                  (117,"Heropanti 2","Hindi","Babloo is a computer genius and Inaaya is a self-made billionaire. The two fall in love but suddenly part ways. When they finally reunite, the world wants Babloo dead.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/heropanti-2-et00128067-14-04-2022-03-52-38.jpg"),
                  (118,"DC League of Super-Pets","English","Krypto the Super-Dog and Superman are inseparable best friends and fighting crime in Metropolis side by side. When Superman and the rest of the Justice League are kidnapped, Krypto must convince the others to master their own newfound powers and help him rescue the superheroes.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/dc-league-of-super-pets-et00318402-25-11-2021-01-25-26.jpg"),
                  (119,"Memory","English","An assassin-for-hire finds that he's become a target after he refuses to complete a job for a dangerous criminal organization. A remake of the 2003 Belgian film The Memory of a Killer.",300,"https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/memory-et00325616-29-03-2022-12-44-10.jpg");''')
c.commit()"""
data = c.execute("select * from movie where lower(mov_name) = 'aasha'")
for i in data:
    print(i[0], i[1], i[2], i[3], i[4], i[5])