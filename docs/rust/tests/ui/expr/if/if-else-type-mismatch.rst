tests/ui/expr/if/if-else-type-mismatch.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = if true {
        1i32
    } else {
        2u32
    };
    //~^^ ERROR `if` and `else` have incompatible types
    let _ = if true { 42i32 } else { 42u32 };
    //~^ ERROR `if` and `else` have incompatible types
    let _ = if true {
        3u32;
    } else {
        4u32
    };
    //~^^ ERROR `if` and `else` have incompatible types
    let _ = if true {
        5u32
    } else {
        6u32;
    };
    //~^^ ERROR `if` and `else` have incompatible types
    let _ = if true {
        7i32;
    } else {
        8u32
    };
    //~^^ ERROR `if` and `else` have incompatible types
    let _ = if true {
        9i32
    } else {
        10u32;
    };
    //~^^ ERROR `if` and `else` have incompatible types
    let _ = if true {

    } else {
        11u32
    };
    //~^^ ERROR `if` and `else` have incompatible types
    let _ = if true {
        12i32
    } else {

    };
    //~^^^ ERROR `if` and `else` have incompatible types
}


