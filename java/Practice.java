//testing oo understanding


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
    