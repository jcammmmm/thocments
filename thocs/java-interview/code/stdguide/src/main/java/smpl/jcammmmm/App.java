package smpl.jcammmmm;

import java.util.function.Supplier;
import java.util.stream.Stream;
import java.util.stream.LongStream;
import java.util.stream.DoubleStream;
import java.util.Random;
import java.lang.Integer;
import java.lang.Double;
import java.time.LocalTime;

/**
 * Hello world!
 *
 */
public class App {
    public static void main( String[] args ) {
        // App.streamSamples();
    }

    public static void multhreading() {
        
    }

    public static void streamSamples() {
       // Serial Processing
        Random rnd = new Random(11223344L);
        DoubleStream doubles = rnd.doubles().limit(100_000_000L);
        long start = LocalTime.now().toNanoOfDay();
        // commented due shor-circuiting behavior
        // System.out.println(doubles.findFirst().orElse(999.0));
        // System.out.println(doubles.findAny().orElse(999.0));
        double result1 = doubles.filter(d -> d < 0.5).sum();
        System.out.println(result1);
        System.out.println((LocalTime.now().toNanoOfDay() - start)/1_000_000_000.0 + "s");

        // Parallel Processing
        rnd = new Random(11223344L);
        doubles = rnd.doubles().parallel().limit(100_000_000L).unordered();
        double result2 = doubles.filter(d -> d < 0.5).sum();
        System.out.println(result2);
        System.out.println((LocalTime.now().toNanoOfDay() - start)/1_000_000_000.0   + "s");
    }
}
