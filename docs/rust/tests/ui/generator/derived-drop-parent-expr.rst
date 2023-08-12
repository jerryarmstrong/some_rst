tests/ui/generator/derived-drop-parent-expr.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// compile-flags:-Zdrop-tracking

//! Like drop-tracking-parent-expression, but also tests that this doesn't ICE when building MIR
#![feature(generators)]

fn assert_send<T: Send>(_thing: T) {}

#[derive(Default)]
pub struct Client { pub nickname: String }

fn main() {
    let g = move || match drop(Client { ..Client::default() }) {
        _status => yield,
    };
    assert_send(g);
}


