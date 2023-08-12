tests/ui/drop/repeat-drop-2.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn borrowck_catch() {
    let foo = String::new();
    let _bar = foo;
    let _baz = [foo; 0]; //~ ERROR use of moved value: `foo` [E0382]
}

const _: [String; 0] = [String::new(); 0];
//~^ ERROR destructor of `String` cannot be evaluated at compile-time [E0493]

fn must_be_init() {
    let x: u8;
    let _ = [x; 0]; //~ ERROR E0381
}

fn main() {}


