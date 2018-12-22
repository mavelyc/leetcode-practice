//TP - Case Study

class Employee{
    private String name;
    private int age;
    private String designation;
    private double salary;

    public Employee(String name){
        this.name = name;
    }

    public void setAge(int empAge){
        age = empAge;
    }

    public void setDesignation (String empDesig){
        designation = empDesig;
    }

    public void setSalary(double empSalary){
        salary = empSalary;
    }

    public void printEmployee(){
        System.out.println("Name:" + name);
        System.out.println("Age:" + age);
        System.out.println("Designation:" + designation);
        System.out.println("Salary:" + salary);
    }
}


public class EmployeeTest{

    public static void main(String []args){
        Employee empOne = new Employee("James Smith");
        Employee empTwo = new Employee("Mary Anne");

        empOne.setAge(26);
        empOne.setDesignation("Senior Software Engieer");
        empOne.setSalary(1000);
        empOne.printEmployee();

        empTwo.setAge(21);
        empTwo.setDesignation("Software Engineer");
        empTwo.setSalary(500);
        empTwo.printEmployee();

    }
}
