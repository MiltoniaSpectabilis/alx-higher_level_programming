#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *tmp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast)
		slow = slow->next;

	prev->next = NULL;
	tmp = reverse_list(&slow);

	while (*head && tmp)
	{
		if ((*head)->n != tmp->n)
			return (0);
		*head = (*head)->next;
		tmp = tmp->next;
	}

	return (1);
}
