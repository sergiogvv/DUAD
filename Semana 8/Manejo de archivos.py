def open_and_print_file(path):
	with open(path) as file:
		print(file.read())


def sort_lines_in_file(path):
	with open(path) as file:
          list_of_lines = file.readlines()
          list_of_lines.sort()
          return list_of_lines


def write_sorted_lines_to_file(list,path):
    with open(path,'a') as file:
        for line in list:
            file.write(line)


def main():
    
    open_and_print_file('C:/Users/sergi/OneDrive/Documents/Lyfter/Semana 8/10_songs.txt')
    sorted_song_lines = sort_lines_in_file('C:/Users/sergi/OneDrive/Documents/Lyfter/Semana 8/10_songs.txt')
    write_sorted_lines_to_file(sorted_song_lines,'C:/Users/sergi/OneDrive/Documents/Lyfter/Semana 8/10_songs_sorted.txt')
    print('\n\n')
    open_and_print_file('C:/Users/sergi/OneDrive/Documents/Lyfter/Semana 8/10_songs_sorted.txt')


if __name__ == "__main__":
    main()