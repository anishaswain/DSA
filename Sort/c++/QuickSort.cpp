/*
Quick uses Divide and Conquer Algorithm (similar to merge sort)
also partition algorithm
time complexity : Average - O(nLogn), Worst Case - O(N^2clang )
*/

#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int> &a, int s, int e) {
	int i = s-1;
	for(int j=s;j<e;j++) {
		if(a[j] < a[e]) {
			i++;
			swap(a[i], a[j]);
		}
	}

	swap(a[i+1], a[e]);
	return i+1;
}

void quicksort(vector<int> &a, int s, int e) {
	//base case
	if(s>=e) {
		return;
	}
	int pivot = partition(a, s, e);
	quicksort(a, s, pivot - 1);
	quicksort(a, pivot + 1, e);
}

int main() {
	
	vector<int> arr{10, 5, 2, 0 ,7, 6, 4};
	//cout<< arr.size() << endl;
	quicksort(arr, 0, arr.size() - 1);
	
	//print the sorted arr
	for(int x: arr) {
		cout<< x<<",";
	}

	return 0;
}