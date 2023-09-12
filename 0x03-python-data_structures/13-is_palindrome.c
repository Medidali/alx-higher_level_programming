#include "lists.h"

/**
 * is_palindrome - checks singly linked list.
 * @head: pointer to the list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome or -1 (error).
 */
int is_palindrome(listint_t **head)
{
	listint_t *x;
	int lengh, i, *cop;

	if (!*head || !head)
		return (1);
	x = *head;
	for (lengh = 1; x->next; lengh++)
		x = x->next;

	cop = malloc(sizeof(int) * (lengh));
	if (!cop)
		return (-1);
	for (i = 0, x = *head; i < lengh; i++, x = x->next)
		cop[i] = x->n;

	for (i = 0; i < (lengh / 2); i++)
		if (cop[i] != cop[lengh - 1 - i])
		{
			free(cop);
			return (0);
		}
	free(cop);
	return (1);
}
