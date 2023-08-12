tests/ui/borrowck/borrowck-move-in-irrefut-pat.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn with<F>(f: F) where F: FnOnce(&String) {}

fn arg_item(&_x: &String) {}
    //~^ ERROR [E0507]

fn arg_closure() {
    with(|&_x| ())
    //~^ ERROR [E0507]
}

fn let_pat() {
    let &_x = &"hi".to_string();
    //~^ ERROR [E0507]
}

pub fn main() {}


