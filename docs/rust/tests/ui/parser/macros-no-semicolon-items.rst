tests/ui/parser/macros-no-semicolon-items.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo()  //~ ERROR semicolon
                    //~| ERROR unexpected end of macro

macro_rules! bar {
    ($($tokens:tt)*) => {}
}

bar!( //~ ERROR semicolon
    blah
    blah
    blah
)

fn main() {
}


