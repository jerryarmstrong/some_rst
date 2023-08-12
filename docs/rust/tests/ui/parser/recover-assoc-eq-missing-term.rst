tests/ui/parser/recover-assoc-eq-missing-term.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(FALSE)]
fn syntax() {
    bar::<Item =   >(); //~ ERROR missing type to the right of `=`
}

fn main() {}


