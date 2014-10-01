#include <stdio.h>
#include <conio.h>

int binarySearch(int* A, int key, int start, int end)
{
	if (start > end)
		return start;

	else
	{
		int mid = (int)((start + end) / 2);
        if (A[mid] == key)
        	return mid;
        else if (key < A[mid])
        	return binarySearch(A, key, start, mid-1);
        else
        	return binarySearch(A, key, mid+1, end);
	}
}


void binaryInsertionSort(int* A, int size)
{
    int i = 1;
    int index;

    while(i<size)
    {
        index = binarySearch(A, A[i], 0, i);

        if(index < i)                                             //Shift only if the new index comes before the current index
        {
            int temp = A[i];
            int j = i-1;

            while (j >= index)
            {
                A[j+1] = A[j];
                j -= 1;
            }
            A[index] = temp;
        }
        i += 1;
    }
}


void merge(int* A, int start, int mid, int end)
{
	int lenA = end - start + 1;
	int temp[lenA];
    int i=start, j = mid + 1, k=0;

    while(i <= mid && j <= end)
    {
        if(A[i] < A[j])
        {
            temp[k] = A[i];
            k += 1;
            i += 1;
        }
        else
        {
            temp[k] = A[j];
            k += 1;
            j += 1;
        }
    }

        while(i <= mid)
        {
        	temp[k] = A[i];
        	k += 1;
        	i += 1;
        }

        while(j <= end)
        {
        	temp[k] = A[j];
        	k += 1;
        	j += 1;
        }
	A = temp;
  }


void mergeSort(int* A, int start, int end, int threshold)
{
    if (start>end)
        return;

    int lenA = end - start + 1;
    if ((end - start + 1) <= threshold)
        binaryInsertionSort(A, lenA);
    else
    {
        int mid = (int)((start + end) / 2);
        mergeSort(A, start, mid, threshold);
        mergeSort(A, mid + 1, end, threshold);
        merge(A, start, mid, end);
    }
}


int main()
{
	int A[5] = {5,1,3,2,4};
	mergeSort(A, 0, 4, 0);
	int i;
	for(i=0; i< 5; i++)
		printf("%d\n", A[i]);

	return 1;
}
