tests/rustdoc/issue-100679-sidebar-links-deref.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="foo"]

pub struct Vec;

pub struct Slice;

impl std::ops::Deref for Vec {
    type Target = Slice;
    fn deref(&self) -> &Slice {
        &Slice
    }
}

// @has foo/struct.Vec.html '//*[@class="sidebar-elems"]//section//li/a[@href="#method.is_empty"]' \
//          "is_empty"
impl Vec {
    pub fn is_empty(&self) -> bool {
        true
    }
}

// @has foo/struct.Vec.html '//*[@class="sidebar-elems"]//section//li/a[@href="#method.is_empty-1"]' \
//          "is_empty"
// @has foo/struct.Slice.html '//*[@class="sidebar-elems"]//section//li/a[@href="#method.is_empty"]' \
//          "is_empty"
impl Slice {
    pub fn is_empty(&self) -> bool {
        true
    }
}


