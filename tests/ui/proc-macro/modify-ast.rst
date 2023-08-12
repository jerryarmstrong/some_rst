tests/ui/proc-macro/modify-ast.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:modify-ast.rs

extern crate modify_ast;

use modify_ast::*;

#[derive(Foo)]
pub struct MyStructc {
    #[cfg_attr(my_cfg, foo)]
    _a: i32,
}

macro_rules! a {
    ($i:item) => ($i)
}

a! {
    #[assert1]
    pub fn foo() {}
}

fn main() {
    let _a = MyStructc { _a: 0 };
    foo();
}


