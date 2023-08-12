tests/ui/self/self_type_keyword-2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use self::Self as Foo; //~ ERROR unresolved import `self::Self`

pub fn main() {
    let Self = 5;
    //~^ ERROR cannot find unit struct, unit variant or constant `Self` in this scope

    match 15 {
        Self => (),
        //~^ ERROR cannot find unit struct, unit variant or constant `Self` in this scope
        Foo { x: Self } => (),
        //~^ ERROR cannot find unit struct, unit variant or constant `Self` in this scope
    }
}


