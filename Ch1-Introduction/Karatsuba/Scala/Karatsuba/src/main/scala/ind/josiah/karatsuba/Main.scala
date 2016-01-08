package ind.josiah.karatsuba

import scala.util.{Try, Success, Failure}

import Karatsuba._

object Main {
  def main(args: Array[String]): Unit = {
    (for (x <- parseInt(args(0)); y <- parseInt(args(1))) yield karatsuba(x, y)) match {
      case Success(answer) => println(answer)
      case Failure(e) => System.err.println(e); System.exit(-1)
    }
  }

  private[this] def parseInt(num: String): Try[BigInt] = Try(BigInt.apply(num))
}
