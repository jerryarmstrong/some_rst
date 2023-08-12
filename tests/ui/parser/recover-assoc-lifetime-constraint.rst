tests/ui/parser/recover-assoc-lifetime-constraint.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(FALSE)]
fn syntax() {
    bar::<Item = 'a>(); //~ ERROR associated lifetimes are not supported
}

fn main() {}


