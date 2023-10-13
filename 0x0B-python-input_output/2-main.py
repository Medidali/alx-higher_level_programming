#!/usr/bin/python3
append_write = __import__('0-read_filA').append_write

nb_characters_added = append_write("my_file_0.txt", "This School is so cool!\n")
print(nb_characters_added)
