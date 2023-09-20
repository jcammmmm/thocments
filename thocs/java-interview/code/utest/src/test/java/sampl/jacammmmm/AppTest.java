package sampl.jacammmmm;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class AppTest {

	@Test
	@DisplayName("1 + 1 = 2")
	void addsTwoNumbers() {
		App calculator = new App();
		assertEquals(2, calculator.add(1, 1), "1 + 1 should equal 2");
	}

    // @Test
	void addsTwoComplexNumbers() {
		App calculator = new App();
        ComplexNumber z1 = mock(ComplexNumber.class);
        ComplexNumber z2 = new ComplexNumber(1, 2);
        when(z1.getReal()).thenReturn(3.0);
        when(z1.getImg()).thenReturn(4.0);
        // note the order of the operands. If you swap them the add method
        // got called on the mock, and a NPE will occur.
		assertTrue((new ComplexNumber(4, 6)).equals(calculator.add(z2, z1)));
	}

    @Test
	void addsTwoComplexNumbersSpy() {
		App calculator = new App();
        ComplexNumber z2 = new ComplexNumber(1, 2);
        ComplexNumber z3 = new ComplexNumber();
        ComplexNumber z3spy = spy(z3);

        when(z3spy.getReal()).thenReturn(3.0);
        when(z3spy.getImg()).thenReturn(1.0);

        // note the order of the operands. If you swap them the add method
        // got called on the mock that has the value 0.0i + 0.0
		assertTrue((new ComplexNumber(4, 3)).equals(calculator.add(z2, z3spy)));
	}

	@ParameterizedTest(name = "{0} + {1} = {2}")
	@CsvSource({
			"0,    1,   1",
			"1,    2,   3",
			"49,  51, 100",
			"1,  100, 101"
	})
	void add(int first, int second, int expectedResult) {
		App calculator = new App();
		assertEquals(expectedResult, calculator.add(first, second),
				() -> first + " + " + second + " should equal " + expectedResult);
	}
}