tests/ui/parser/issues/issue-68000-unicode-ident-after-missing-comma.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo {
    pub bar: Vec<i32>ö
    //~^ ERROR expected `,`, or `}`, found `ö`
} //~ ERROR expected `:`, found `}`

fn main() {}


