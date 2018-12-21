#We've given you a file called "top500.txt" which contains
#the name and lifetime gross revenue of the top 500
#films at the time this question was written. 
#
#Each line of the given file is formatted like so:
# <name>\t<gross revenue in dollars>
#
#In other words, you should call .split("\t") to split
#the line into the movie name (the first item) and the
#gross (the second item).
#
#Unfortunately, these movies are not in order. Write a 
#function called "sort_films" that accepts two parameters:
#a string of a source filename and a string of a
#destination filename. Your function should open the
#source file and sort the contents from greatest gross
#revenue to least gross revenue, and write the sorted
#contents to the destination filename. You may assume the
#source file is correctly formatted.


#Write your function here!

def sort_films(input_filename, output_filename):
	movie_data=open(input_filename,"r")
	list_of_movies=[]
	for movie in movie_data:
		list_of_movies.append(movie.strip().split("\t"))
	list_of_movies.sort(reverse=True, key = lambda lst: int(lst[1]))
	#print(list_of_movies)
	movie_data.close()
	
	output_file = open(output_filename, "w")
	for movie in list_of_movies:
		output_str="\t".join(movie)
		output_file.write(output_str+"\n")
        #print(output_str, file=output_file)  ...This is equivalent to the line above.
        #apparently, only strings can be written to text files.  Tuples and Lists need to be converted to str.
	output_file.close() 	
#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")
