#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        int len;
        scanf("%d", &len);
        int arr[len];
        for (int j = 0; j < len; j++)
        {
            scanf("%d", &arr[j]);
        }

        if (len < 3)
        {
            printf("-1\n");
            continue;
        }
        if (arr[len - 1] == arr[len - 2] && arr[len - 2] == arr[len - 3])
        {
            printf("%d\n", arr[len - 1]);
            continue;
        }
        int count = 1;
        for (int j = len - 1; j > -1; j--)
        {
            for (int k = 0; k < j; k++)
            {
                if (arr[k] == arr[j])
                {
                    count++;
                }
                if (count == 3)
                {
                    printf("%d\n", arr[j]);
                    break;
                }
            }
            if (count == 3)
            {
                break;
            }
            count = 1;
        }

        if (count < 3)
        {
            printf("-1\n");
        }
        // for (int j = 0; j < len; j++)
        // {
        //     printf("%d, ", arr[j]);
        // }
    }

    return 0;
}
