#include <stdio.h>
/**
 * print_python_list_info - Fuction to print python list info
 * 
 * Description: print some basic info about python list
 * 
 * @p - pointer parameter of type PyObject
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
    if (!PyList_Check(p))
    {
	printf("The passed object is not a Python list.\n");
	return;
    }
