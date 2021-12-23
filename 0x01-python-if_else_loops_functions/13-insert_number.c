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
	if (head == NULL || *head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	current = *head;
	while (current != NULL)
	{
		if (current->n > number)
			break;
		prev = current;
		current = current->next;
	}
	new_node->next = current;
	prev->next = new_node;
	return (*head);
}
