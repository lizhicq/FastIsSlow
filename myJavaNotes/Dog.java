package myJavaNotes;

public class Dog implements Animal {
    void praise(Dog a){
        System.out.print("u r cool dog");
    }

    public static void main(String[] args){
        Animal a = new Dog();
        Dog d = new Dog();
        d.praise(d);
        a.praise(d);
    }
}
