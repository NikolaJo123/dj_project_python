# imports go here
from  parser import Parser



def main():
   """Main entry"""
   with open("example.txt", "r") as file:
      p1 = Parser(file)
      
      sentences = p1.parsing()

      print(sentences, "\n\n\n")

      print(f'Found total of {sentences["stats"]["total_sentences"]} sentences. With total of {sentences["stats"]["total_chars"]} character in the file {file.name}')


if __name__ == '__main__':
   main()
   
