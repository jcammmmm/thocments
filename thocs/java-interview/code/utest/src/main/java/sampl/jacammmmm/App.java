package sampl.jacammmmm;

/*
 * Copyright 2015-2022 the original author or authors.
 *
 * All rights reserved. This program and the accompanying materials are
 * made available under the terms of the Eclipse Public License v2.0 which
 * accompanies this distribution and is available at
 *
 * http://www.eclipse.org/legal/epl-v20.html
 */

public class App {

	public int add(int a, int b) {
		return a + b;
	}

	public ComplexNumber add(ComplexNumber a, ComplexNumber b) {
        System.out.println("###########################");
        System.out.println(a);
        System.out.println(b);
        System.out.println("###########################");
		return a.add(b);
	}

    public static void main(String... args) {
        System.out.println("buahhahahaah!");
    }
    
}