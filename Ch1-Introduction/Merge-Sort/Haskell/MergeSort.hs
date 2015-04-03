module MergeSort (mergesort) where

import Data.List (insert)

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
conquer x y = conquer' x y []
  where conquer' a@(a0:aTail) b@(b0:bTail) acc
          | null aTail = acc ++ (insert a0 b)
          | null bTail = acc ++ (insert b0 a)
          | a0 < b0    = conquer' aTail b (acc ++ [a0])
          | otherwise  = conquer' a bTail (acc ++ [b0])

