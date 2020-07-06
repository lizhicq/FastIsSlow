package main.scala.com.chapter18.generictype

object GenericDemo01 {
  def main(args: Array[String]): Unit = {
    val intMessage = new IntMessage[Int](1)
    println(intMessage)
  }

  abstract class Message[v](s: v) {
    def get = s
  }

  class IntMessage[Int](v: Int) extends Message(v)

}