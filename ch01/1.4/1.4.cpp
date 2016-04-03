
#include <string>
#include <stdlib.h>

using namespace std;


//this is the simplest implementation, better performance if used ctrings
//worse case is O(n2) which isn't good!
//c++ style, against the rules!
string replaceSpace(string str)
{
    string retStr = str;
    size_t spacePos = 0;
    while (string::npos != (spacePos = retStr.find(' '))){ //find is O(N) each time
        retStr.replace(spacePos, 1, "%20"); // O(N) and creating a brand new string each time, i think?
    }
    return retStr;
}

void replaceCSpace(char* str, int len) {
    printf("replaceCSpace(%s, %d)\n", str, len);
    char* str2 = (char*)malloc(len+1);
    
    int nsi = 0;  //new string index, where to put next char
    for (int i=0; i<len; i++) {
        if (str[i] == ' ') {
            strcpy(str2+nsi, "%20");
            nsi += 3;
        } 
        else {
            str2[nsi] = str[i];
            nsi++;
        }
    }

    printf("\ts2: %s\n", str2);
    delete str2; 
    return;
}

int main()
{

    printf("\t C++ style strings... \n");
    string s = "nospace";
    printf("||%s||%s||\n", s.c_str(), replaceSpace(s).c_str());
    s = "one space";
    printf("||%s||%s||\n", s.c_str(), replaceSpace(s).c_str());
    s = " lots of  spaces    ";
    printf("||%s||%s||\n", s.c_str(), replaceSpace(s).c_str());
    s = "";
    printf("||%s||%s||\n", s.c_str(), replaceSpace(s).c_str());

    printf("\t char array style strings... \n");
    char* s1 = (char*)calloc(100, sizeof(char));
    strcpy(s1, "as df");
    printf("as df: %s\n", s1);
    replaceCSpace(s1, 5); 
    
    delete s1;

  return 0;
}
