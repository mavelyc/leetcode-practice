//loop control practice


public class Loopcontrol {
    public static void main (String args[]){
        int x = 10;
        while (x < 20) {
            System.out.print("value of x : " + x);
            x++;
            if(x==20){
                break;
            }
            System.out.print("\n");
        }
    }
}