/**
 * @file make_ifs_oxfd.c 
 * @author Gibran Fuentes Pineda <gibranfp@turing.iimas.unam.mx>
 * @date 2015
 *
 * @section GPL
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * General Public License for more details at
 * http://www.gnu.org/copyleft/gpl.html
 *
 * @brief Creates the inverted file from word id files in the Oxford Buildings Dataset.
 */
#include <smh/ifindex.h>

#define VOCABULARY_SIZE 1000000

/**
 * @brief Checks if directory entry is a file
 *
 * @return 1 if it is a file, 0 otherwise
 */
int is_file(const struct dirent *file)
{
     return strcmp(file->d_name, ".") != 0 && strcmp(file->d_name, "..") != 0;
}     

/**
 * @brief Reads every bag-of-features representation file in a directory and
 *        stores it in a database of lists
 *        
 * @return Database of bags-of-features
 */
ListDB make_oxfd_corpus(char *dir)
{
     struct dirent **filenames;
     int number_of_files = scandir(dir, &filenames, is_file, alphasort);

     ListDB corpus = listdb_create(VOCABULARY_SIZE, number_of_files);
     
     uint i;
     for (i = 0; i < number_of_files; i++) {
          if (!(file = fopen(filename,"r"))){
               fprintf(stderr,"Could not read file %s. Skipping . . .\n", filenames[i]);
               continue;
          }

          uint j, nil, words_in_file;
          fscanf(file,"%f %d", &nil, &words_in_file);
          for (j = 0; j < words_in_file; j++){
               if (fscanf(file,"%d %lf %lf %lf %lf %lf", &id, &x, &y, &a, &b, &c) != 6){
                    fprintf(stderr,"Could not read id = %d x = %lf, y = %lf a = %lf, b = %lf, c = %lf from %s\n", id, x, y, a, b, c, filename);
                    continue;
               } else {
                    Item item = {id, 1};
                    list_push(&corpus->lists[i], item);
               }
          }
          
          if (close(file)){
               fprintf(stderr,"Waning: Error while closing file %s\n", filename);
               continue;
          }     
     }

     return corpus;
}

/**
 * ======================================================
 * @brief Main function
 * ======================================================
 */
int main(int argc, char *argv[])
{
     ifindex_
     return 0;
}

