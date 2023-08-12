tests/ui/cycle-trait/cycle-trait-supertrait-direct.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test a supertrait cycle where a trait extends itself.

trait Chromosome: Chromosome {
    //~^ ERROR cycle detected
}

fn main() { }


