import org.scalatest._
import org.scalacheck.Prop._
import org.scalatest.prop.Checkers._
import ind.josiah.karatsuba._

class KaratsubaSpec extends FlatSpec with Matchers {
  "karatsuba" should "return the correct product for generic numbers" in {
    check((x: BigInt, y: BigInt) => Karatsuba.karatsuba(x, y) == x * y)
  }

  "karatsuba" should "return the correct product for very large numbers" in {
    assert(
      Karatsuba.karatsuba(
        BigInt.apply("21340987563249087947532356"),
        BigInt.apply("90985623498562498576492386")
      ) == (
        BigInt.apply("21340987563249087947532356")
        * BigInt.apply("90985623498562498576492386")
      )
    )
  }

}
