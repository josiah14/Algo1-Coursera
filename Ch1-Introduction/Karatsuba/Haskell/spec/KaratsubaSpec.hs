module KaratsubaSpec where

import Test.Hspec
import Test.QuickCheck
import Karatsuba as K
import Karatsuba0 as K0

-- -- configure quickcheck
-- customCheck p = quickCheckWith (stdArgs{ maxSuccess = whatever  }) p

main :: IO ()
main = hspec $ parallel $ do
  describe "K0.karatsuba" $ do
    it "returns the product of the arguments" $ property $
      \x y -> K0.karatsuba x y == x*y
  describe "K.Karatsuba" $ do
    it "returns the product of the arguments" $ property $
      \x y -> K.karatsuba x y == x*y

