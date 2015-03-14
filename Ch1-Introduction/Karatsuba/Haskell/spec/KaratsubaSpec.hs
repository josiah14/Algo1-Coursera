module KaratsubaSpec where

import Test.Hspec
import Test.QuickCheck
import Karatsuba as K
import Karatsuba0 as K0

main :: IO ()
main = hspec $ parallel $ do
  describe "K0.karatsuba" $ do
    it "returns the product of the arguments" $ property $
      \x y -> K0.karatsuba x y == x*y
    it "returns the product of very large argements" $ do
      K0.karatsuba 21340987563249087947532356 90985623498562498576492386 `shouldBe` 21340987563249087947532356*90985623498562498576492386
  describe "K.Karatsuba" $ do
    it "returns the product of the arguments" $ property $
      \x y -> K.karatsuba x y == x*y
    it "returns the product of very large argements" $ do
      K.karatsuba 21340987563249087947532356 90985623498562498576492386 `shouldBe` 21340987563249087947532356*90985623498562498576492386

