#include "lists.h"
#include <stdlib.h>
/**
 * *insert_node - function in C that inserts a
 * number into a sorted singly linked list
 * @head: pointer to first node
 * @number: data in the node
 * Return: Alwaya 0 (success)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new_node = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
return (new_node);
}
