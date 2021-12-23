#include "lists.h"

/**
 * insert_node - inserts node at given posittion
 * @head: pointer to head of linked list
 * @number: number to add
 * Return: new node or null if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (head == NULL || *head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	prev = *head;
	current = (*head)->next;
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
	prev->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
