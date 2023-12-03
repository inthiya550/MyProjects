import java.util.*;
public class minicalculator{
public static void main(String args[]){
    Scanner sc=new Scanner(System.in);
    System.out.println("enter the first number:");
    int number1=sc.nextInt();
    System.out.println("enter the second number:");
    int number2=sc.nextInt();
    System.out.println("enter the operator to perform the operation:");
    char operator=sc.next().charAt(0);
    switch(operator){
        case '+':
            System.out.println("The addition of two numbers is:"+(number1+number2));
            break;
            case '-':
                System.out.println("The subtraction of the two numbers is:"+(number1-number2));
                break;
                case '*':
                    System.out.println("The multiplication of the two numbers is:"+(number1*number2));
                    break;
                    case '/':
                        System.out.println("The division of two numbers is:"+(number1/number2));
                        break;
                        default:
                            System.out.println("Please enter the correct operator:");
    }

}
}