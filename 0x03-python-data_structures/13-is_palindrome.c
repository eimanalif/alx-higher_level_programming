#include "lists.h"
#include <stddef.h>

/**
 *palindrom -  a function in C that checks if a singly linked list is a palindrome.
 *Description: a function in C that checks if a singly linked list is a palindrome.
 *@head:pointer
 *Return:0 or 1
 */


int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (pa(head, *head));
}



/**
 *pa - function to check palindrme
 *Description:function to check palindrome
 *@head:pointer to head
 *@end: end list
 */


int pa(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (pa(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return(0);
}
