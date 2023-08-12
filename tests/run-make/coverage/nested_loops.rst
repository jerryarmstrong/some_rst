tests/run-make/coverage/nested_loops.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let is_true = std::env::args().len() == 1;
    let mut countdown = 10;

    'outer: while countdown > 0 {
        let mut a = 100;
        let mut b = 100;
        for _ in 0..50 {
            if a < 30 {
                break;
            }
            a -= 5;
            b -= 5;
            if b < 90 {
                a -= 10;
                if is_true {
                    break 'outer;
                } else {
                    a -= 2;
                }
            }
        }
        countdown -= 1;
    }
}


