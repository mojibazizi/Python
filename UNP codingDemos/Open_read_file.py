def open_read_file(file):
    '''Opens the given file, reads each line and prints to the console. Closes the given file.'''
    
    #Opens the given file in read mode 
    f = open(file, "r")
    print(type(f)) #print the type of the stream f

    cnt = 0
    #reads and prints each line in f, while there is a line to read 
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
        cnt += 1
    print('')
    print('there are', cnt, 'lines in the file ')
    f.close()

def open_read_append_new_file(file1, file2):
    '''Opens the first file, and reads all lines into a list.
    Reverses the lines and appends them to the second file'''

    #open the first file in read mode 
    with open(file1) as fin:

        #read all lines into a list
        lst = fin.readlines()

        #reverse the list
        lst.reverse()
        #Open second file for appending 
        Jo = open(file2, 'a')

        #Write reverse lines to second file 
        Jo.writelines(lst)

        #close the second file
        Jo.close()

def open_read_append_same_file(file):
    '''Opens the given file and reads all lines as a list.
    Appends lines to same file'''

    #Open the file for reading and writing.
    f = open(file, 'r+')
    #read all lines into a list a list
    lst = f.readlines()
    #Updating list for appending back to same file
    lst.insert(0, '\n')
    lst.insert(0, "here's some new text")
    lst.insert(0, '\n')

    #Append the lines back to same file 
    f.writelines(lst)
    #Close the file
    f.close()

def open_read_write_new_file(file1, file2):
    '''Opens the first file and reads all text as a string.
    Copies or writes all text to the second file'''

    #open the first file 
    with open(file1) as fin:
        #read all lines as a single string 
        text = fin.read()
        #Open second file in write mode
        fout = open(file2, 'w')
        #write single string to second file
        fout.write(text)
        fout.close()
        



def main():
    open_read_write_new_file('news.txt', 'news_copy.txt')
    #open_read_file('news.txt')
    #open_read_append_new_file('news.txt', 'reverse_news.txt')
    #open_read_append_same_file('news.txt')
if __name__ == '__main__':
    main()