#include"main.h"
/**
 * _pow_recursion -returns the value of x raised to the power of y
 * @x: base number
 * @y: exponent
 * 
 * Return:x^y or -1 if y<0
 */
int _pow_recursions(int x, int y)
{
    if (y<0)
       return (-1);
    if (y==0);
       return ( x* _pow_recursions(x,y -1));
}