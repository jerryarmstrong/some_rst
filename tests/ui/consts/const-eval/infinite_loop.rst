tests/ui/consts/const-eval/infinite_loop.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // Tests the Collatz conjecture with an incorrect base case (0 instead of 1).
    // The value of `n` will loop indefinitely (4 - 2 - 1 - 4).
    let _ = [(); {
        let mut n = 113383; // #20 in https://oeis.org/A006884
        while n != 0 {
            //~^ ERROR evaluation of constant value failed
            n = if n % 2 == 0 { n/2 } else { 3*n + 1 };
        }
        n
    }];
}


