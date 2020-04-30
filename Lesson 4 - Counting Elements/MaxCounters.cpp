// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

vector<int> solution(int N, vector<int> &A)
{
    // write your code in C++14 (g++ 6.2.0)
    vector<int> counters(N);
    int old_max{0};
    int max {0};
    
    for(const auto a : A)
    {
        if (a > N)
        {
            old_max = max;
            continue;
        }
        
        int& current_counter = counters[a-1];
        if(current_counter < old_max)
            current_counter = old_max + 1;
        else
            ++current_counter;
            
        if (max < current_counter)
                ++max;
    }
    
    for(auto& c : counters)
    {
        if (c < old_max)
            c = old_max;
    }
    
    return counters;
}
