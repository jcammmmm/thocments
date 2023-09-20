package sampl.jacammmmm;

public class ComplexNumber {

    private final double r;
    private final double i;

    public ComplexNumber(double r, double i) {
        this.r = r;
        this.i = i;
    }

    public ComplexNumber() {
        this.r = 0;
        this.i = 0;
    }

	public ComplexNumber add(ComplexNumber b) {
		return new ComplexNumber(r + b.getReal(), i + b.getImg());
	}

    public double getReal() {
        return r;
    }

    public double getImg() {
        return i;
    }

    public boolean equals(ComplexNumber z) {
        return this.r == z.getReal() && this.i == z.getImg();
    }

    public String toString() {
        return String.format("%fi + %f", this.getReal(), this.getImg());
    }
    
}