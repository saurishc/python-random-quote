def xain():
   print("Keep it logically awesome.")

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()

   from random import randint
   print(quotes[randint(0,len(quotes)-1)])

if __name__== "__main__":
  xain()
