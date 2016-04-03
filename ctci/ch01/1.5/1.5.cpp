// chapter 1 question 5
/*
implment a method to perform basic string compressions using the counts of repeated characters. for example the string aabcccccaaa would become a2b1c5a3
*/

//assume all letters

#include <string>
#include <iostream>
#include <assert.h>

using namespace std;

//bool isLetter(string s_c)
bool isLetter(char& s_c)
{
  //const char c = *s_c.c_str();
  char c = s_c;
  if ( (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) return true;

  return false;
}

string compress(string s)
{
    printf("compress(%s)\n", s.c_str());
  string strComp = "";
  size_t sLen = s.length();
  char curLetter = s[0];
  unsigned int repeatCtr = 0;

  for (size_t i = 0; i<sLen; i++) {
    if (!isLetter(s[i])) {
      cout << "your string has non-letter characters!" << endl;
      exit(1);
    }
    else {
      if ( s[i] != curLetter ) { //found new letter, write out
        strComp.append(1,curLetter);
        strComp += std::to_string(repeatCtr);  //c++ 11!!
        curLetter = s[i];
        repeatCtr = 1;
        continue;
      }
      curLetter = s[i];
      repeatCtr++;
    }
  }
    strComp.append(1,curLetter);
    strComp += std::to_string(repeatCtr);  //c++ 11!!

    printf("\t%s\n", strComp.c_str());
  return strComp;
}

int main()
{
  string str;

  str = "aabbccc";
    compress(str);

  str = "aabcccccaaa";
    compress(str);

  str = "aab%ccccaaa";
    compress(str);

  return 0;
}
