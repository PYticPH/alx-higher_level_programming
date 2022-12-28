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
    listint_t *temp;

    temp = list;
    while (list != NULL)
    {
	if (temp == list->next)
	    return (1);

	list = list->next;
    }

    return (0);
}
