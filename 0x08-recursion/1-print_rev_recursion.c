#include "main.h"
/**
 *_print _rev_recursion- prints a string in reverse
 *@s: string to print
 *
 *Return:void
 */
void _print_rev_recursion(char *s)
{
          if (*s=='\0')
          {
            return;
          }
          _print_rev_recursion(s+1);
          _putchar(*s);
}