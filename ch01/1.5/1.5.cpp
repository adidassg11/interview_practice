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
  string strComp = "";
  size_t sLen = s.length();
  char curLetter = s[0];
  unsigned int repeatCtr = 1;

  for (size_t i = 0; i<sLen; i++) {
    if (!isLetter(s[i])) {
      cout << "your string has non-letter characters!" << endl;
      exit(1);
    }
    else {
      if ( s[i] != curLetter ) { //found new letter, write out
        char buf [50];
        size_t numChars = sprintf(buf, "%d", repeatCtr, 10);
        
        strComp.append(&curLetter);
        strComp.append(string(buf), numChars);
        curLetter = s[i];
        repeatCtr = 1;
        continue;
      }
      curLetter = s[i];
      repeatCtr++;
    }
  }

  return strComp;
}

int main()
{
  string str;

  //TODO: test isLetter
/*
  char x;
  x = '7';
  cout << "isLetter(): " << isLetter(x) << endl;
  x = 'a';
  cout << "isLetter(): " << isLetter(x) << endl;
  x = 'Z';
  cout << "isLetter(): " << isLetter(x) << endl;
  x = '%';
  cout << "isLetter(): " << isLetter(x) << endl;

  return 0;
*/
  

  str = "aabbccc";
  cout << "string: " << str << endl;
  cout << "string compressed: " << compress(str) << endl;

  str = "aabcccccaaa";
  cout << "string: " << str << endl;
  cout << "string compressed: " << compress(str) << endl;

  str = "aab%ccccaaa";
  cout << "string: " << str << endl;
  cout << "string compressed: " << compress(str) << endl;

  return 0;
}
