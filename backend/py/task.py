from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    # creating a dictionary of parent ids allows us to access them later in constant time, doing this 
    # with two seperate loops instead of a nested loop lets me have O(2n) which simplifies to O(n) instead of O(n^2)
    parentIds = {}
    res = []

    for i, file in enumerate(files):
        parentIds[i] = file.parent
    
    for file in files:
        if file.id not in parentIds.values():
            res.append(file.name)

    return res


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    # loop through files and put all categories into a list, sort by value then key and slice
    categories = {}
    for file in files:
        for category in file.categories:
            categories[category] = categories.get(category, 0) + 1

    sortedCategories = sorted(categories.items(), key=lambda x: (-x[1], x[0]))
    res = [key for key, value in sortedCategories]

    return res[:k]


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    # use recursion to find the highest level parent for each file and compare sizes
    maxSize = 0
    for file in files:
        maxSize = max(getSize(file, files), maxSize)

    return maxSize

def getSize(file, files):
    size = file.size
    for element in files:
        if file.id == element.parent:
            size += getSize(element, files)

    return size

if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    
    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
