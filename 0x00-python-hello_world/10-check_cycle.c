#include"lists.h"
#include<stdio.h>
#include<stdlib.h>



/**
 *check_cycle - to check code
 *Description:to check code
 *@list: pointer
 *Return: 0 or 1
 */



int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
			if (slow == fast)
				return (1);
	}
	return (0);
}
