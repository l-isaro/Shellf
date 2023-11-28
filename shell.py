class Menu:
    """Displays the countries to choose from."""
    

    def __init__(self, selection):
        """initialize selection"""
        self.__selection = selection
    
    @property
    def selection(self):
        """assigns selction to selection"""
        return self.__selection

    @selection.setter
    def selection(self, value):
        """conditions"""
        if value > 10 or value < 1:
            raise ValueError("selection out of range")    
        
        self.__selection = value

    def display_books(self):
        print(self.__selection, type(self.__selection))
        if self.__selection == 0:
            print(""" 1. Between Wild and Free - Caroline Numuhire
                         ------------------------------------------
                         Store: https://www.amazon.com/Between-Wild-Free-Caroline-Numuhire/dp/9997777948
                      2. Barefoot in Germany - Tete Loeper 
                         ----------------------------------
                         Store: https://www.amazon.com/Barefoot-Germany-Tete-Loeper/dp/3000674659
                      3. The girl who smiled beads - Clementine Wamariya 
                         --------------------------------------------------------------------------
                         Store: https://www.amazon.com/Girl-Who-Smiled-Beads-Story/dp/0451495322
                      4. The Barefoot – Scholastique 
                         ---------------------------------------------------------------------------
                         

                      5. From Red Earth: A Rwandan Story of Healing and Forgiveness – Denise Uwimana
                      6. Scars that Shape Us – Divine Akimana 
                      7. Love tails – Yves Muhizi
                      8. First Creation - Sandra Nadege
                      """)
            book = int(input("Enter the number of the book you would like to get more information on:"))

        elif self.__selection == 1:
            print("""1. petals of blood by ngũgĩ wa thiong’o
                     2. the river and the source by margaret a. Ogola
                     3. one day i will write about this place: a memoir by binyavanga wainaina 
                     4. dust by yvonne adhiambo owuor
                     5. the promised land by grace ogot
                     6. nairobi heat by mukoma wa ngugi
                     7. population, tradition, and environmental control in colonial kenya by martin s. Shanguhyia
                     8. facing mount kenya by jomo kenyatta
                     9. history of resistance in kenya 1884-2002 by maina wa kĩnyattĩ
                  """)
        elif self.__selection == 2:
            print("""1. cutting for stone by abraham verghese
                     2. the shadow king by maaza mengiste
                     3. the beautiful things that heaven bears by dinaw mengestu
                     4. open my eyes, that i may see marvellous things by alice allan
                     5. beneath the lion’s gaze by maaza mengiste
                     6. addis ababa noir by various
                     7. the wife’s tale by aida edemariam
                     8. shallow graves: a memoir of the ethiopia-eritrea war by richard reid
                     9. i want to die with a flag. ethiopia: my delusions and disillusionment by vartkes nalbandian
                     10. held at a distance: a rediscovery of ethiopia by rebecca g. Haile
                  """)
        elif self.__selection == 3:
            print(""" 1. COCONUT: A BLACK GIRL, A WHITE FOSTER FAMILY, AND THE SEARCH FOR BELONGING AND IDENTITY BY FLORENCE OÒLAÌJIÌDEÌ
                      2. HOPE AND GLORY BY JENDELLA BENSON
                      4. YOU MADE A FOOL OF DEATH WITH YOUR BEAUTY BY AKWAEKE EMEZI
                      5. A COASTLINE IS AN IMMEASURABLE THING: A MEMOIR ACROSS THREE CONTINENTS BY MARY-ALICE DANIEL
                      6. THE LEGACY OF MOLLY SOUTHBOURNE (THE MOLLY SOUTHBOURNE TRILOGY BOOK 3) BY TADE THOMPSON
                      7. WHERE THE CHILDREN TAKE US: HOW ONE FAMILY ACHIEVED THE UNIMAGINABLE BY ZAIN E. ASHER
                      8. NOTES FROM A YOUNG BLACK CHEF BY KWAME ONWUACHI WITH JOSHUA DAVID STEIN
                      9. WAHALA: A NOVEL BY NIKKI MAY
                      10. OPERATION SISTERHOOD BY OLUGBEMISOLA RHUDAY-PERKOVICH
                   """)  
        elif self.__selection == 4:
            print("""1. Changes: A Love Story by Ama Ata Aidoo
                     2. Tail of the Blue Bird BY NII AYIKWEI PARKES
                     3. b""")

        elif self.__selection == 5:
            print("""1. TREASURE TROVE OF BENEFITS AND VARIETY AT THE TABLE EDITED AND TRANSLATED BY NAWAL NASRALLAH
                     2. BRAINS CONFOUNDED BY THE ODE OF ABU SHADUF EXPOUNDED EDITED AND TRANSLATED BY HUMPHREY DAVIES
                     3. THE ESSENTIAL TAWFIQ AL-HAKIM ED. DENYS JOHNSON-DAVIES
                     4. THE DAYS BY TAHA HUSSEIN, TRANSLATED BY E.H. PAXTON, HILARY WAYMENT, KENNETH CRAGG
                     5. THE CALL OF THE CURLEW BY TAHA HUSSEIN, TRANSLATED BY A. B. AS-SAFI
                     6. MIRAMAR BY NAGUIB MAHFOUZ, TRANSLATED BY FATMA MOUSSA MAHMOUD
                     7. THE OPEN DOOR BY LATIFA AL-ZAYYAT, TRANSLATED BY MARILYN BOOTH
                     8. THE MAN WHO LOST HIS SHADOW BY FATHY GHANEM, TRANSLATED BY DESMOND STEWART 
                     9. THE SEARCH: PERSONAL PAPERS BY LATIFA AL-ZAYYAT, TRANSLATED BY SOPHIE BENNETT 
                     """)
        elif self.__selection == 6:
            print(""" 1. """)
if __name__ == "__main__":
    welcome_text = """ Wecome to Shellf. We have multiple African books. you can choose based off of the country you prefer
                    ----------------------------------------------------------------------------------------------------
                    1. Rwanda
                    2. Kenya
                    3. Ethiopia
                    4. Nigeria
                    5. Ghana
                    6. Egypt
                    7. Libya
                    8. South Africa
                    9. zambia
                    10. DRC
                    """
    print(welcome_text)
    countries = ["Rwanda", "Kenya","Ethiopia", "Nigeria","Ghana","Egypt","Libya", "South Africa", "Zambia", "DRC"]
    selection = int(input("Input a number:")) - 1
    obj = Menu(selection)
    obj.display_books()
    print(countries[obj.selection])
    