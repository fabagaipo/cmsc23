#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_CHAR 1000
#define MAX_PAR 5

// A program that shows how we can use pointers to represent details in a document.

//initializing structures
typedef struct word{
        char* data;
}word;

typedef struct sentence{
	word* data;
	int word_count;
}sentence;

typedef struct paragraph{
	sentence* data;
	int sentence_count;
}paragraph;


typedef struct document{
	paragraph* data;
	int paragraph_count;
}document;


//input functions
char* get_input();

//main functions
document initialize_document(document);
paragraph kth_paragrah(document, int);
sentence kth_sentence_in_mth_paragraph(document, int, int); 
word kth_word_in_mth_sentence_in_nth_paragragh(document, int, int, int);
document assign_document(char*);

//printing functions
void parPrint(paragraph);
void senPrint(sentence);
void worPrint(word);

int main(){
	char* input_text = get_input();
	document Doc = assign_document(input_text);

	int queries;
	scanf("%d", &queries);

	int k, m, n, type;
	paragraph par;
	sentence sen;
	word wor;
	while (queries--){
		scanf("%d", &type);
		switch (type){
			case 1:
				scanf("%d", &k);
				par = kth_paragrah(Doc, k - 1);
				parPrint(par);
				printf("\n");
				break;
			case 2:
				scanf("%d %d", &k, &m);
				sen = kth_sentence_in_mth_paragraph(Doc, k - 1, m - 1);
				senPrint(sen);
				printf("\n");
				break;
			case 3:
				scanf("%d %d %d", &k, &m, &n);
				wor = kth_word_in_mth_sentence_in_nth_paragragh(Doc, k - 1, m - 1, n - 1);
				worPrint(wor);
				printf("\n");
				break;
		}
	}
}

char* get_input(){
	int paragraph_count;
	scanf("%d", &paragraph_count);

	char inputs[MAX_CHAR];
	char* output = (char*)malloc(MAX_CHAR*sizeof(char));

	while (paragraph_count--){
		scanf(" %[^\n]s", inputs);
		strcat(output, inputs);
		if (paragraph_count != 0)
			strcat(output, "\n");
	}

	char* final_output = (char*)malloc((strlen(output) + 1) * sizeof(char));
	final_output = output;
	return final_output;
}

document initialize_document(document Doc){
	//initilized for getting their sizes in dynamic allocation
	paragraph para;
	sentence sen;
	word wor;

	Doc.data = (paragraph*)malloc(5 * sizeof(paragraph));
	Doc.paragraph_count = 0;

	//Max 5 paragraphs
	for (int i = 0; i < 5; i++){

		//initializing each paragraphs with 100 max sentences
		Doc.data[i].data = (struct sentence*)malloc(100 * sizeof(sentence));
		Doc.data[i].sentence_count = 0;
		for (int j = 0; j < 10; j++) {

			//initializing each sentences with 500 max words
			Doc.data[i].data[j].data = (word*)malloc(500 * sizeof(word));
			Doc.data[i].data[j].word_count = 0;
			for(int k = 0; k < 50; k++) {

				//initializing each words with 100 max letters
				Doc.data[i].data[j].data[k].data = (char*)malloc(100* sizeof(char));
			}
		}
	}

	return Doc;
}
 
document assign_document(char *text){
	document Doc = initialize_document(Doc);

	//initializing indices
	int p = 0, s = 0, w = 0, l = 0;

	//itirate through out the text's each character
	for (char *ch = text; *ch != '\0'; ch++){
		switch(*ch) {
			case ' ':
				Doc.data[p].data[s].data[w].data[l] = '\0'; //putting a null
				w++; //increasing the index for words
				l = 0; //turn index for letter back to zero for next word to use
				break;
			case '.':
				Doc.data[p].data[s].data[w].data[l] = '\0'; //putting a null
				Doc.data[p].data[s].word_count = ++w; //++w because index starts in 0.
				s++; //going to next sentence
				w = l = 0; //turn index for word and letter back to zero for the next sentence to use
				break;
			case '\n':
				Doc.data[p].sentence_count = s; //the number of senteces in index p paragraph
				p++; //going to next paragraph
				s = w = l = 0; //turn everything to zero for next paragraph
				break;
			default:
				Doc.data[p].data[s].data[w].data[l] = *ch; //words are being formed letter by letter
				l++; //increasing index for next letter
				break;
		}
	}
	Doc.data[p].sentence_count = s; //the number of sentences for the last index
	Doc.paragraph_count = ++p; //total number of paragraph for document. ++p because index starts in 0

	return Doc;	
}


paragraph kth_paragrah(document Doc, int k){
	return Doc.data[k];
}

sentence kth_sentence_in_mth_paragraph(document Doc, int k, int m){
	return Doc.data[k].data[m];
}

word kth_word_in_mth_sentence_in_nth_paragragh(document Doc, int k, int m, int n){
	return Doc.data[k].data[m].data[n];
}


//printing functions
void parPrint(paragraph par){
	int size = par.sentence_count;
	for (int i = 0; i < size; i++) {
		senPrint(par.data[i]);
		printf(".");
	}
}

void senPrint(sentence sen){
	int size = sen.word_count;
	for (int i = 0; i < size; i++) {
		worPrint(sen.data[i]);
		if (i != size - 1)
			printf(" ");
	}
}

void worPrint(word wor){
	printf("%s", wor.data);
}
