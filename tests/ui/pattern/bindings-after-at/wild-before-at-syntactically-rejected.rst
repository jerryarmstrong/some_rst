tests/ui/pattern/bindings-after-at/wild-before-at-syntactically-rejected.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Here we check that `_ @ sub` is syntactically invalid
// and comes with a nice actionable suggestion.

fn main() {}

#[cfg(FALSE)]
fn wild_before_at_is_bad_syntax() {
    let _ @ a = 0;
    //~^ ERROR pattern on wrong side of `@`
    let _ @ ref a = 0;
    //~^ ERROR pattern on wrong side of `@`
    let _ @ ref mut a = 0;
    //~^ ERROR pattern on wrong side of `@`
    let _ @ (a, .., b) = (0, 1, 2, 3);
    //~^ ERROR left-hand side of `@` must be a binding
}


