tests/ui/issues/issue-74236/main.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// aux-build:dep.rs
// compile-flags:--extern dep

fn main() {
    // Trigger an error that will print the path of dep::private::Pub (as "dep::Renamed").
    let () = dep::Renamed;
    //~^ ERROR mismatched types
}


