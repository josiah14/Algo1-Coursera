module MergeSort (mergesort) where

mergesort :: [Int] -> [Int]
mergesort list =
  case list
  of []        -> []
     (_:rest)
      | null rest -> list
      | otherwise -> conquer (mergesort left) $ mergesort right
        where (left, right) = divide list

-- private functinons
divide :: Ord a => [a] -> ([a], [a])
divide xs = splitAt (length xs `div` 2) xs

conquer :: Ord a => [a] -> [a] -> [a]
conquer xs ys =
  case (xs, ys) of
    ([], _) -> ys
    (_, []) -> xs
    (x0:xTail, y0:yTail)
      | x0 < y0   -> x0:conquer xTail ys
      | otherwise -> y0:conquer xs yTail

