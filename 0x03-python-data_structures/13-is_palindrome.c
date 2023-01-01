#include "lists.h"

/**
 * is_palindrome - Function to check palindrome
 *
 * Description: check if a linked list is a palindrome
 *
 * @head: heaf of a linked list
 *
 * Return: listint_t
 */

int is_palindrome(listint_t **head)
{
    listint_t *ptr, *ptr2;

    int i, j;
    int count = 0;
 
    if ((*head) == NULL)
	return (1);

    /* count the number of nodes in a linked list */

    ptr = *head;
    ptr2 = *head;
    while (ptr != NULL)
    {
	ptr = ptr->next;
	count++;
    }
    ptr = *head;

    if ((count / 2) == 1)
	return (0);
    
    ptr = *head;
    i = count;

    while (((i - count) + 1) <= (i / 2))
    {
	j = count - 1;
	while (j)
	{
	    ptr2 = ptr2->next;
	    j--;
	}

	if (ptr->n != ptr2->n)
	    return (0);
	ptr2 = *head;
	ptr = ptr->next;
	count--;
    }

    return (1);
}
