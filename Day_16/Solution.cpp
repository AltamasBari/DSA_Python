vector<int> help_classmate(vector<int> arr, int n)
{
    // Your code goes here
    vector<int> v;
    int cnt;
    for (int i = 0; i < (arr.size() - 1); i++)
    {
        for (int j = i + 1; j < arr.size(); j++)
        {
            if (arr[j] < arr[i])
            {
                v.push_back(arr[j]);
                cnt = 0;
                break;
            }
            else
                cnt = 1;
        }
        if (cnt == 1)
        {
            v.push_back(-1);
        }
    }
    v.push_back(-1);
    return v;
}