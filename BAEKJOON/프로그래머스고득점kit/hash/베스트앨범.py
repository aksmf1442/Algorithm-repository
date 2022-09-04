def solution(genres, plays):
    genreDict = {}
    genreSumDict = {}
    for i in range(len(genres)):
        genre = genres[i]
        playNum = plays[i]
        genreSumDict[genre] = genreSumDict.get(genre, 0) + playNum

        if genre not in genreDict:
            genreDict[genre] = [(i, playNum)]
            continue

        genreDict[genre].append((i, playNum))

    genreList = []
    for i in genreDict:
        genreDict[i].sort(key=lambda x: (-x[1], x[0]))
        genreList.append(i)

    genreList.sort(key=lambda x: -genreSumDict[x])

    result = []
    for genre in genreList:
        candidate = []
        for idx, value in genreDict[genre]:
            if len(candidate) == 2:
                break
            candidate.append(idx)
        result.extend(candidate)

    return result

# 각 장르별 상위 2개만 뽑기
# result : [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))