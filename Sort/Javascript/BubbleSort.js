function bubbleSort(elements) {
    let allSorted = false
    while (!allSorted) {
        allSorted = true
        for (let i = 0; i < elements.length; i++) {
            if (elements[i] > elements[i+1]) {
                allSorted = false;
                [elements[i], elements[i+1]] = [elements[i+1], elements[i]]
            }
        }
    }
    return elements
}

module.exports = { bubbleSort }