tests/rustdoc/tuples.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/fn.tuple0.html //pre 'pub fn tuple0(x: ())'
// @snapshot link_unit - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn tuple0(x: ()) -> () { x }
// @has foo/fn.tuple1.html //pre 'pub fn tuple1(x: (i32,)) -> (i32,)'
// @snapshot link1_i32 - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn tuple1(x: (i32,)) -> (i32,) { x }
// @has foo/fn.tuple2.html //pre 'pub fn tuple2(x: (i32, i32)) -> (i32, i32)'
// @snapshot link2_i32 - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn tuple2(x: (i32, i32)) -> (i32, i32) { x }
// @has foo/fn.tuple1_t.html //pre 'pub fn tuple1_t<T>(x: (T,)) -> (T,)'
// @snapshot link1_t - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn tuple1_t<T>(x: (T,)) -> (T,) { x }
// @has foo/fn.tuple2_t.html //pre 'pub fn tuple2_t<T>(x: (T, T)) -> (T, T)'
// @snapshot link2_t - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn tuple2_t<T>(x: (T, T)) -> (T, T) { x }
// @has foo/fn.tuple2_tu.html //pre 'pub fn tuple2_tu<T, U>(x: (T, U)) -> (T, U)'
// @snapshot link2_tu - '//div[@class="item-decl"]/pre[@class="rust"]/code'
pub fn tuple2_tu<T, U>(x: (T, U)) -> (T, U) { x }


