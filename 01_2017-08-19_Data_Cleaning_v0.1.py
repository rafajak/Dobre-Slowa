
# coding: utf-8

# In[129]:

# GLANSOWANIE_SOCJOLEKTU(filepath) processes the raw text file (filepath) and saves it as "Dobre Slowa.txt" 
# warning: The output may contain słowa that are not actually dobre. 

# todo:
#    1. Delete words like "HAHAHAHAHAHA", "BYŁO", "GIPHY", "KAAPOK",  etc

def GLANSOWANIE_SOCJOLEKTU(filename = "Surowe Slowa.txt"):


# 1. Opening the text file 
    with open("Surowe Slowa.txt", 'r', encoding='utf-8') as f:
        text = f.read()

        caps_words = str()   # processed words will be added to this string 
        for word in words:
            if word.isupper() == True:
                if word not in ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE",
                                "JULY","AUGUST,""SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]:
                    if not word.startswith(("!","?","(",")","*",":","!","?","(",")","*",":",".")):
                        if not word.endswith(("!","?","(",")","*",":","!","?","(",")","*",":",".")):
                            if len(word)>1:
                                if word not in caps_split:
                                    caps_words = caps_words + str(" ") + str(word)

        text_file = open("Dobre Slowa.txt", "w")
        text_file.write(caps_words)
        text_file.close()

    return caps_words


# In[128]:

GLANSOWANIE_SOCJOLEKTU(filename = "Surowe Slowa.txt")


# In[ ]:



