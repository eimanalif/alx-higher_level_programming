#include <Python.h>
#include <stdio.h>

/**
 *print_python_list_info - prints python baisic info
 *Description:prints python basic info
 *@p: A pyobject list
 *Return: void
 */



void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;


	printf("[*] size of the Python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);


	for (i = 0; i < size; i++)
	{
		printf("elment %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
