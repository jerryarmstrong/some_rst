tests/rustdoc/array-links.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]
#![no_std]

pub struct MyBox<T: ?Sized>(*const T);

// @has 'foo/fn.alpha.html'
// @snapshot link_slice_u32 - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn alpha() -> &'static [u32; 1] {
    loop {}
}

// @has 'foo/fn.beta.html'
// @snapshot link_slice_generic - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn beta<T>() -> &'static [T; 1] {
    loop {}
}

// @has 'foo/fn.gamma.html'
// @snapshot link_box_u32 - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn gamma() -> MyBox<[u32; 1]> {
    loop {}
}

// @has 'foo/fn.delta.html'
// @snapshot link_box_generic - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn delta<T>() -> MyBox<[T; 1]> {
    loop {}
}


