tests/ui/closures/closure-no-fn-4.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let b = 2;
    let _: fn(usize) -> usize = match true {
        true => |a| a + 1,
        false => |a| a - b,
        //~^ ERROR `match` arms have incompatible types
    };
}


