#include "lists.h"
#include <stddef.h>
/**
 * check_cycle - checks if a singly linked list
 * has a cycle in it
 * @list: pointer to the first box
 *
 * Return: Always 0 (success)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
