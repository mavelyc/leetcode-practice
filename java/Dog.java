//TP - Object and Classes

public class Dog{
    int age;
    String color;
    void barking(){
        System.out.println("Barking");
    }

    void sleeping(){
        System.out.println("Sleeping");
    }

    void setDog(int a, String c){
        age = a;
        color = c;
    }

    void printDog(){
        System.out.println("This dog is " + age + " color is " + color);
    }

    public static void main (String []args){
        Dog d1 = new Dog();
        Dog d2 = new Dog();
        d1.setDog(10,"dog");
        d1.printDog();
        d1.age = 20;
        d1.printDog();
        //d1.barking();
    }
}
