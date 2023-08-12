tests/ui/compare-method/region-unrelated.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we elaborate `Type: 'region` constraints and infer various important things.

trait Master<'a, T: ?Sized, U> {
    fn foo() where T: 'a;
}

// `U: 'a` does not imply `V: 'a`
impl<'a, U, V> Master<'a, U, V> for () {
    fn foo() where V: 'a { }
    //~^ ERROR impl has stricter requirements than trait
}

fn main() {
    println!("Hello, world!");
}


