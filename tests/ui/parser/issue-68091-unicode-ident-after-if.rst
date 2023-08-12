tests/ui/parser/issue-68091-unicode-ident-after-if.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! x {
    ($($c:tt)*) => {
        $($c)ö* {}
        //~^ ERROR missing condition for `if` expression
    };
}

fn main() {
    x!(if);
}


