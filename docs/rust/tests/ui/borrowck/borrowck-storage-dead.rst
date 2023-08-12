tests/ui/borrowck/borrowck-storage-dead.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn ok() {
    loop {
        let _x = 1;
    }
}

fn also_ok() {
    loop {
        let _x = String::new();
    }
}

fn fail() {
    loop {
        let x: i32;
        let _ = x + 1; //~ERROR [E0381]
    }
}

fn main() {
    ok();
    also_ok();
    fail();
}


