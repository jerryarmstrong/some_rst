tests/ui/borrowck/borrowck-drop-from-guard.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(if_let_guard)]

fn foo(_:String) {}

fn main()
{
    let my_str = "hello".to_owned();
    match Some(42) {
        Some(_) if { drop(my_str); false } => {}
        Some(_) => {}
        None => { foo(my_str); } //~ ERROR [E0382]
    }

    let my_str = "hello".to_owned();
    match Some(42) {
        Some(_) if let Some(()) = { drop(my_str); None } => {}
        Some(_) => {}
        None => { foo(my_str); } //~ ERROR [E0382]
    }
}


