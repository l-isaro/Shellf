import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='password123', database='books')

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS books;")
table_query = """ CREATE TABLE IF NOT EXISTS book_ratings(
                        id int AUTO_INCREMENT,
                        title varchar(100) NOT NULL,
                        rating int,
                        PRIMARY KEY(id));"""
review_table = """ CREATE TABLE IF NOT EXISTS book_reviews(
                        id int AUTO_INCREMENT,
                        book_title varchar(100),
                        review varchar(255),
                        PRIMARY KEY(id));"""
mycursor.execute(table_query)
mycursor.execute(review_table)
mydb.commit()


class Menu:
    """Displays the countries to choose from."""
    def __init__(self, selection):
        """initialize selection"""
        self.__selection = selection

    @property
    def selection(self):
        """assigns selection to selection"""
        return self.__selection

    @selection.setter
    def selection(self, value):
        """conditions"""
        if value > 10 or value < 1:
            raise ValueError("selection out of range")    
        
        self.__selection = value

    def display_books(self):

        # Rwanda
        if self.__selection == 0:
            print("""          
                                1. Rwanda
                  
                      1. Between Wild and Free - Caroline Numuhire
                      2. Barefoot in Germany - Tete Loeper 
                      3. The girl who smiled beads - Clementine Wamariya 
                      4. The Barefoot – Scholastique 
                      5. From Red Earth: A Rwandan Story of Healing and Forgiveness – Denise Uwimana
                      6. Scars that Shape Us – Divine Akimana 
                      7. Love tails – Yves Muhizi
                      8. First Creation - Sandra Nadege

                      You can purchase any of these books on Amazon: 
                      https://www.amazon.com/Books-Online/s?rh=n%3A283155%2Cp_27%3AOnline
                      """)

        elif self.__selection == 1:
            print("""           2. Kenya
                     
                     1. petals of blood by ngũgĩ wa thiong’o
                     2. the river and the source by margaret a. Ogola
                     3. one day i will write about this place: a memoir by binyavanga wainaina 
                     4. dust by yvonne adhiambo owuor
                     5. the promised land by grace ogot
                     6. nairobi heat by mukoma wa ngugi
                     7. population, tradition, and environmental control in colonial kenya by martin s. Shanguhyia
                     8. facing mount kenya by jomo kenyatta
                     9. history of resistance in kenya 1884-2002 by maina wa kĩnyattĩ
                  
                     You can purchase any of these books on Amazon:
                     https://www.amazon.com/Books-Online/s?rh=n%3A283155%2Cp_27%3AOnline
                  """)
        # Ethiopia
        elif self.__selection == 2:
            print("""           3. Ethiopia
                  
                     1. cutting for stone by abraham verghese
                     2. the shadow king by maaza mengiste
                     3. the beautiful things that heaven bears by dinaw mengestu
                     4. open my eyes, that i may see marvellous things by alice allan
                     5. beneath the lion's gaze by maaza mengiste
                     6. addis ababa noir by various
                     7. the wife's tale by aida edemariam
                     8. shallow graves: a memoir of the ethiopia-eritrea war by richard reid
                     9. i want to die with a flag. ethiopia: my delusions and disillusionment by vartkes nalbandian
                     10. held at a distance: a rediscovery of ethiopia by rebecca g. Haile
                  
                     You can purchase any of these books on Amazon:
                     https://www.amazon.com/Books-Online/s?rh=n%3A283155%2Cp_27%3AOnline
                  """)
        # Nigeria
        elif self.__selection == 3:
            print("""           4. Nigeria 
                  
                      1. COCONUT: A BLACK GIRL, A WHITE FOSTER FAMILY, AND THE SEARCH FOR BELONGING AND IDENTITY BY FLORENCE OÒLAÌJIÌDEÌ
                      2. HOPE AND GLORY BY JENDELLA BENSON
                      4. YOU MADE A FOOL OF DEATH WITH YOUR BEAUTY BY AKWAEKE EMEZI
                      5. A COASTLINE IS AN IMMEASURABLE THING: A MEMOIR ACROSS THREE CONTINENTS BY MARY-ALICE DANIEL
                      6. THE LEGACY OF MOLLY SOUTHBOURNE (THE MOLLY SOUTHBOURNE TRILOGY BOOK 3) BY TADE THOMPSON
                      7. WHERE THE CHILDREN TAKE US: HOW ONE FAMILY ACHIEVED THE UNIMAGINABLE BY ZAIN E. ASHER
                      8. NOTES FROM A YOUNG BLACK CHEF BY KWAME ONWUACHI WITH JOSHUA DAVID STEIN
                      9. WAHALA: A NOVEL BY NIKKI MAY
                      10. OPERATION SISTERHOOD BY OLUGBEMISOLA RHUDAY-PERKOVICH
                  
                      You can purchase any of these books on Amazon:
                      https://www.amazon.com/Books-Online/s?rh=n%3A283155%2Cp_27%3AOnline
                   """) 
        # Ghana
        elif self.__selection == 4:
            print("""           5. Ghana
                  
                     1. Changes: A Love Story by Ama Ata Aidoo
                     2. Tail of the Blue Bird BY NII AYIKWEI PARKES
                     3. Ghana must go by Taiye Selasi
                     4. Homegoing by Yaa Gyasi
                     5. The housemaid by Amma Darko
                     6. Selected speeches by Kwame
                     7. This earth, my brother by Kofi Awoonor
                     8. Daughter in Exile: A Novel by Bisi Adjapon
                     9. Fragments by Ayi Kwei Armah
                     10. Fibbed by Elizabeth Agyemang""")
        # Egypt
        elif self.__selection == 5:
            print("""           6. Egypt
                  
                     1. TREASURE TROVE OF BENEFITS AND VARIETY AT THE TABLE EDITED AND TRANSLATED BY NAWAL NASRALLAH
                     2. BRAINS CONFOUNDED BY THE ODE OF ABU SHADUF EXPOUNDED EDITED AND TRANSLATED BY HUMPHREY DAVIES
                     3. THE ESSENTIAL TAWFIQ AL-HAKIM ED. DENYS JOHNSON-DAVIES
                     4. THE DAYS BY TAHA HUSSEIN, TRANSLATED BY E.H. PAXTON, HILARY WAYMENT, KENNETH CRAGG
                     5. THE CALL OF THE CURLEW BY TAHA HUSSEIN, TRANSLATED BY A. B. AS-SAFI
                     6. MIRAMAR BY NAGUIB MAHFOUZ, TRANSLATED BY FATMA MOUSSA MAHMOUD
                     7. THE OPEN DOOR BY LATIFA AL-ZAYYAT, TRANSLATED BY MARILYN BOOTH
                     8. THE MAN WHO LOST HIS SHADOW BY FATHY GHANEM, TRANSLATED BY DESMOND STEWART 
                     9. THE SEARCH: PERSONAL PAPERS BY LATIFA AL-ZAYYAT, TRANSLATED BY SOPHIE BENNETT 
                  
                     You can purchase any of these books on Amazon:
                     https://www.amazon.com/Books-Online/s?rh=n%3A283155%2Cp_27%3AOnline
                     """)
        # Libya
        elif self.__selection == 6:
            print("""           7. Libya
                  
                      1. The Return: Fathers, Sons and the Land in Between by Hisham Matar 
                      2. In the Country of Men by Hisham Matar
                      3. The Arab of the Future: A Childhood in the Middle by Riad Sattouf
                      4. Under the Tripoli Sky by Kamal Ben Hameda 
                      5. The Shadows of Ghadame by Joëlle Stolz
                      6. Maps of the soul by Ahmed Fagih
                      7. Gold dust by Ibrahim Al-koni
                      8. Green book by Muammmar Gaddafi
                      9. The lion's Gane by Nelson DeMille
                      10. The puppet by Ibrahim Al-koni
                  
                     You can purchase any of these books on Amazon:
                     https://www.amazon.com/Books-Online/s?rh=n%3A283155%2Cp_27%3AOnline""")
        # South Africa
        elif self.__selection == 7:
            print("""           8. South Africa
                  
                      1. Bitter fruit by Achmat Dangor
                      2. The promise by Damon Galgut
                      3. Portrait with keys by Ivan Vladislavic
                      4. Young blood by Sifiso Mzobe
                      5. The Dark Flood by Deon Meyer
                      6. The scramble for Africa by Thomas Pakenham
                      7. The quality of mercy by Siphiwe Gloria Ndiovu
                      8. Another country by Karel Schoeman, 1984
                      9. Zoo city by Lauren Beukes
                      10. The grass is singing by Doris Lessing
                  
                     You can purchase any of these books on Amazon:
                     https://www.amazon.com/Books-Online/s?rh=n%3A283155%2Cp_27%3AOnline""")

        # Zambia 
        elif self.__selection == 8:
            print("""          9. Zambia
                  
                      1. The old draft by Namwali Serpell
                      2. A cowrie of hope by Binwell Sinyangwe
                      3. Patchwork by Ellen Banda-Aaku
                      4. Kumukanda by Kayo Chingonyi
                      5. Travel light, move fast by Alexandra Fuller
                      6. The unheard by Josh Swiller
                      7. North of south by Shiva Naipul
                      8. The mourning bird by Mubanga Kalimamukwento
                      9. Fever Dream by Lincoln Child
                      10. The ukiwi Road by Dervla Murphy
                  
                     You can purchase any of these books on Amazon:
                     https://www.amazon.com/Books-Online/s?rh=n%3A283155%2Cp_27%3AOnline""")

        # DRC
        elif self.__selection == 9:
            print("""          10. DRC
                      1. The year of the gorilla by George Schaller
                      2. Congo by Michael Crichton
                      3. Refugee: A memoir by Emmanuel Mbolela
                      4. The poisonwood Bible by Barbara Kingsolver
                      5. Heart of darkness by Joseph Conrad
                      6. Tram 83 by Fiston Mwanza Mujila
                      7. Mr. Fix it by Richard Ali A Mutu
                      8. Maison rouge by Leolina Leila Juma
                      9. No palce to call home by J.J Cola
                      10. Congolese Wiskunde by In Koli Jean Bofane
                  
                     You can purchase any of these books on Amazon:
                     https://www.amazon.com/Books-Online/s?rh=n%3A283155%2Cp_27%3AOnline""")

        # user wants to rate a book they read
        elif self.__selection == 10:
            print("""           
                                1. Rwanda
                
                    1. Between Wild and Free - Caroline Numuhire
                    2. Barefoot in Germany - Tete Loeper 
                    3. The girl who smiled beads - Clementine Wamariya 
                    4. The Barefoot - Scholastique 
                    5. From Red Earth: A Rwandan Story of Healing and Forgiveness - Denise Uwimana
                    6. Scars that Shape Us - Divine Akimana 
                    7. Love tails - Yves Muhizi
                    8. First Creation - Sandra Nadege
                    
                                2. Kenya
                
                    1. petals of blood by ngũgĩ wa thiong'o
                    2. the river and the source by margaret a. Ogola
                    3. one day i will write about this place: a memoir by binyavanga wainaina 
                    4. dust by yvonne adhiambo owuor
                    5. the promised land by grace ogot
                    6. nairobi heat by mukoma wa ngugi
                    7. population, tradition, and environmental control in colonial kenya by martin s. Shanguhyia
                    8. facing mount kenya by jomo kenyatta
                    9. history of resistance in kenya 1884-2002 by maina wa kĩnyattĩ
                
                                3. Ethiopia
                
                    1. cutting for stone by abraham verghese
                    2. the shadow king by maaza mengiste
                    3. the beautiful things that heaven bears by dinaw mengestu
                    4. open my eyes, that i may see marvellous things by alice allan
                    5. beneath the lion's gaze by maaza mengiste
                    6. addis ababa noir by various
                    7. the wife's tale by aida edemariam
                    8. shallow graves: a memoir of the ethiopia-eritrea war by richard reid
                    9. i want to die with a flag. ethiopia: my delusions and disillusionment by vartkes nalbandian
                    10. held at a distance: a rediscovery of ethiopia by rebecca g. Haile
                    
                                4. Nigeria 
                
                    1. COCONUT: A BLACK GIRL, A WHITE FOSTER FAMILY, AND THE SEARCH FOR BELONGING AND IDENTITY BY FLORENCE OÒLAÌJIÌDEÌ
                    2. HOPE AND GLORY BY JENDELLA BENSON
                    4. YOU MADE A FOOL OF DEATH WITH YOUR BEAUTY BY AKWAEKE EMEZI
                    5. A COASTLINE IS AN IMMEASURABLE THING: A MEMOIR ACROSS THREE CONTINENTS BY MARY-ALICE DANIEL
                    6. THE LEGACY OF MOLLY SOUTHBOURNE (THE MOLLY SOUTHBOURNE TRILOGY BOOK 3) BY TADE THOMPSON
                    7. WHERE THE CHILDREN TAKE US: HOW ONE FAMILY ACHIEVED THE UNIMAGINABLE BY ZAIN E. ASHER
                    8. NOTES FROM A YOUNG BLACK CHEF BY KWAME ONWUACHI WITH JOSHUA DAVID STEIN
                    9. WAHALA: A NOVEL BY NIKKI MAY
                    10. OPERATION SISTERHOOD BY OLUGBEMISOLA RHUDAY-PERKOVICH
                    
                                5. Ghana
                
                    1. Changes: A Love Story by Ama Ata Aidoo
                    2. Tail of the Blue Bird BY NII AYIKWEI PARKES
                    3. Ghana must go by Taiye Selasi
                    4. Homegoing by Yaa Gyasi
                    5. The housemaid by Amma Darko
                    6. Selected speeches by Kwame
                    7. This earth, my brother by Kofi Awoonor
                    8. Daughter in Exile: A Novel by Bisi Adjapon
                    9. Fragments by Ayi Kwei Armah
                    10. Fibbed by Elizabeth Agyemang
                    
                                6. Egypt
                
                    1. TREASURE TROVE OF BENEFITS AND VARIETY AT THE TABLE EDITED AND TRANSLATED BY NAWAL NASRALLAH
                    2. BRAINS CONFOUNDED BY THE ODE OF ABU SHADUF EXPOUNDED EDITED AND TRANSLATED BY HUMPHREY DAVIES
                    3. THE ESSENTIAL TAWFIQ AL-HAKIM ED. DENYS JOHNSON-DAVIES
                    4. THE DAYS BY TAHA HUSSEIN, TRANSLATED BY E.H. PAXTON, HILARY WAYMENT, KENNETH CRAGG
                    5. THE CALL OF THE CURLEW BY TAHA HUSSEIN, TRANSLATED BY A. B. AS-SAFI
                    6. MIRAMAR BY NAGUIB MAHFOUZ, TRANSLATED BY FATMA MOUSSA MAHMOUD
                    7. THE OPEN DOOR BY LATIFA AL-ZAYYAT, TRANSLATED BY MARILYN BOOTH
                    8. THE MAN WHO LOST HIS SHADOW BY FATHY GHANEM, TRANSLATED BY DESMOND STEWART 
                    9. THE SEARCH: PERSONAL PAPERS BY LATIFA AL-ZAYYAT, TRANSLATED BY SOPHIE BENNETT 
                
                                7. Libya
                
                    1. The Return: Fathers, Sons and the Land in Between by Hisham Matar 
                    2. In the Country of Men by Hisham Matar
                    3. The Arab of the Future: A Childhood in the Middle by Riad Sattouf
                    4. Under the Tripoli Sky by Kamal Ben Hameda 
                    5. The Shadows of Ghadame by Joëlle Stolz
                    6. Maps of the soul by Ahmed Fagih
                    7. Gold dust by Ibrahim Al-koni
                    8. Green book by Muammmar Gaddafi
                    9. The lion's Gane by Nelson DeMille
                    10. The puppet by Ibrahim Al-koni
                
                                8. South Africa
                
                    1. Bitter fruit by Achmat Dangor
                    2. The promise by Damon Galgut
                    3. Portrait with keys by Ivan Vladislavic
                    4. Young blood by Sifiso Mzobe
                    5. The Dark Flood by Deon Meyer
                    6. The scramble for Africa by Thomas Pakenham
                    7. The quality of mercy by Siphiwe Gloria Ndiovu
                    8. Another country by Karel Schoeman, 1984
                    9. Zoo city by Lauren Beukes
                    10. The grass is singing by Doris Lessing
                            
                                9. Zambia
                
                    1. The old draft by Namwali Serpell
                    2. A cowrie of hope by Binwell Sinyangwe
                    3. Patchwork by Ellen Banda-Aaku
                    4. Kumukanda by Kayo Chingonyi
                    5. Travel light, move fast by Alexandra Fuller
                    6. The unheard by Josh Swiller
                    7. North of south by Shiva Naipul
                    8. The mourning bird by Mubanga Kalimamukwento
                    9. Fever Dream by Lincoln Child
                    10. The ukiwi Road by Dervla Murphy
                
                                10. DRC
                  
                    1. The year of the gorilla by George Schaller
                    2. Congo by Michael Crichton
                    3. Refugee: A memoir by Emmanuel Mbolela
                    4. The poisonwood Bible by Barbara Kingsolver
                    5. Heart of darkness by Joseph Conrad
                    6. Tram 83 by Fiston Mwanza Mujila
                    7. Mr. Fix it by Richard Ali A Mutu
                    8. Maison rouge by Leolina Leila Juma
                    9. No palce to call home by J.J Cola
                    10. Congolese Wiskunde by In Koli Jean Bofane
                """)
            book_name = input("what is the name of the book:").lower()
            retrieve_rate = "SELECT AVG(rating) FROM book_ratings WHERE title = %s"
            mycursor.execute(retrieve_rate, (book_name,))
            average_rating = mycursor.fetchone()
            print(f"the average rating of {book_name} is {average_rating}")

        elif self.__selection == 11:
            title = input("Enter the title of the book:")
            retrieve_reviews = "SELECT review FROM book_reviews WHERE book_title = %s"
            mycursor.execute(retrieve_reviews, (title,))
            reviews = mycursor.fetchall()

            if not reviews:
                print("No reviews found for this book")
            else:
                for book_review in reviews:
                    split_review = book_review[0].split("|")
                    lines = '\n'.join(split_review)
                    print(lines)


if __name__ == "__main__":
    while True:
        welcome_text = """ Explore a diverse collection of books authored by Africans in this program. 
    Simply input the country number to discover a curated selection of literature from the desired African nation.
    ----------------------------------------------------------------------------------------------------------
                            1. Rwanda
                            2. Kenya
                            3. Ethiopia
                            4. Nigeria
                            5. Ghana
                            6. Egypt
                            7. Libya
                            8. South Africa
                            9. Zambia
                            10. DRC
                        
                            Choose 11 to see the rating of a book and 12 to see reviews 
                        """
        print(welcome_text)
        countries = ["Rwanda", "Kenya", "Ethiopia", "Nigeria", "Ghana", "Egypt", "Libya", "South Africa", "Zambia", "DRC", "Reviews"]
        choice = int(input("Input a number: ")) - 1
        obj = Menu(choice)
        obj.display_books()
        answer = input("Do you want to rate a book?(Yes/No): ").lower()
        if answer == "yes":
            book_title = (input("enter the book you would like to rate:")).lower()
            rating = int(input("enter the rating(1-5): "))

            try:
                insert_query = "INSERT INTO book_ratings (title, rating) VALUES(%s, %s)"
                mycursor.execute(insert_query, (book_title, rating))
                mydb.commit()
                print("rating successful!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

        answer2 = input("Do you want to review a book ?").lower()
        if answer2 == "yes":
            try:
                review_book = input("Enter the book you would like to review:")
                review = input("Enter your review:") + "|"
                insert_review = "INSERT INTO book_reviews (book_title, review) VALUES(%s, %s)"
                mycursor.execute(insert_review, (review_book, review))
                mydb.commit()
                print(f"{review_book} reviewed successfully!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                mydb.close()







    
