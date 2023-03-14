#include "lists.h"
#include <stdlib.h>

/**
 * insert_code - inserts node in sorted list
 * @head: address of head pointer
 * @number: number to insert
 * Return: inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old, *new, *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	old = NULL;
	current = *head;

	for (; current != NULL && current->n < number;)
	{
		old = current;
		current = current->next;
	}

	new->next = current;

	if (old != NULL)
		old->next = new;
	else
		*head = new;

	return (new);
}
