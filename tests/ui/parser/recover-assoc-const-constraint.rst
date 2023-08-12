tests/ui/parser/recover-assoc-const-constraint.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(FALSE)]
fn syntax() {
    bar::<Item = 42>();
    //~^ ERROR associated const equality is incomplete
    bar::<Item = { 42 }>();
    //~^ ERROR associated const equality is incomplete
}

fn main() {}


