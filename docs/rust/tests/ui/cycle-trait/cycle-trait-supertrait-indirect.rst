tests/ui/cycle-trait/cycle-trait-supertrait-indirect.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test a supertrait cycle where the first trait we find (`A`) is not
// a direct participant in the cycle.

trait A: B {
}

trait B: C {
    //~^ ERROR cycle detected
}

trait C: B { }

fn main() { }


