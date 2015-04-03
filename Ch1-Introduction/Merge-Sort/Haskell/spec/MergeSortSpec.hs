module MergeSortSpec where

import Test.Hspec
import Test.QuickCheck
import Data.List (sort)
import MergeSort as M

main :: IO ()
main = hspec $ parallel $ do
  describe "M.mergesort" $ do
    it "sorts a list of arbitrary length and values" $ verbose $ property $
      \xs -> M.mergesort xs == sort xs

