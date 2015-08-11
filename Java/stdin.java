package com.example.hi;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class hello {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        String name = reader.nextLine();
        int number = Integer.parseInt(reader.nextLine());
        double dnum = Double.parseDouble(reader.nextLine());
        System.out.println("String: "+name);
        System.out.println("Double: "+dnum);
        System.out.println("Int: "+number);

    }
}


