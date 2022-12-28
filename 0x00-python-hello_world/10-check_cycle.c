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
    unsigned int nodeCount = 0;

    temp = list;
    while (list != NULL)
    {
	if (temp == list->next && nodeCount > 1)
	    return (1);

	list = list->next;
	nodeCount++;
    }

    return (0);
}
