tests/ui/hygiene/items.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// ignore-pretty pretty-printing is unhygienic

#![feature(decl_macro)]

pub macro m($foo:ident, $f:ident, $e:expr) {
    mod foo {
        pub fn f() -> u32 { 0 }
        pub fn $f() -> u64 { 0 }
    }

    mod $foo {
        pub fn f() -> i32 { 0 }
        pub fn $f() -> i64 { 0  }
    }

    let _: u32 = foo::f();
    let _: u64 = foo::$f();
    let _: i32 = $foo::f();
    let _: i64 = $foo::$f();
    let _: i64 = $e;
}

fn main() {
    m!(foo, f, foo::f());
    let _: i64 = foo::f();
}


