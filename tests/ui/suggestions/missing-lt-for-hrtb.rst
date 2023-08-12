tests/ui/suggestions/missing-lt-for-hrtb.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct X<'a>(&'a ());
struct S<'a>(&'a dyn Fn(&X) -> &X);
//~^ ERROR missing lifetime specifiers
struct V<'a>(&'a dyn for<'b> Fn(&X) -> &X);
//~^ ERROR missing lifetime specifiers

fn main() {
    let x = S(&|x| {
        println!("hi");
        x
    });
    x.0(&X(&()));
}


