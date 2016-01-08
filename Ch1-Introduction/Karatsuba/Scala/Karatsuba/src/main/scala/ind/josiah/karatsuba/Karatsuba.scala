package ind.josiah.karatsuba

object Karatsuba {
  def karatsuba(x: BigInt, y: BigInt): BigInt = {
    x * y
  }

  private[this] def numDigits(x: BigInt): BigInt = ???

  private[this] def split(i: Int, num: BigInt): (BigInt, BigInt) = ???
}
