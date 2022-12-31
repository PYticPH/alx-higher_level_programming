#include "lists.h"

/**
 * insert_node - Function to insert node in a sorted list
 *
 * head: head of linked list
 * number: integer data of node
 *
 * Return: listint_t
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newNode;
    listint_t *ptr;

    newNode = malloc(sizeof(listint_t));
    if (newNode == NULL)
	return (NULL);

    newNode->n = number;
    newNode->next = NULL;

    if ((*head) == NULL || (*head)->n >= newNode->n)
    {
	newNode->next = *head;
	*head = newNode;
    }
    else
    {
	ptr = *head;
	while (ptr->next != NULL && ptr->next->n < newNode->n)
	{
	    ptr = ptr->next;
	}
	newNode->next = ptr->next;
	ptr->next = newNode;
    }

    return (*head);
}

