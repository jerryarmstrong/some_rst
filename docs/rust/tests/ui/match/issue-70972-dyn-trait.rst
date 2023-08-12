tests/ui/match/issue-70972-dyn-trait.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const F: &'static dyn Send = &7u32;

fn main() {
    let a: &dyn Send = &7u32;
    match a {
        F => panic!(),
        //~^ ERROR `&dyn Send` cannot be used in patterns
        _ => {}
    }
}


