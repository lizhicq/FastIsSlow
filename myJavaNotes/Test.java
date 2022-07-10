package myJavaNotes;

import java.util.stream.Collectors;
import java.util.stream.*;
import java.util.*;

public class Test {
    public static void main(String[] args) {
        Set<String> set = Stream.of("a", "b", "c").collect(Collectors.toCollection(HashSet::new));
        System.out.println(set);
    }
}
