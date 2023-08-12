tests/ui/recursion/issue-26548-recursion-via-normalize.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //~ ERROR cycle detected when computing layout of `core::option::Option<S>`
//~| NOTE ...which requires computing layout of `S`...
//~| NOTE ...which requires computing layout of `core::option::Option<<S as Mirror>::It>`...
//~| NOTE ...which again requires computing layout of `core::option::Option<S>`, completing the cycle
//~| NOTE cycle used when computing layout of `core::option::Option<<S as Mirror>::It>`

trait Mirror {
    type It: ?Sized;
}
impl<T: ?Sized> Mirror for T {
    type It = Self;
}
struct S(Option<<S as Mirror>::It>);

fn main() {
    let _s = S(None);
}


