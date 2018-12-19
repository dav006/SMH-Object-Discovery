
/**
 * @pfile make_ifs_oxfd.c 
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
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <math.h>

#include <smh/ifindex.h>

#define VOCABULARY_SIZE 1000000

/**
 * @brief Reads every bag-of-features representation file in a directory and
 *        stores it in a database of lists
 *        
 * @return Database of bags-of-features
 */
ListDB make_oxfd_corpus(char *dirpath)
{
     DIR *dir = opendir(dirpath);
     struct dirent *dp;
     char files[5062][1000];
     int number_of_files = 0;
     FILE *pfile;
     
     while ((dp = readdir(dir)) != NULL) {
          if (strcmp(dp->d_name, ".") != 0 && strcmp(dp->d_name, "..") != 0) {
               strcpy (files[number_of_files], dirpath);
               strcat (files[number_of_files], "/");
               strcat (files[number_of_files], dp->d_name);
               number_of_files++;
          }
     }

     ListDB corpus = listdb_create(number_of_files, VOCABULARY_SIZE);
     uint i;
     for (i = 0; i < number_of_files; i++) {
          printf("Processing file %s . . .\n", files[i]);
          if (!(pfile = fopen(files[i],"r"))){
               fprintf(stderr,"Could not read file %s. Skipping . . .\n", files[i]);
               continue;
          }

          uint j, number_of_words;
          double nil;
          if ( fscanf(pfile,"%lf %d", &nil, &number_of_words) != 2 ){
               fprintf(stderr,"Could not read number of words in file %s", files[i]);
               continue;
          }

          
          for (j = 0; j < number_of_words; j++){
               int id;
               double x, y, a, b, c;
               if ( fscanf(pfile,"%d %lf %lf %lf %lf %lf", &id, &x, &y, &a, &b, &c) != 6 ){
                    fprintf(stderr,"Could not read id = %d x = %lf, y = %lf a = %lf, b = %lf, c = %lf from %s\n", id, x, y, a, b, c, files[i]);
                    continue;
               } else {
                    Item item = {id - 1, 1};
                    list_push(&corpus.lists[i], item);
               }
          }
          
          if ( fclose(pfile) ){
               fprintf(stderr,"Warning: Error while closing file %s\n", files[i]);
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
     if (argc < 4) {
          printf("Missing arguments make_ifs_oxfd FILE_WITH_LIST_OF_WORD_FILES CORPUS_FILE INVERTED_FILE");
          exit(-1);
     }

     ListDB corpus = make_oxfd_corpus(argv[1]);     
     listdb_save_to_file(argv[2], &corpus);
     ListDB ifindex = ifindex_make_from_corpus(&corpus);
     listdb_save_to_file(argv[3], &ifindex);
     
     return 0;
}

