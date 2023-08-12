tests/ui/pattern/usefulness/refutable-pattern-errors.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn func((1, (Some(1), 2..=3)): (isize, (Option<isize>, isize))) { }
//~^ ERROR refutable pattern in function argument
//~| `(_, _)` not covered

fn main() {
    let (1, (Some(1), 2..=3)) = (1, (None, 2));
    //~^ ERROR refutable pattern in local binding
    //~| `(i32::MIN..=0_i32, _)` and `(2_i32..=i32::MAX, _)` not covered
}


