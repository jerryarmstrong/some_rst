tests/ui/issues/issue-5883.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A {}

struct Struct {
    r: dyn A + 'static
}

fn new_struct(
    r: dyn A + 'static //~ ERROR the size for values of type
) -> Struct {          //~ ERROR the size for values of type
    Struct { r: r }
}

fn main() {}


