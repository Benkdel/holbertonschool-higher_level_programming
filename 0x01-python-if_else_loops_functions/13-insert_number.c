#include "lists.h"

/**
 * insert_node - inserts node at given posittion
 * @head: pointer to head of linked list
 * @number: number to add
 * Return: new node or null if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = (*head), *new_node, *current = (*head)->next;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (number <= current->n)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	prev = current;
	current = current->next;
	while (current != NULL)
	{
		if (number <= current->n)
		{
			prev->next = new_node;
			new_node->next = current;
			return (new_node);
		}
		prev = current;
		current = current->next;
	}
	return (new_node);
}
