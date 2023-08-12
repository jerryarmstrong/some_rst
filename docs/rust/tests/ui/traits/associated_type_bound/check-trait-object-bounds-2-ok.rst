tests/ui/traits/associated_type_bound/check-trait-object-bounds-2-ok.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure that we're handling bound lifetimes correctly when validating trait
// bounds.
// run-pass

trait X<'a> {
    type F: FnOnce(&i32) -> &'a i32;
}

fn f<T: for<'r> X<'r> + ?Sized>() {
    None::<T::F>.map(|f| f(&0));
}

fn main() {
    f::<dyn for<'x> X<'x, F = fn(&i32) -> &'x i32>>();
}


