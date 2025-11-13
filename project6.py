import os

class JournalManager:
    
    def __init__(self):
        self.file="journal.txt"
        
    def add_entry(self):
        add=input("Enter your journal entry : ")
        
        try:
            self.file=open("journal.txt","a")
            self.file.write("\n"+add)
            self.file.close()
            print("\nEntry added successfully!")
            
        except Exception:
            print("cannot added successfully!")
            
        else:
            print("finally entry added successfully!")
            
        finally:
            print("Execution completed.")
            
    def view_entry(self):
        try:
            self.file=open("journal.txt","r")
            print("Your journal Entries : ")
            print("-----------------------------------")
            self.lines=self.file.readlines()
            for self.li in self.lines:
                print(self.li)
            self.file.close()
            print("\nView all entry successfully!")
            
        except Exception:
            print("No journal entries found. Start by adding a new entry!\n")
            
        else:
            print("finally view all successfully!")
            
        finally:
            print("Execution completed.")   

    def search_entry(self):
        search=input("Enter a keyword from journal entry to view that specific entry: ")
        try:
            self.file=open("journal.txt","r")
            self.lines=self.file.readlines()
            for self.li in self.lines:
                if search in self.li:
                    print(self.li)
         
                else:
                    print("No matching entries found")
                    self.file.close()
            
        except Exception:
            print(f"no entries were found for the keyword : {search}") 
        
        else:
            print("\nfinally search successfully!")
            
        finally:
            print("Execution completed.")    
                  
    def delete_entry(self):
        delete=input("Are you sure you want to delete all enteries (yes/no) : ")
        try:
            if delete=="yes":
                self.file=open("journal.txt","w")
                self.file.close()
                print("\nAll journal entries have been deleted!")
                
            else:
                print("No entries delete.")
                
        except Exception:
            print("No journal entries to delete.")
      
        else:
            print("finally deleted successfully!")
            
        finally:
            print("Execution completed.")          
        
while True:
    
    print("\nWelcome to Personal Journal Manager!\n")
    
    print("Please select an option : \n")
    print("1.Add a new Entry")
    print("2.View all Entries")
    print("3.Search for an Entry")
    print("4.Delete all Entries")
    print("5.Exit\n")
    
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        obj=JournalManager()
        obj.add_entry()
        
    elif choice==2:
        obj=JournalManager()
        obj.view_entry()
        
    elif choice==3:
        obj=JournalManager()
        obj.search_entry()
        
    elif choice==4:
        obj=JournalManager()
        obj.delete_entry()
        
    elif choice==5:
        print("Exit")
        break
    
    else:
        print("Your choice is not valid!")
        
    
        