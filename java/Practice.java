//testing oo understanding

/*
public class Practice{
    String name;

    Practice(String n){
        name = n;
    }

    public void print(){
        System.out.println("Hello my name is " + name);
    }

    public static void main(String args[]){
        Practice t1 = new Practice("Christian");
        Practice t2 = new Practice("Michael");
        t1.print();
        t2.print();
    }
}
*/

abstract class Test{
    abstract void print();
}

class Sub extends Test{
    void print(){
        System.out.println("Hello");
    }
}

public class Practice{
    public static void main(String []args){
        Sub sc = new Sub();
        sc.print();
    }
}