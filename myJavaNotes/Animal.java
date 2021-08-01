package myJavaNotes;

public interface Animal {
    default void praise(Animal a){
        System.out.print("u r cool animal");
    }
}
