function sort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let j = i-1
        const anchor = arr[i]
        for (; j >= 0; j--) {
            if (arr[j] < anchor) break
            arr[j+1] = arr[j]
        }
        arr[j+1] = anchor
    }
    return arr
}

console.log(sort([3, 2, 6, 9, 10, 1, 56, 7, 11]))

module.exports = { sort }
