module KaratsubaSpec where

import Test.Hspec
import Test.QuickCheck
import Karatsuba

-- -- configure quickcheck
-- customCheck p = quickCheckWith (stdArgs{ maxSuccess = whatever  }) p

main :: IO ()
main = hspec $ parallel $ do
  describe "karatsuba" $ do
