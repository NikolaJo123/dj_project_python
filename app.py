# imports go here
from  parser import Parser



def main():
   """Main entry"""
   with open("example.txt", "r") as file:
      p1 = Parser(file)
      
      sentences, snt_count, char_count = p1.parsing()

      print(sentences, "\n\n")

      print(f'Found total of {snt_count} sentences. With total of {char_count} character in the file {file.name}')


if __name__ == '__main__':
   main()
   
