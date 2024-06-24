/*
*
* pyfmt
* string formatting python library
*
* aceinet (2022-present)
*
*/

#define _GNU_SOURCE
#include <stdarg.h>
#include <stdio.h>

char* default_fmt(char* text, ...){
  char* dst;

  va_list v;
  va_start(v, text);

  vasprintf(&dst, text, v);

  va_end(v);

  return dst;
}
