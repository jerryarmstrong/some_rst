tests/ui/macros/span-covering-argument-1.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! bad {
    ($s:ident whatever) => {
        {
            let $s = 0;
            *&mut $s = 0;
            //~^ ERROR cannot borrow `foo` as mutable, as it is not declared as mutable [E0596]
        }
    }
}

fn main() {
    bad!(foo whatever);
}


