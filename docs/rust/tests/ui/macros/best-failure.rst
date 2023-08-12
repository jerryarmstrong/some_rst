tests/ui/macros/best-failure.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! number {
    (neg false, $self:ident) => { $self };
    ($signed:tt => $ty:ty;) => {
        number!(neg $signed, $self);
        //~^ ERROR no rules expected the token `$`
    };
}

number! { false => u8; }

fn main() {}


