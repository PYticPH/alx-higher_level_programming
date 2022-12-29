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

    if (list == NULL)
	return (1);

    temp = list->next;
    while (temp != NULL)
    {
	if (temp == list)
	    return (1);
	temp = temp->next;
    }

    return (0);
}
