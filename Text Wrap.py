import textwrap

def wrap(string, max_width):
    i , j = 0, max_width
    while len(string) >= max_width + j:
        print(string[i:j])
        i = j 
        j += max_width
    print(string[i:j])
    return(string[j:])
     
if __name__ == '__main__':
