class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(i, path, cur):
            if cur == target:
                result.append(path[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if cur + candidates[j] > target:
                    break
                path.append(candidates[j])
                backtrack(j + 1, path, cur + candidates[j])
                path.pop()
        
        backtrack(0, [], 0)
        return result