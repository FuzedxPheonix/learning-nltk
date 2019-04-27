from nlp_functions import *
def main():

	test_file_1 = NLP_TEST_FILE("randomfile.txt")

	test_file_1.tokenize_raw_file()
	
	fw = test_file_1.freq_words( 4, 10)

	print(fw)
	

if __name__ == '__main__':
	main()