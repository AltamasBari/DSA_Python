string Reduced_String(int k, string s)
{
    // Your code goes here
    vector<pair<char, short>> st;
    for (auto p : s)
    {
        if (st.empty() || st.back().first != p)
            st.push_back({p, 0});
        if (++st.back().second == k)
            st.pop_back();
    }
    string res;
    for (auto &p : st)
        res += string(p.second, p.first);

    return res;
}