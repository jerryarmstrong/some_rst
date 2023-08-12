tests/ui/typeck/typeck-default-trait-impl-negation-send.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

struct MySendable {
   t: *mut u8
}

unsafe impl Send for MySendable {}

struct MyNotSendable {
   t: *mut u8
}

impl !Send for MyNotSendable {}

fn is_send<T: Send>() {}

fn main() {
    is_send::<MySendable>();
    is_send::<MyNotSendable>();
    //~^ ERROR `MyNotSendable` cannot be sent between threads safely
}


