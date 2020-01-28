package main.scala.com.chapter18.generictype

object GenericDemo02 {
  def main(args: Array[String]): Unit = {
    println("yes")
  }
}

class EnglishClass[A,B,C](val classSeason:A, val className: B, val classType:C)

//Season is enum type
class SeasonEnum extends Enumeration{
  type SeasonEnum = Value
  val spring, autum, summer, winter = Value
}