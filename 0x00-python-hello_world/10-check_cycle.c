#include "lists.h"

/**
 * check_cycle - Function to test if a linked list is circular
 *
 * @list: linked list to test
 *
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
    listint_t *temp_x1, *temp_x2;

    if (list == NULL)
	return (0);

    temp_x1 = list;
    temp_x2 = list;
    while (temp_x2 != NULL && temp_x2->next != NULL)
    {
	temp_x1 = temp_x1->next;
	temp_x2 = temp_x2->next->next;
	if (temp_x2 == temp_x1)
	    return (1);
    }

    return (0);
}
