public class star {
    
    public static void drawstar(int x, int y, int z){
        
        while (x <= y){
              z = 0;
              while (z <  x){
                  System.out.print('*');
                  z= z + 1;
              }
              System.out.println();
              x = x + 1;}


    }
    
    public static void main(String[] args){
        
        drawstar(1, 5, 0);
          }


    
}
