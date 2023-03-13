import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
       Scanner key= new Scanner(System.in);
        HashMap<String,String> rpsfGame= new HashMap<>();

        rpsfGame.put("Rock","Paper");
        rpsfGame.put("Paper","Scissors");
        rpsfGame.put("Scissors","Rock");
        rpsfGame.put("Fox","Foxen");

        int N= key.nextInt();
        key.nextLine();

        String [] inps= new String[N];
        for(int s= 0; s< inps.length; s++){
            inps[s]= key.nextLine();
        }
        ArrayList <String> outs= new ArrayList<>();
        for (String i : inps){

            if (i.compareTo("Foxen")==0){
                break;
            }
            else{
                outs.add(rpsfGame.get(i));
            }
        }

        for (String j: outs){
            System.out.println(j);
        }
        
        
    }
}
